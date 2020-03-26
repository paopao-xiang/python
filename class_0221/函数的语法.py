# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 21:37
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 函数的语法.py

#函数的定义：为了实现某个功能而写的代码段  如果这个功能是需要重复使用的 提高复用性
#函数的语法：
#def 函数名(参数1，参数2，参数3)：#小写字母 不同的字母或者是数字之间用下划线隔开
     #'''解释文档'''
     #函数体
     #return

#参数类型：位置参数 默认参数 动态参数 *args 关键字参数**kwargs
#参数个数：0到无数个
#函数体
#return 是否有返回值 只会出现在函数里面
#
def say_hello():#定义函数
    print('早上好！！！')
    return {'name':777,"hero":'superman','age':18}

x,y,z=say_hello()
print(x)
print(y)
print(z)
#
# a=b=c=4

# print('66666')#调用函数
# res=say_hello()#函数的调用 函数名())
# print("函数返回的值是:",res)
# #请对say_hello()这个函数的结果 进行遍历
# for item in res:
#     print(item)

#一：
#1：函数里面没有return 它会隐性给你添加一个return None
#2:函数里面有return 但是return后面啥都并没有 等同于 return None
#3:函数里面有return  但是return后面加的是None 最后的结果还是返回None

#二：return后面只有一个值的时候 是什么类型的数据就会返回什么类型的数据
#比如说return后面是整数 那么返回的整数类型  如果是字符串 那么返回的就是字符串类型

#三：如果return后面有多个值的时候  是以元组的类型返回

#四、return表示函数的结束  return后面的代码都不会执行
# def add(a,b,c):
#     res=a+b+c
#     return res
#     print(66666666666)
#
# add(1,2,3)

