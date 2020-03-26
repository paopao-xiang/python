# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 21:10
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : if条件语句.py
#1：非常简单的条件语句
#if 条件:#if 后面的条件运算结果是布尔值  逻辑/比较/成员  各类数据类型
    #if代码  只有当if后面的条件成立（True）的时候才会执行if的代码块

#python 非零非空数据 True 1   ; 零/空数据 False
# d={}
# if d:
#     print('华华老师今年18岁！')


# #2：第二个条件语句：if..else..
# age=55
#
# if age>=18:
#     print('恭喜你成年了！')
#     if age>40:
#         print('你是一个中年人')
#     else:
#         print('你是一个青少年')
# else:
#     print('恭喜你，你还是一个小学生！')

#3：多重判断语句 ：if..elif...elif...else
#if 必须要有的  else elif 可有可无
#但是如果一定有elif以及else
#1)elif 的个数不限定  2）他的分支顺序一定是 if...elif...else,else一定是放在最后的

score=int(input('请输入整数的成绩'))
if score>90:
    print('great!!!')
elif score>80:
    print('good!!!')
elif score>70:
    print('well')
elif score>=60:
    print('pass')
elif score<60:
    print('不及格')