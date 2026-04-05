import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8564398983:AAHuuntq53gVgwIxQash63fatvHq-27BJTc")
    API_ID = int(os.environ.get("API_ID", "20807000"))
    API_HASH = os.environ.get("API_HASH", "cde2366a7c61e23f4cb44618cbe6cf70")
    AUTH_USER = os.environ.get('AUTH_USERS', '890749443, 5938871512').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "〖ᴷⁱⁿᴳ Ⱥʂʂìցղҽɾ 🔰❌️🔰♡▪︎•Å𝑁𝐈𐌑À𝐿•▪︎♡ ⱽᵉʳⁱᶠⁱᵉᵈ"#Here You Can Change with Your Name  or any custom name or title you prefer
