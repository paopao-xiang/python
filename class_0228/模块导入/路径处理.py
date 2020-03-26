__author__ = 'xsj'
# 相对路径
# 绝对路径（全面的路径）C:\Python34\python.exe C:/Users/xsj/PycharmProjects/Python_15/class_0228/路径处理.py
# open()#打开一个文件,根据相对路径来找文件../会往上翻一级
# file=open("Python_15")
# file=open("../../Python_15")
# file=open("C:\\Users\\xsj\PycharmProjects\Python_15\class_0228\Python_15")
# print(file.read())
#\t  \n  \r ---转义  r   R  或者是加\class_0228/Python_15

import os #导入os模块
# path_1=os.getcwd()#获取当前路径，不会具体到模块
# path_2=os.path.realpath(__file__) #__file__指当前当前文件本身，给的值不确定路径是否正确
# path_3=os.path.basename(__file__)#返回文件名
# print("path_1",path_1)
# print("path_2",path_2)
# print("path_3",path_3)
path_2=os.path.realpath(__file__) #__file__指当前当前文件本身，给的值不确定路径是否正确
print("path_2",path_2)

#可以对路径进行切割os.path.split(path)    path是路径字符串
res=os.path.split(path_2)#对路径进行处理，返回是一个元祖
print("res",res)
# os.mkdir(path)  path 是路径字符串，新建一个文件夹
# os.mkdir(res[0]+"\python5")

new_path=os.path.join(res[0],"python15","python16")#拼接路径,只能一级一级的建立
os.mkdir(new_path)