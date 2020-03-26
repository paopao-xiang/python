# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 14:50
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : football_team.py
#1、一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，
# 询问10次后，输出满足条件的总人数。
#年龄 10<=age<=12  性别：女生  m  f
#询问10个人  问的问题是一样的~~ 我们就可以循环 for循环
#输出符合条件的总人数
# sum=0#符合条件的总人数初始值
# for i in range(10):#0 1 2 3 4 5 6 7 8 9
#     age=int(input('你的年龄是：'))#从控制台获取的数据 是字符串
#     sex=input('你的新别是,f是女 m是男：')
#     if 10<=age<=12  and sex=='f':
#         print('满足条件')
#         sum=sum+1
#     else:
#         print('不满足条件')
# print('满足条件的人数是:',sum)

import unittest
from task_15 import chengfa
import HTMLTestRunnerNew
def main():
    suite=unittest.TestSuite()#创建一个收集对象
# from task_15.chengfa import *
# suite.addTest(Test_HttpRequest_Right())
# suite.addTest(Test_HttpRequest_Right("test_002"))
# suite.addTest(Test_HttpRequest_Wrong("test_003"))
# suite.addTest(Test_HttpRequest_Wrong("test_004"))
    loaders=unittest.TestLoader()
    suite.addTest(loaders.loadTestsFromModule(chengfa))
# suite.addTest(loaders.loadTestsFromModule(Test_HttpRequest_Wrong ))

# from task_15 import  chengfa
# loaders=unittest.TestLoader()
# suite.addTest(loaders.loadTestsFromModule(chengfa))
#     with open("testrequest.html","wb") as file:
    file=open("testrequest.html","wb")
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="测试http请求的测试报告",description="一共写了4条测试用例")
# runner=unittest.TextTestRunner()
    runner.run(suite)
if __name__ == '__main__':
    main()

