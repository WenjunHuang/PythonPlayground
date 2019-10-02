from dataclasses import is_dataclass, fields
from functools import singledispatch
from typing import Optional, Any

from PyQt5.QtQml import QJSEngine, QJSValue


@singledispatch
def to_jsobject(data, js_engine: QJSEngine) -> Optional[Any]:
    if is_dataclass(data):
        js_obj = js_engine.newObject()
        for f in fields(data):
            v = data[f.name]
            if isinstance(v, list):
                js_array = js_engine.newArray()
                for idx, v in enumerate(v):
                    if is_dataclass(v):
                        result = to_jsobject(v, js_engine)
                    else:
                        result = v
                    js_array.setProperty(idx, result)
                js_obj.setProperty(f.name, js_array)
            elif is_dataclass(v):
                result = to_jsobject(v, js_engine)
                js_obj.setProperty(f.name, result)
            else:
                js_obj.setProperty(f.name, v)

        return js_obj
    else:
        return None


@to_jsobject.register(str)
@to_jsobject.register(int)
@to_jsobject.register(bool)
@to_jsobject.register(float)
def _(data, js_engine: QJSEngine):
    return QJSValue(data)


@to_jsobject.register(list)
def _(data: list, js_engine: QJSEngine):
    js_array = js_engine.newArray()
    for idx, v in enumerate(data):
        result = to_jsobject(v, js_engine)
        js_array.setProperty(idx, result)
    return js_array
