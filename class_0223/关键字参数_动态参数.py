# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 10:33
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 关键字参数_动态参数.py

def add(*args):#定义---表示你可以传递任意多个参数
    print('args的值：',args)
    # print('args的类型是',type(args))

# t=[1,2],[3,4,5]
# add(t)
# add(*t)#如果你是在调用的时候--解包--脱外套--脱一层  只能加一个*

def student_info(**kwargs):
    print(kwargs)

d={'age':18,'name':'promise'}
# student_info(age=18,name='sadness')
student_info(**d)
print(d)
