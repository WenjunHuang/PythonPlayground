import random
import sys
from PyQt5.QtCore import QObject, QUrl, pyqtProperty
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlEngine, QQmlComponent, qmlRegisterType, QQmlListProperty,qmlRegisterExtendedType
from .lineedit import LineEditExtension

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)

    qmlRegisterExtendedType()
    engine = QQmlEngine()
    component = QQmlComponent(engine)
    component.loadUrl(QUrl('./example.qml'))
    party = component.create()

    if party and party.host:
        print(f"{party.host.name} is having a birthday party")
        print("They are inviting:")
        for guest in party.all_guests():
            print(f"    {guest.name}")
    else:
        for error in component.errors():
            print(error.description())
