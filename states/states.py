from aiogram.dispatcher.filters.state import State, StatesGroup


class Anketa(StatesGroup):
    language = State()
    main = State()
    center = State()
    course = State()
    other = State()
    full_name = State()
    tel = State()
    jins = State()
    age = State()
    choice = State()
    send = State()
    confirm = State()

    