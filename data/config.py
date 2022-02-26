from environs import Env
from pathlib import Path
# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o‘qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro‘yxati
GROUP = env.list("GROUP")
IP = env.str("ip")  # Xosting ip manzili

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_HOST = env.str("DB_HOST")
DB_NAME = env.str("DB_NAME")


I18N_DOMAIN = 'Info_bot'
BASE_DIR = Path(__file__).parent.parent
LOCALES_DIR = BASE_DIR / 'locales'