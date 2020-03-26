# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 20:38
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 列表的内置函数.py
#增删改查
# L=[0.02,100,'hello',(1,2,3),['python',0.02]]

#增加：
#1)两个列表相加  两个列表的元素 会合成到一个列表里面
# s=[4,5,6]
# L=L+s
# print(L)
#2）append() 给列表里面增加元素  只能增加最后面,只能一次加一个
# L.append('柠檬班最佳cp:')

#3）insert() 给列表里面增加元素  可以增加在指定位置
# L.insert(0,'柠檬')

#4)extend 拓展列表   效果与+等效
# s=[6,66,666]
# L.extend(s)
# print(L)

#改：
# L=[0.02,100,'hello',(1,2,3),['python',0.02]]
# L[0]='华华'#赋值运算

#删除
# L=[100,'hello',(1,2,3),['python',0.02]]
# del(L)清空整个列表
#删除 pop() 默认删除最后一个元素  指定索引 就删除指定位置的值
# res=L.pop(0)
# print(L)
# print('被删除的元素：',res)
# L.clear()#清空的操作，变成空列表
# L.remove()#删除指定的值，无返回值
# print(L)

#查：利用索引取值 以及切片取值--不记得的同学请自行去复习

#range函数：
# range(m,n,k)#生成指定范围的整数序列
#切片很相似 取头不取尾
#m 索引头  n 索引尾 k步长 k默认值为1
#如果只传一个参数 默认索引头是0 从0开始
res=list(range(0,-2,-1))#
print(res)

# L=[100,'hello',(1,2,3),['python',0.02]]
# # for item in L:
# #     print(item)
#
# for i in range(len(L)-1,-1,-1):#>range(3,-1,-1)-->3 2 1 0
#     print(L[i])
L=[100,'hello',(1,2,3),['python',0.02],'hello']
# res=L.count(100)
# res=L.copy()#深copy 浅copy
# res=L.index('hello',2)
# L.reverse()#列表翻转

# 经典冒泡算法： 利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序： 冒泡排序：小的排前面，大的排后面。
# a=[1,7,4,89,34,2]
# a.sort(reverse=True)
# print(a)