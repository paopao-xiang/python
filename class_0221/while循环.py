# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 20:09
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : while循环.py

#while循环&for循环&嵌套循环
#函数语法&内置函数

#什么时候才会用到循环：重复的操作
#while循环
#语法：while 条件表达式：#条件表达式-->同if--->本质：布尔值 逻辑 比较 成员 各种数据类型
         #循环体

# #有一个风险：容易进入死循环
#如果要避免进入死循环  怎么办？
#1）while后面不要是永真式，那么while后面的表达式的值 是要变化的
# a=0#设定一个变量 a 初始值为0
# while a<5:
#     a+=1
#     print('Python是世界上最优美的语言！')

#2）while后面是永真式 那么可以用break continue组合的方法来防止进入死循环
#break 终止循环  continue 结束本轮循环 继续下一轮循环
a=0#设定一个变量 a 初始值为0
while 1:
    if a<3:#a=0 1 2
        print('Python是世界上最优美的语言！')
        a+=1
        continue
    # else:
    #     # break

#Python 里面的：
#False 与False等价的还有数字0 空字典 空列表 空字符串  空元组
#True  与True等价的还有数字1 其他非0数字 非空列表 非空字典 非空字符串 非空元组

#有一个空列表 s=[] 我们利用while循环 循环5次 每次询问一个人的名字
# 并且把名字加到列表里面去 利用while来完成这个表达
#温馨提示 列表增加元素 可以用这个方法 列表名.append(值)

# s=[]
# a=0
# while True:
#     if a<5:
#         sir=input('请输入你的名字：')
#         s.append(sir)
#         a+=1
#         continue
#     else:
#         break
# print(s)

# s=[]
# a=0
# while a<5:
#         sir=input('请输入你的名字：')
#         s.append(sir)
#         a+=1
# print(s)

# s=[]
# while len(s)<5:
#         sir=input('请输入你的名字：')
#         s.append(sir)
# print(s)

# # 列表名.append(值)
# s=[]
# s.append(8)
# s.append(9)
# s.append(10)
# print(s)