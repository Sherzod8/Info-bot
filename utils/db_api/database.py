from gino import Gino
from data.config import DB_HOST, DB_NAME, DB_PASS,DB_USER
db = Gino()
from aiogram import types

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String)
    tg_id = db.Column(db.String)

class DBcommands():
    async def add_user(self):
        user = types.User.get_current()
        old_user  = await self.get_user(str(user.id))
        if old_user:
            return old_user
        new_user = User()
        new_user.tg_id = str(user.id)
        await new_user.create()
        return new_user
        
    async def user_caunt(self):
        list1 = await User.query.gino.all()
        soni = [i.tg_id for i in list1]
        return len(soni)
    
    async def get_user(self, user_id):
        user = await User.query.where(User.tg_id == user_id).gino.first()
        return user
    async def set_language(self, lang):
        user = types.User.get_current()
        user = await self.get_user(str(user.id))
        user = await user.update(language=lang).apply()

async def create_db():
    # await db.set_bind(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    await db.set_bind(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")
    await db.gino.create_all()
    # await db.gino.drop_all()