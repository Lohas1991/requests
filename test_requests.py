import pytest
import requests
import json
import logging
import urllib3
import jsonpath
from hamcrest import *
# 解决“Unverified HTTPS request is being made to host '127.0.0.1'”问题
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class TestRequests(object):
    def __init__(self, filename):
        self.logger = logging.getLogger("requests")
        self.logger.setLevel(logging.DEBUG)
        # 格式设置
        fmt = logging.Formatter(
            "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
        # logging.basicConfig(filename="req.log")
        # 文件方式处理
        fh = logging.FileHandler(filename)
        # fh=logging.StreamHandler(filename)
        fh.setFormatter(fmt)
        fh.setLevel(logging.DEBUG)
        self.logger.addHandler(fh)

    def test_get(self):
        self.url = "https://testerhome.com/api/v3/topics.json?limit=2"
        r = requests.get(self.url,
                         # get方法是params
                         params={"a": 1, "b": "string content"},
                         proxies={"http": 'http://127.0.0.1:8888',
                                  "https": 'http://127.0.0.1:8888'},
                         verify=False)
        # logging.info(r)
        # logging.info(r.text)
        # logging.info(json.dumps(r.json(),indent=2))
        self.logger.info(r)
        self.logger.info(r.text)
        self.logger.info(json.dumps(r.json(), indent=2))

    def test_post(self):
        self.url = "https://testerhome.com/api/v3/topics.json?limit=2"
        r = requests.post(self.url, data={'a': 1, 'b': 'string content'},  # post方法是data
                          headers={"c": "3", "d": "int"},
                          proxies={"http": 'http://127.0.0.1:8888',
                                   "https": 'http://127.0.0.1:8888'},
                          verify=False)
        self.logger.info(r)
        self.logger.info(r.text)
        self.logger.info(json.dumps(r.json(), indent=2))

    def test_cookies(self):
        self.url = "https://testerhome.com/api/v3/topics.json?limit=2"
        r = requests.get(self.url,
                         params={"a": 1, "b": "string content"},
                         proxies={"http": 'http://127.0.0.1:8888',
                                  "https": 'http://127.0.0.1:8888'},
                         cookies={"a": 1, "b": "string content"},
                         verify=False)
        self.logger.info(r.text)

    def test_xueqiu_quote(self):
        self.url = "https://api.xueqiu.com/query/v1/road_show/history.json?"
        self.params = {"size": "2", "page": "1", "subjectId": "0"}
        self.cookies = {"xq_a_token": "5952fde81e52759f2363e6c14829343972498bf2",
                        "u": "6158723088"}
        self.headers = {"Host": "api.xueqiu.com",
                        "user-agent": "Xueqiu Android 12.18.1"}
        r = requests.get(self.url, params=self.params,
                         headers=self.headers,
                         cookies=self.cookies,
                         verify=False)
        self.logger.info(json.dumps(r.json(), indent=4))
        #assert r.json()['data'][0]['guests'][0]['id'] == 224
        # print(jsonpath.jsonpath(r.json(),'$.data[0].symbol'))
        print(jsonpath.jsonpath(r.json(), '$.data[0].guests[0].id'))
        # print(jsonpath.jsonpath(r.json(),"$.data[0].guests[0][?(@.id=='287')]"))
        assert_that(0.1*0.1, close_to(0.01, 0.000001))

    def test_hamcrest(self):
        assert_that(0.1*0.1, close_to(0.01, 0.00000000000000002))
        assert_that(["a", "b", "c"], has_item('a'))
        assert_that(['a', 'b', 'c'], any_of(
            has_items('d', 'a'), has_items('a', 'b')))
        assert_that(['a', 'b', 'c'], all_of(
            has_items('d', 'a'), has_items('a', 'b')))


if __name__ == '__main__':
    req = TestRequests('./requests/requests.log')
    # req.test_cookies()
    # req.test_get()
    # req.test_post()
    req.test_xueqiu_quote()
    # req.test_hamcrest()
