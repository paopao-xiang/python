# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 10:57
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 内置函数.py
# print(1,2,3,sep='@@',end='\n\n')
# type()
# len()
# int()
# str()
# float()
# format()
# input()

#字符串
# s='pytHonyy'
# res=s.capitalize()
# res=s.count('y',2,8)#返回次数
# res=s.find('x',2,8)#找字符串第一次出现的索引位置  如果没找到就返回-1
# res=s.index('z')#寻找子字符串 并返回索引值 没找到报错
# res=s.islower()#判断字符串是否是小写，如果都是小写 返回True 否则返回 False
# res=s.isupper()#判断字符串是否是大写，如果都是大写 返回True 否则返回 False
# res=s.upper()#变成大写
# res=res.isupper()
# res=s.lower()#变成小写

# s=input('请输入一个数据')
# res=s.isdigit()#判断是否都是纯数字
# res=s.isdecimal()#判断是否是十进制的数据

s='pytHonyy'
res='@'.join(s)#拼接
print(res)

#