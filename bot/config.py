import os

class Config:
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "5603145675:AAEdhwnKmHOgh5JaIvXJVchuKoCVZcF8QIQ")
    TELEGRAM_APP_HASH=os.environ["facf91d4e7d4e31fa2974792bb4763c4"]
    TELEGRAM_APP_ID=int(os.environ["16645066"])
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
