# -*- encoding: utf-8 -*-
'''
@文件:test_httpbin.py
@说明:
@时间:2022/03/20 21:40:17
@作者:hunaifeng
@版本:1.0
'''
import pytest
import requests
import logging
import json


class TestHttpBin(object):
#     def __init__(self):
#         self.url = "http://httpbin.org/"

    def test_gethtttp(self):
        url_get = self.url+"get"
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.get(url_get, params=payload)
        print(r)
        print(json.dumps(r.json(),indent=4))
        
# if __name__ == '__main__':
#     httpbin=TestHttpBin()
#     httpbin.test_gethtttp()
