import os
from enum import Enum
from app.utils.response import success_response_builder, failure_response_builder 
from app.utils.bothandler import BotHandler
from app.config.config import Config
from werkzeug.utils import secure_filename

class FileType(Enum):
    IMAGE = "IMAGE"
    DOCUMENT = "DOCUMENT"
    NONE = "NONE"

# UPLOAD_FOLDER = Config().UPLOAD 

ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'svg'}
ALLOWED_DOCUMENT_EXTENSIONS = {'pdf', 'doc', 'txt', 'docx', 'ppt', 'pptx'}

MAX_IMAGE_SIZE = 10000000;
MAX_DOCUMENT_SIZE = 50000000;

def allowed_file_type(filename):
    if not filename:
        return FileType.NONE
    extension = filename.rsplit('.', 1)[1].lower()
    if extension in ALLOWED_IMAGE_EXTENSIONS:
        return FileType.IMAGE
    elif extension in ALLOWED_DOCUMENT_EXTENSIONS:
        return FileType.DOCUMENT
    return FileType.NONE

def is_valid_img_size(content_length):
    if content_length > MAX_IMAGE_SIZE:
        return False
    return True

def is_valid_doc_size(content_length):
    if content_length > MAX_IMAGE_SIZE:
        return False
    return True

def process_request(file,file_size,token):
    file_type = allowed_file_type(file.filename);
    response = failure_response_builder(403, "Invalid file type")
    if file_type == FileType.NONE:
        return response
    
    elif file_type == FileType.IMAGE:
        if (file_size > MAX_IMAGE_SIZE):
            return failure_response_builder(413, "Image cannot excedd 10 MB")
        try:
            response = BotHandler().send_photo(token, file)
        except (BadRequest, Unauthorized, TelegramError) as e:
            response = failure_response_builder(500, f"Failed to send photo: {e}")

    elif file_type == FileType.DOCUMENT:
        if (file_size > MAX_DOCUMENT_SIZE):
            return failure_response_builder(413, "Image cannot exceed 50 MB")
        try:
            response = BotHandler().send_document(token, file)
        except (BadRequest, Unauthorized, TelegramError) as e:
            response = failure_response_builder(500, f"Failed to send photo: {e}")
    return response
