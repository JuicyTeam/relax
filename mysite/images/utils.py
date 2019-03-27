# coding = utf-8
import base64
from django.utils.http import urlquote
from images.models import ImagesClass

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

def save_info(data):
    try:
        ImagesClass.objects.create(user=data.get('user'), gender=data.get('gender'),
                                   location=data.get('location'), imagepath=data.get('imagepath'),
                                   label=data.get('label'))
    except Exception as e:
        raise e
