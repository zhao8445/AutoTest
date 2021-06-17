# encoding:utf-8

import requests
import base64

from config.settings import params

APP_ID = '24388465'
API_KEY = '4bWzGcaRPGCVIz0T0gxSSDSY'
SECRET_KEY = 'nin0rRXUGwUCu59OMcKZBdvPFXE9jTag'
PROJECT_ROOT_PATH = params["project_root_path"]

def get_token():
    """
    获取百度云access_token
    """
    access_token = ""
    host = 'https://aip.baidubce.com/oauth/2.0/token'

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    params = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": SECRET_KEY
    }
    response = requests.get(url=host, params=params)
    if response:
        response = response.json()
        access_token = response["access_token"]

    return access_token

def img_ocr(img_path):
    """
    百度OCR文字识别
    """
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

    # 二进制方式打开图片文件
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        response = response.json()
        words = response["words_result"][0]["words"]
        print(response)
        print(words)
        f.close()
        return words

    f.close()
    return ""
