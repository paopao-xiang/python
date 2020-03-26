# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function：  数据类型的转换 str-->dict
"""
import json

# 正常的json格式
# {"key":[]}
params = '{"status":1,"code":"10001","data":null,"msg":"登录成功"}'  # 返回   这种只有json可转为字典
p = '{"mobilephone":"15810447878","pwd":""}'  # 请求入参，这种json和eval都可转为字典
s='{"mobilephone":"15810447878","pwd":None}'   # 请求入参，这种只有eval可转为字典
d = eval(p)
print(type(d),d)
# json.loads()
# d = eval(params)  # 根据的python的数据类型来做转换
# print(d['status'])

d1 = json.loads(p)
print(type(d1), d1)

#总结，字符串形式的字典两种方式都可以转换，但是json格式只能由json.loads转换,包含json不认识的json无法转换，包含python不认识的eval无法转换