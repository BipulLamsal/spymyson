import os
from flask import request, Blueprint, render_template
from app.utils.filehandler import allowed_file_type,FileType,process_request  
from app.utils.response import failure_response_builder, success_response_builder


bot = Blueprint("bot", __name__)
initial = Blueprint('initial',__name__)
@initial.route('/')
def index():
    return render_template('index.html')

@bot.route('/', methods=["GET"])
def say_hello_world():
    return success_response_builder(200, "Hello world")


'''
the send method requires to have both
file and auhorization token which is 
obtained via the bot
'''
@bot.route("/send", methods=["POST"])
def upload_file():
    if not request.headers.get('Authorization'):
        return failure_response_builder(400, "No token provided")

    token = request.headers.get('Authorization')
    text = request.form.get("message")

    if 'file' not in request.files and not text:
        return failure_response_builder(400, "No image or message provided")

    if text:
        return BotHandler().send_message(token, text)

    file = request.files["file"]
    return process_request(file, request.content_length, token)


