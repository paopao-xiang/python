# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 20:18
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_requests.py
#requests
#安装：pip install requests
#作用是什么？发送http请求 你常见的有哪几种？？ get post
#为什么要学习它？http协议的接口

#request:客户端---服务器的一个请求，包含：请求头 请求方法、请求地址 请求参数 http协议版本
#response：服务器---客户端的一个请求的响应，包含：响应头 响应报文 状态码
#常见的状态码：200 404：url地址不对或者是找不到
#500 502：网关错误
#304：静态资源  png jpeg gif css js

import requests
# url='http://www.lemfix.com/topics/198'#请求地址

#发送一个get请求
# resp=requests.get(url)#响应结果消息实体  包含：响应头 响应报文 状态码
# print('响应报文',resp.text)#响应报文
# print('响应头',resp.headers)#响应头
# print('状态码',resp.status_code)#状态码

#发送一个post请求
# resp=requests.post(url)#响应结果消息实体  包含：响应头 响应报文 状态码
# print('响应报文:',resp.text)#响应报文
# print('响应头:',resp.headers)#响应头
# print('状态码:',resp.status_code)#状态码


#作业安排：
#写一个类：里面有一个函数 http_request 能够完成get请求或post请求，要求有返回值
#每个请求要求有请求参数
# class Request():
#     def http_request(self,url,method):
#         if method.lower()=="get":
#             resp=requests.get(url)
#         else:
#             resp=requests.post(url)
#         return resp.status_code,resp.text,resp.headers
# t=Request()
# s=t.http_request("http://jxcloud.uat.jxintell.com","get")
# print(s)

#登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
import json
from configparser import ConfigParser
class Login():
    def http_request(self,url,method,params):
        if method.lower()=="get":
            resp=requests.get(url,params=params)
        else:
            if type(params)==dict :
                resp=requests.post(url,json=params )
            else:
                resp=requests.post(url,data=params )
        return resp
if __name__ == '__main__':
    t=Login()
    c=ConfigParser()
    c.read("url_demo.conf",encoding="utf-8")
    method="post"
    s=t.http_request(c.get("url","url_2"),method,json.loads(c.get("params","params_1")))
    print(s.status_code)
    print(s.text)
    print(s.json()["msg"])
#



