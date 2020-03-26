# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 20:51
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : for循环.py

#遍历循环：
# L=['angelbaby','cindy','sunny','Jolin']

#for循环的语法：
# for 变量名 in 数据:
    #循环体

# for item in L:#依次按顺序访问L里面的元素  有几个元素就会循环几次
#     #在访问L里面的每一个元素的同时  会赋值给item
#     print('Python大法好，信Python得永生！')
#     print('item的值:{}'.format(item))#格式化输出

#到底用哪个循环？如果你确定循环次数的话  就用for
# 如果你不确定循环次数，而是要达到某个限制的条件后才停止 用while

#有一个空列表 s=[] 我们利用for循环 循环5次 每次询问一个人的名字
# 并且把名字加到列表里面去 利用for来完成这个表达
#温馨提示 列表增加元素 可以用这个方法 列表名.append(值)
#in 后面的数据类型可以是什么呢？ 字符串 字典  元组  列表
s=['1','2','3','4','5']
for item in range(1,5):
   print(s[item])

