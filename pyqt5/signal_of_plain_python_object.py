from dataclasses import dataclass
from enum import Enum

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


@dataclass
class Message:
    id: int
    name: str


class MessageType(Enum):
    Basic = 'basic'
    Private = 'private'


class From(QObject):
    message = pyqtSignal(Message, MessageType)

    def __init__(self):
        super().__init__()

    def do_something(self):
        self.message.emit(Message(1, 'wenjun'), MessageType.Private)


class To(QObject):
    def __init__(self):
        super().__init__()

    @pyqtSlot(Message, MessageType)
    def on_message(self, message: Message, type: MessageType):
        print(message)


f = From()
t = To()
f.message.connect(t.on_message)

f.do_something()
f.do_something()
f.do_something()
