import os
from flask import request, Blueprint
from app.utils.filehandler import allowed_file_type,FileType,process_request  
from app.utils.response import failure_response_builder, success_response_builder


bot = Blueprint("bot", __name__)

@bot.route('/', methods=["GET"])
def say_hello_world():
    return success_response_builder(200, "Hello world")


'''
the send method requires to have both
file and auhorization token which is 
obtained via the bot
'''
@bot.route("/send",methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return failure_response_builder(400,"No image provided")

    if not request.headers.get('Authorization'):
        return failure_response_builder(400,"No token provided")

    file = request.files["file"]
    token = request.headers.get('Authorization')
    return process_request(file,token)

