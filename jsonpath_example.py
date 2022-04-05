# -*- encoding: utf-8 -*-
'''
@文件:jsonpath_example.py
@说明:
@时间:2022/03/30 22:25:44
@作者:Lohas
@版本:1.0
'''
import json
import jsonpath

obj = json.load(open('./requestsfile/jsonpath.json','r',encoding='utf-8'))

# 获取所有书的作者
authors=jsonpath.jsonpath(obj, '$.store.book[*].author')
print("authors:%s\n" %authors)

# 获取所有的作者
authors=jsonpath.jsonpath(obj, '$..author')
print("authors:%s\n" %authors)

# store的所有元素。所有的book和bicycle
store_element=jsonpath.jsonpath(obj, '$.store.*')
print("store_element:%s\n" %store_element)

# 获取store里面的所有东西的price
prices=jsonpath.jsonpath(obj, '$.store.*..price')
print("prices:%s\n" %prices)

# 获取第三本书，也可以写成$.store.book[:2]或者$.store.book[0,1]
thirdbook=jsonpath.jsonpath(obj, '$.store.book[2]')
print("thirdbook:%s\n" %thirdbook)

# 获取最后一本书,也可以写成$.store.book[-1:]
lastbook1=jsonpath.jsonpath(obj, "$.store.book[(@.length-1)]")
lastbook2=jsonpath.jsonpath(obj, "$.store.book[-1:]")
print("lastbook1:%s\n" %lastbook1)
print("lastbook2:%s\n" %lastbook2)

# 获取前面的两本书
book_1_2=jsonpath.jsonpath(obj, '$..book[0,1]')
print("book_1_2:%s\n" %book_1_2)

#  过滤出所有的包含isbn的书。
isbn=jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print("isbn:%s\n" %isbn)

# 过滤出价格低于30的书。
under10=jsonpath.jsonpath(obj, '$..book[?(@.price<30)]')
print("under10:%s\n" %under10)