# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 9:36
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 格式化输出.py

#格式化输出
# name='丫头'
# age=22#int str float
# sex='女'#0 女生 1 男生 注解
# salary='9000'#str int float
# hobby='游泳'
# height=170.45#浮点数

#简单的输出
#+ 字符串之间的拼接  + 只能针对同类型的数据  str(数字)--->字符串类型
# print('Python15期有一个学生的名字叫：'+name+',她的薪资是：'+salary+',她今年'+str(age)+'岁')
# print('Python15期有一个学生的名字叫：'+name+',她的薪资是：'+salary+',她今年',age,'岁')

# print(1,2,3,4)#内置函数 *args-->arguments-->参数们  可以输入任意多个参数 ,用逗号隔开

# f(x)=x+4
# f(1)=5
# f(2)=6

#第一种格式化输出 %s %d %f 占坑 按顺序赋值 %s是万能的 啥都可以接  数字类型 %d %f %s  其他类型 必须用%s
# print('Python15期有一个学生的名字叫:%s,她的薪资是：%s,她今年%f岁,她的身高是：%s'%(name,salary,age,height))

name='丫头'
age=22#int str float
sex='女'#0 女生 1 男生 注解
salary='9000'#str int float
hobby='游泳'
height=170.45#浮点数

#第二种格式化输出 {} format  推荐使用  1)不标序号  按顺序赋值/2)标了序号  按序号给值
# print('Python15期有一个学生的名字叫:{},她的薪资是：{},她今年{}岁,她的身高是：{}'.format(name,salary,age,height))

print('''-----student's info--------
    Python15期有一个学生的名字叫:%s
    她的薪资是：%s
    她今年%s岁
    她的身高是：%s'''%(name,salary,age,height))