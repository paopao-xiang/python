# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 10:21
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 元组.py

#元组 tuple ()
#1：空元组  t=()
#2：元组里面只有一个数据 要加一个逗号 才会是元组类型 t=('hello',)
#3:元组里面的元素可以是任意类型 不同的元素之间用逗号隔开
#4:是有下标的  正序/反序编号都支持 取值方式同字符串
t=(1,0.02,'hello',True,(1,2,3,666,'python'))#0 1 2 3 4
#单个取值  元组名[索引值]
# print(t[-1])
#切片 元组名[索引头:索引尾:步长] 步长默认为1
#倒序输出元组里面的每一个元素
# print(t[::-1])
#嵌套取值 元组里面还有元组   层级定位
print(t[-1][3])#取值666
#取值Python里面的y
print(t[-1][-1][1])
#5:元组是有序不可变类型
# t[0]='华华'#TypeError: 'tuple' object does not support item assignment


