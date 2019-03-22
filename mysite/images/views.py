# coding = utf-8
from django.http import JsonResponse
import requests
import json
from images.image_interface import ImageClassic
from images.utils import *
# Create your views here.

def imageclass(request):
    '''
    获取植物分类，post接口
    :param request:
    :return:
    '''
    try:
        #data = request.body
        #data = json.loads(data)
        #image = data.get('image')

        image_path = './images/11.jpg'
        image = read_image(image_path)
        base64_image = encode_image(image)
        data = {
            "image" : base64_image,
            "top_num":5,
            "baike_num":10
        }
        ic = ImageClassic()
        result = ic.flower_info(data)
        response = {"status": {"status_code": 200, "msg": "ok"}, "data": result}
    except Exception as e:
        response = {"status": {"status_code": 500, "msg": str(e)}}
    return JsonResponse(response)
