# coding = utf-8
import base64
from django.utils.http import urlquote

def read_image(image_path):
    try:
        with open(image_path, 'rb') as f:
            image = f.read()
        return image
    except Exception as e:
        raise e

def encode_image(image):
    base64_image = base64.b64encode(image)
    return base64_image
