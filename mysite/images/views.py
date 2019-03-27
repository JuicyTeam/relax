# coding = utf-8
from django.views.generic import View
from django.http import JsonResponse
import requests
import json
from images.image_interface import ImageClassic
from images.utils import *
from mysite.settings import BASE_DIR
# Create your views here.

class Imageclass(View):
    '''
    获取植物分类，post接口
    :param request:user, gender, location,image
    :return:
    '''
    def post(self, request):

        try:
            save_data = {}
            data = request.POST
            save_data['user'] = data.get('user')
            save_data['gender'] = data.get('gender')
            save_data['location'] = data.get('location')
            image = request.FILES.get('image')
            base64_image = encode_image(image.read())
            data = {
                "image" : base64_image,
                "top_num":5,
                "baike_num":10
            }
            ic = ImageClassic()
            result = ic.flower_info(data)
            filepath = './static/images/' + image.name
            with open(filepath, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            save_data['imagepath'] = filepath
            save_data['label'] = json.dumps(result)
            save_info(save_data)
            response = {"status": {"status_code": 200, "msg": "ok"}, "data": result}
        except Exception as e:
            response = {"status": {"status_code": 500, "msg": str(e)}}
        return JsonResponse(response)
