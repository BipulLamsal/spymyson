import os
from app.config.dev_config import DevConfig
from app.config.production_config import ProductionConfig
from dotenv import load_dotenv
load_dotenv()
class Config:
    def __init__(self):
        self.dev_config = DevConfig()
        self.production_config = ProductionConfig()
        self.UPLOAD = 'tmp/uploads/'
        self.BOT_TOKEN = os.getenv('BOT_TOKEN')

