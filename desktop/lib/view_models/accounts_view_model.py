from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtQml import QJSValue, qjsEngine
from tornado.platform import asyncio

from desktop.lib.api import APIEmailData
from desktop.lib.common import with_logger
from desktop.lib.models.account import Account
from desktop.lib.stores.accounts_store import AccountsStore


@with_logger
class AccountsViewModel(QObject):
    def __init__(self, accounts_store: AccountsStore, parent=None):
        super().__init__(parent)
        self._accounts_store = accounts_store

    @pyqtSlot(QJSValue, name="getAllAccounts")
    def get_all_accounts(self, callback: QJSValue):
        async def work(callback: QJSValue):
            js_engine = qjsEngine(self)
            try:
                accounts = await self._accounts_store.get_all()

                result_arrays = js_engine.newArray(len(accounts))
                for i, account in enumerate(accounts):
                    obj = js_engine.newObject()
                    obj.setProperty(Account.endpoint.name, account.endpoint)
                    obj.setProperty(Account.token, account.token)
                    obj.setProperty(Account.avatar_url.name, account.avatar_url)
                    obj.setProperty(Account.name.name, account.name)
                    obj.setProperty(Account.id.name, account.id)
                    obj.setProperty(Account.login.name, account.login)

                    # emails
                    emails = js_engine.newArray(len(account.emails))
                    for j, email in enumerate(account.emails):
                        email_obj = js_engine.newObject()
                        email_obj.setProperty(APIEmailData.primary.name, email.primary)
                        email_obj.setProperty(APIEmailData.visibility.name, email.visibility.value)
                        email_obj.setProperty(APIEmailData.verified.name, email.verified)
                        email_obj.setProperty(APIEmailData.email.name, email.email)
                        emails.setProperty(j, email_obj)
                    obj.setProperty(Account.emails.name, emails)

                    result_arrays.setProperty(i, obj)

                callback.call([result_arrays])
            except Exception as e:
                self.logger.error(f'error in get_all_accounts', e)
                error = js_engine.newErrorObject(QJSValue.GenericError, 'error')
                callback.call([error])

        asyncio.create_task(work(QJSValue(callback)))

    async def async_fetch(self, url, callback: QJSValue):
        try:
            async with self.session.get(url) as r:
                result = await r.text()

        except Exception as e:
            result = f"Error: {e}"
        print(result)

        engine = qjsEngine(self)
        result_object = engine.newObject()
        result_object.setProperty("result", QJSValue(result))
        # result = [QJSValue(result)]
        result = [result_object]
        callback.call(result)
