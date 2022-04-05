# -*- encoding: utf-8 -*-
'''
@文件:test_json.py
@说明:
@时间:2022/04/04 16:47:01
@作者:Lohas
@版本:1.0
'''

import json
import jsonpath

obj = json.load(open('./requestsfile/test.json','r',encoding='utf-8'))

# 输出：['睿郡资产']
name=jsonpath.jsonpath(obj, '$.data[*].guests..[?(@.id==956)].name')
print("name:%s\n" %id)

# id=jsonpath.jsonpath(obj, '$.data[*].guests..id')
# print("id:%s\n" %id)

