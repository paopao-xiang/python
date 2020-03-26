# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 20:14
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 运算符.py
#1:算术运算符：+ - * / % //
# a=10
# b=3
# print(a%b)
# a=0.1
# b=0.3
# c=0.2
# print(round(a+b-c+a,1))#python 动态语言 精确度不定
# round(目标数字,精确的小数位数)  如果你要精确你的浮点数运算值
#判断奇数偶数  就会用到% x%2==0

#赋值运算符 = += -=
# x=3
# x+=2#等同于 x=x+2
# x-=4#等同于x=x-4
# print(x)

#比较运算符 == 、!=、 >、 >= 、< 、<=
#运算结果是 布尔值 True False
# x='get'
# y='GET'
# print(x==y)#字符串的字母是区分大小写

#逻辑运算符  not>and>or
#运算结果是 布尔值 True False
# a=5
# b=0
# print(a>5 and not b==0)
#and 两边为真才为真  真真为真
#or 只要有一边为真就为真  假假为假
# and 一假则假  or  一真则真
# and 真真为真  or 假假为假

#成员运算符 in not in   字符串 元组 列表 字典  可迭代数据类型 数据集
#运算结果是 布尔值 True False
# s=('python',9,0.33)
# print(9 in s)

# d={'age':20,"name":'七月'}#默认判断的时候  拿到的是字典的key
# print(20 in d.values())
#
# print(d.values())
# print(d.keys())

a=0
b=10
#非空非零数据 True  #空数据 0 False
print(a and b)