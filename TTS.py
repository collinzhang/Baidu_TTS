#encoding: utf8
from aip import AipSpeech
import os
import sys
import json

""" 你的 APPID AK SK """
APP_ID = '5203061'
API_KEY = 'HxPBVGrRw2w20kmXljrPW6rj'
SECRET_KEY = 'FkmLKunqnBTZY8w2t5sGFKXHvKBgu1YX'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

""" 读取文本 """
n =0
print('Start from 1.txt')
while n <=3:
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    n = n + 1
    str(n)
    print(n)
    txt = get_file_content(str(n) + '.txt')
    res =client.synthesis(txt,'zh',1);
    f1=open(str(n) + '.mp3','wb')
    if not isinstance(res,dict):
        with open(str(n) + '.mp3','wb') as f1:
            f1.write(res)
        f1.close()
print('END')
print('结束')



