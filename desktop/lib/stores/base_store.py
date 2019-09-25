from pyee import BaseEventEmitter
from abc import ABC


class BaseStore(ABC):
    def __init__(self):
        self._emitter = BaseEventEmitter()

    def emit_update(self, data):
        self._emitter.emit('did-update', data)

    def emit_error(self, error: Exception):
        self._emitter.emit('did-error', error)
