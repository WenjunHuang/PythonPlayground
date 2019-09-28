import random
import sys
from PyQt5.QtCore import QObject, QUrl, pyqtProperty, pyqtSlot, Qt, Q_CLASSINFO, QDate
from PyQt5.QtGui import QGuiApplication, QColor
from PyQt5.QtQml import QQmlApplicationEngine, QQmlEngine, QQmlComponent, qmlRegisterType, QQmlListProperty, \
    qmlAttachedPropertiesObject


class ShoeDescription(QObject):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

    @pyqtProperty(int)
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int) -> None:
        self._size = value

    @pyqtProperty(QColor)
    def color(self) -> QColor:
        return self._color

    @color.setter
    def color(self, value: QColor):
        self._color = value

    @pyqtProperty(str)
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value: str):
        self._brand = value

    @pyqtProperty(float)
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        self._price = value


class Person(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._name = None
        self._shoe = ShoeDescription(self, size=0, color=Qt.white, price=0.0, brand="")

    @pyqtProperty(str)
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @pyqtProperty(ShoeDescription)
    def shoe(self) -> ShoeDescription:
        return self._shoe


class Boy(Person):
    pass


class Girl(Person):
    pass


class BirthdayParty(QObject):
    Q_CLASSINFO('DefaultProperty', 'guests')

    def __init__(self, parent=None):
        super().__init__(parent)
        self._guests = []

    @pyqtSlot(str, bool)
    def invite(self, name: str, boy: bool):
        if boy:
            person = Boy()
        else:
            person = Girl()
        person.name = name
        self._guests.append(person)

    def append_guest(self, property, p: Person):
        self._guests.append(p)

    def guest_count(self, property):
        return len(self._guests)

    def guest(self, property, index: int):
        return self._guests[index]

    def clear_guests(self, property):
        self._guests.clear()

    def all_guests(self):
        return self._guests

    @pyqtProperty(Person)
    def host(self) -> Person:
        return self._host

    @host.setter
    def host(self, value: Person) -> None:
        self._host = value

    @pyqtProperty(QQmlListProperty)
    def guests(self):
        return QQmlListProperty(Person, self, append=self.append_guest,
                                count=self.guest_count, at=self.guest,
                                clear=self.clear_guests)


class BirthdayPartyAttached(QObject):
    def __init__(self,parent=None):
        super().__init__(parent)
        self._rsvp = QDate()

    @pyqtProperty(QDate)
    def rsvp(self):
        return self._rsvp

    @rsvp.setter
    def rsvp(self, value: QDate):
        self._rsvp = value


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    qmlRegisterType(Person)
    qmlRegisterType(ShoeDescription)
    qmlRegisterType(BirthdayPartyAttached)
    qmlRegisterType(Boy, "People", 1, 0, "Boy")
    qmlRegisterType(Girl, "People", 1, 0, "Girl")
    qmlRegisterType(BirthdayParty, "People", 1, 0, "BirthdayParty", BirthdayPartyAttached)
    engine = QQmlEngine()
    component = QQmlComponent(engine)
    component.loadUrl(QUrl('./example.qml'))
    party = component.create()

    if party and party.host:
        print(f"{party.host.name} is having a birthday party")
        print("They are inviting:")
        for guest in party.all_guests():
            attached = qmlAttachedPropertiesObject(BirthdayParty, guest, False)
            rsvpDate = None
            if attached:
                rsvpDate = attached.rsvp

            if rsvpDate:
                print(f"    {guest.name} RSVP date:{rsvpDate.toString()}")
            else:
                print(f"    {guest.name} RSVP date: has not rsvp yet")

        bestShoe = None
        for guest in party.all_guests():
            if not bestShoe or bestShoe.shoe.price < guest.shoe.price:
                bestShoe = guest

        if bestShoe:
            print(f"{bestShoe.name} is wearing the best shoes!")
    else:
        for error in component.errors():
            print(error.description())
