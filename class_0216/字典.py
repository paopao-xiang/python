# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 11:02
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 字典.py

#字典 dict--dictionary {}
#1:空字典 d={}
#2:字典 key:value  键值对  不同的键值对之间用逗号隔开
#key:不可变数据类型 int float boolean str tuple  key是唯一的 不能重复的
# key一般都是用字符串 '' ""
#value:可以是任意类型 int  float boolean str tuple list dict
# d={0:'我',
#    0.02:'爱',
#    False:'罗',
#    'age':22,
#    (1,2,3):'tuple'}

d={"name":"柠檬班",
   "class_name":"python15",
   "score":[99,98,88],
   "height":{'sadness':180.89,'小强':183}}
# print(d)
#3:字典取值：字典名[key]  根据key取值
# print(d["score"])
# print(d["height"])
#4：嵌套取值 层级定位
# print(d["height"]["sadness"])
# print(d["score"][0])
#5:字典也是可变无序数据类型
# d['class_name']='柠檬班15期'#重新赋值
# print(d)

# x=1
# x=2
#
# print(x)

#运算符  if条件语句  for循环 while循环 下周主要攻克点

