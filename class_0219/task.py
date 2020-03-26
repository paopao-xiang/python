# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 20:05
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : task.py

# 利用input函数（自行去拓展该函数的用法），
# 获取一个日期，日期格式如下所示：20190216，
# 然后针对输入的这个日期，进行一些处理后，
# 输出：2019年2月16日   这个字符串到控制台

# print()
# input()---》input函数获取到的数据类型 是字符串类型

time=input('请输入日期：')#2019年2月16日
#切片 格式化输出 20190219 20191119
# print("{}年{}月{}日".format(time[:4],time[5],time[6:]))
print("{}年{}月{}日".format(time[:4],time[4:6],time[6:]))#if 条件
#try..except..异常优秀