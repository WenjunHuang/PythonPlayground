import functools
import sys
import asyncio
import aiohttp
from PyQt5.QtCore import QUrl, QObject, pyqtSlot
from PyQt5.QtQml import QQmlApplicationEngine, QJSValue, qjsEngine, qmlRegisterType
from asyncqt import QEventLoop, asyncSlot, asyncClose
from PyQt5.QtGui import QGuiApplication
from typing import List

from desktop.lib.http import init_session
from desktop.lib.models import Account

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
loop = QEventLoop(app)
asyncio.set_event_loop(loop)

# loop = asyncio.get_event_loop()
token = 'bc0706b46ea74b7009c82c2204358d96c04e4680'
endpoint = "https://api.github.com"
# self.api_repositories_store = ApiRepositoriesStore(FakeAccountStore())
init_session()

qmlRegisterType(Account, 'Desktop', 1, 0, 'Account')

engine.load(QUrl("async.qml"))
if not engine.rootObjects():
    sys.exit(-1)

asyncio.events._set_running_loop(loop)
with loop:
    sys.exit(loop.run_forever())
