import pytest
import requests
import json
import logging
import urllib3
import jsonpath
from hamcrest import *
import logging
# 解决“Unverified HTTPS request is being made to host '127.0.0.1'”问题
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class TestRequests(object):
    def setup_method(self):
        # logging.basicConfig(filename='requestsfile\req.log', level=logging.DEBUG)
        self.filename = 'req.log'
        self.logger = logging.getLogger("requests")
        self.logger.setLevel(logging.DEBUG)
        # 格式设置
        fmt = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
        # 文件方式处理
        fh = logging.FileHandler('./requestsfile/'+self.filename)
        # fh=logging.StreamHandler(filename)
        fh.setFormatter(fmt)
        # fh.setLevel(logging.DEBUG)
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
        # logging.info(json.dumps(r.json(), indent=2))
        self.logger.info(r)
        self.logger.info(r.text)
        self.logger.info(json.dumps(r.json(), indent=2))

    def test_post(self):
        self.url = "https://testerhome.com/api/v3/topics.json?limit=2"
        r = requests.post(self.url, data={'a': "1", 'b': 'string content'},  # post方法是data
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
                         params={"a": "params_a", "b": "params_b"},
                         proxies={"http": 'http://127.0.0.1:8888',
                                  "https": 'http://127.0.0.1:8888'},
                         cookies={"a": "1", "b": "string content"},
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
        assert r.json()['data'][0]['guests'][0]['id'] == 956
        assert r.json()['data'][1]['duration'] == 5417
        self.logger.info(jsonpath.jsonpath(r.json(), '$.data[0].guests[0].id'))
        self.logger.info(jsonpath.jsonpath(r.json(), "$.data[*].guests..[?(@.id==956)].name"))

    def test_hamcrest(self):
        assert_that(0.1*0.1, close_to(0.01, 0.00000000000000002), 'not close to')
        # 列表包含一个元素
        assert_that(["a", "b", "c"], has_item('d'), reason='not contains')
        # 列表包含多个元素
        assert_that(["a", "b", "c"], has_items('c','b'), reason='not contains')
        # 任何一个匹配，就返回成功
        assert_that(['a', 'b', 'c'], any_of(
            has_items('d', 'a'), has_items('a', 'b')))
        # 所有都匹配，才返回成功
        assert_that(['a', 'b', 'c'], all_of(
            has_items('c', 'a'), has_items('a', 'b')), reason='not all contains')
        # equal_to
        assert_that(10, equal_to(11), reason='two numbers not equal')

    def teardown_method(self):
        pass


