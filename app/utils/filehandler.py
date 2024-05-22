import os
from enum import Enum
from app.utils.response import success_response_builder, failure_response_builder 
from werkzeug.utils import secure_filename

class FileType(Enum):
    IMAGE = "IMAGE"
    DOCUMENT = "DOCUMENT"
    NONE = "NONE"

UPLOAD_FOLDER = 'app/uploads/'

ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'svg'}
ALLOWED_DOCUMENT_EXTENSIONS = {'pdf', 'doc', 'txt', 'docx', 'ppt', 'pptx'}

MAX_IMAGE_SIZE = 10000;
MAX_DOCUMENT_SIZE = 50000;


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

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

def process_request(file,token):
    file_type = allowed_file_type(file.filename);
    server_file_name = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    if file_type == FileType.NONE:
        return failure_response_builder(400,"Invalid file type")
    elif file_type == FileType.IMAGE: 
        # TODO skip the file greater than MAX_IMAGE_SIZE
        file.save(server_file_name)

    elif file_type == FileType.DOCUMENT:
        # TODO skip the file greater than MAX_DOCUMENT_SIZE
        file.save(server_file_name)
    
    return success_response_builder(400,"booty checkout")

