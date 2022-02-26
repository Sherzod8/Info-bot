from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from utils.db_api.database import DBcommands
from data.config import I18N_DOMAIN, LOCALES_DIR

db=DBcommands()

async def get_lang(user_id):
    user = await db.get_user(user_id)
    if user:
        return user.language


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action, args):
        user=types.User.get_current()
        return await get_lang(str(user.id)) or user.locale

i18n=ACLMiddleware(I18N_DOMAIN,LOCALES_DIR)

_ = i18n.gettext