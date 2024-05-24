from flask import Flask
from app.config.config import Config

config = Config().production_config

def create_app():
    application = Flask(__name__)
    from app.routes import bot
    from app.routes import initial
    from app.webhook.webhook import hook 
    application.register_blueprint(initial)
    application.register_blueprint(bot, url_prefix = "/api")
    application.register_blueprint(hook, url_prefix="/webhook")
    return application

    

