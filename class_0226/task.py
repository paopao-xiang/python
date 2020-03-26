# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 21:52
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : task.py

# 2：完成1-10的整数数字相加，并打印最后的结果
# sum=0#初始值 赋值运算
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     sum+=i
# print(sum)

# a=[1,2,3,4,5,6,7,8,9,10]
# sum=a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]
# print(sum)

# sum=0#初始值 赋值运算
# for i in range(11):#range(0,11,1)-->0 1 2 3 4 5 6 7 8 9 10
#     sum+=i
# print(sum)

# 7：有1 2 3 4 这四个数字，能组成多少个互不相同且无重复数字的三位数？分别是什么？abc a!=b!=c
#a b c
# count=0
# L=[]
# for a in [1,2,3,4]:
#     for b in [1,2,3,4]:
#         for c in [1,2,3,4]:
#             if a!=b and b!=c and a!=c:
#                 count+=1#符合条件的情况下 count+1
#                 L.append(a*100+b*10+c)
#                 # print('符合条件的值是：',a*100+b*10+c)
# print(count)
# print(L)


# 6：经典冒泡算法： 利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序：
# 冒泡排序：小的排前面，大的排后面。
#相邻两个数进行比较
a=[1,7,4,89,34,2]
for j in range(len(a)-1):#控制循环次数 n-1次循环
    '''下面的for循环作用是完成每一次相邻两个数据的比较并且完成数值的交换'''
    for i in range(len(a)-1):#0 1 2 3 4 5 索引值
        if a[i]>a[i+1]:#i=0 i+1=1
            a[i],a[i+1]=a[i+1],a[i]
print(a)

a=2
b=4
a,b=b,a#Python支持这样的用法  交换值 赋值运算
print("a:",a)
print("b:",b)

a,b=1,2#连续赋值的用法
