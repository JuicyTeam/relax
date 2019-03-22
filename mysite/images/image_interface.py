# coding = utf-8
import requests
import json
import urllib
from images.config import *

class ImageClassic():
    def __init__(self):
        '''
        获取认证token
        '''
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        response = requests.post(authen_url, headers)
        result = response.text
        result = json.loads(result)
        self.session_key = result.get('session_key')
        self.session_secret = result.get('session_secret')
        self.access_token = result.get('access_token')
        self.scope = result.get('scope')


    def flower_info(self, data):
        try:
            data = urllib.parse.urlencode(data)
            url = plant_class + self.access_token
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post(url, headers=headers, data=data)
            result = response.text
            result = json.loads(result)
            return result
        except Exception as e:
            raise e
