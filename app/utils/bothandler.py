import telebot
from telebot.apihelper import ApiException
from app.config.config import Config
from app.utils.response import success_response_builder, failure_response_builder
class BotHandler():
    def __init__(self):
        BOT_TOKEN = Config().BOT_TOKEN 
        self.bot = telebot.TeleBot(BOT_TOKEN)
    
    def send_photo(self,chat_id,file_path):
        try:
            with open(file_path, 'rb') as photo:  
                self.bot.send_photo(chat_id, photo)
                return success_response_builder(200,"Sent photo to the telegram account")
        
        except ApiException as e:
            if e.error_code == 400:
                return failure_response_builder(400, f"BadRequest error: {e.result_json['description']} - Invalid chat_id: {chat_id}")
            if e.error_code == 401:
                return failure_response_builder(401, f"Unauthorized error: {e.result_json['description']} - The bot is not authorized to send messages to this chat_id: {chat_id}")
            else:
                return failure_response_builder(500, f"TelegramError: {e.result_json['description']} - An error occurred while sending the photo to chat_id: {chat_id}")
    
    def send_document(self,chat_id,file_path):
        try:
            with open(file_path, 'rb') as document:
                self.bot.send_document(chat_id,document)
                return success_response_builder(200,"Sent document to the telegram account")
        
        except ApiException as e:
            if e.error_code == 400:
                return failure_response_builder(400, f"BadRequest error: {e.result_json['description']} - Invalid chat_id: {chat_id}")
            if e.error_code == 401:
                return failure_response_builder(401, f"Unauthorized error: {e.result_json['description']} - The bot is not authorized to send messages to this chat_id: {chat_id}")
            else:
                return failure_response_builder(500, f"TelegramError: {e.result_json['description']} - An error occurred while sending the photo to chat_id: {chat_id}")
        

