from asyncio import Queue, create_task
from typing import AsyncGenerator, Any

from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot
from PyQt5.QtQml import QQmlEngine, QJSValue
from PyQt5.QtQuick import QQuickItem
from rx.subject import BehaviorSubject
from desktop.lib.static import qqmlApplicationEngine


class Bloc(QObject):
    def __init__(self):
        self._event_queue = Queue()
        self._state_subject = BehaviorSubject(self.initial_state())

    def initial_state(self) -> Any:
        raise NotImplementedError()

    def current_state(self):
        return self._state_subject.value

    def state(self):
        return self._state_subject

    def dispose(self):
        self._state_subject.dispose()

    def on_error(self, error):
        pass

    def create_event(self, event_name: str, event_props: QJSValue) -> Any:
        raise NotImplementedError()

    def dispatch(self, event_name: str, event_props: QJSValue):
        event = self.create_event(event_name, event_props)
        create_task(self._dispatch(event))

    async def _dispatch(self, event):
        await self._event_queue.put(event)

    async def map_event_to_state(self, event) -> AsyncGenerator:
        raise NotImplementedError()

    async def _bind_state_subject(self):
        create_task(self._transform_events())

    async def _transform_events(self):
        while True:
            event = await self._event_queue.get()
            try:
                async for state in self.map_event_to_state(event):
                    self._state_subject.on_next(state)
            except Exception as e:
                self.on_error(e)

            self._event_queue.task_done()


class BlockProvider(QQuickItem):
    BlocTypes = {}

    @classmethod
    def register(cls, blocCls):
        cls.BlocTypes[blocCls.__name__] = blocCls

    @classmethod
    def create_bloc(cls, name: str):
        blocCls = cls.BlocTypes.get(name, None)
        if not blocCls:
            return blocCls()
        else:
            return None


class BlockBuilder(QQuickItem):
    stateChanged = pyqtSignal(Any, arguments=['state'])

    def __init__(self, parent=None):
        super().__init__(parent)
        self._disposable = None
        self._bloc = None

    @pyqtProperty(str)
    def blocName(self):
        return self._bloc_name

    @blocName.setter
    def blocName(self, value: str):
        ctx = QQmlEngine.contextForObject(self)
        ctx.contextProperty(value)
        bloc = BlockBuilder.create_bloc(value)
        if bloc:
            self.bloc = bloc

    @pyqtSlot(str, QJSValue)
    def dispatch(self, event_name: str, args: QJSValue):
        if self._bloc:
            self._bloc.dispatch(event_name, args)
