# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 9:48
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 函数的参数类型.py

#参数类型：位置参数 默认参数 动态参数 *args 关键字参数**kwargs

def add(x,y):#形参/位置参数
    '''加法，求任何两个值的和，并返回计算结果'''
    print('x的值是',x)
    print('y的值是',y)
    return x+y

# 位置参数
# res=add(9,1)#调用函数的时候传的参数--实参--默认按顺序赋值的
# res=add(x=9,y=6)#指定赋值  不关注顺序了 指定是什么就是什么
# print('add函数计算的结果是：{}'.format(res))

# 默认参数：在定义函数的时候，给某个参数设置默认值
#位置参数必须在默认参数之前
#有几个位置参数 就必须要传几个参数
# def add(x=10,y=9):#
#     '''加法，求任何两个值的和，并返回计算结果
#     :arg x 第一个参数
#     :arg y 第二个参数'''
#     print('x的值是',x)
#     print('y的值是',y)
#     return x+y
#
# res=add(y=6)
# print('add函数计算的结果是：{}'.format(res))

#动态参数 *args  arguments 复数 指定多个 --不定长参数
def add(*args):#参数传递到函数内部 会把所有的参数存储到一个元组
    print('数据类型：',type(args))
    print(args)
    sum=0#求和的初始值
    for item in args:
        sum+=item
    print('求和的结果是：',sum)
#
# add(5,6,9,10,11,1)


# 关键字参数**kwargs key word arguments
#参数传递进去后变成了一个字典 kwargs 指明key value
# def student_info(**kwargs):
#     print(kwargs)
#
# student_info(name='牛牛',age=28,money=100)
# student_info('caryon',22)---错误的示范

# def add(*args):
#     print(*args)
#
# add(1,2,3,4)


# f(x)=x+4
# f(1)=5
# f(5)=9