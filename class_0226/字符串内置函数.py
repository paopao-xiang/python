# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 20:02
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 字符串内置函数.py

s='pytHonyy'
# res=s.replace('y','@',2)#替换  第一个参数是目标字符串
# # 第二参数是替换的字符串  第三个参数是替换次数 默认是全部替换
#xmind
# res=s.split('y',3)#切割 第一个参数 根据指定的字符进行切割  第二个参数 切割次数 默认-1是全部切割
# res=s.strip('@')#默认去除头和尾的空格  也可以去掉你指定的字符
# print(len(s))#14
# print(len(res))
# res=s.swapcase()#大小写互换
# print(res)

#课后作业 自行去了解没有讲过的函数  然后配合老师安排的题目 去进行提升
res=s.translate("1")
# s.swapcase()
print(res)
