__author__ = 'xsj'
import os
#方式一：import 模块名（不需要.py这个后缀）  导入模块，
# 在Python  lib（里面有Python自带的模块）文件下可以直接接模块名导入
# 除了顶级项目名外，一层一层定位需要的模块
# import class_0223.函数的参数类型
# class_0223.函数的参数类型.add(5,6,9,10,11,1)

#方式二：import 模块名 as  newname（不需要.py这个后缀）  导入模块，
# 在Python  lib（里面有Python自带的模块）文件下可以直接接模块名导入
# 除了顶级项目名外，一层一层定位需要的模块
# import class_0223.函数的参数类型 as x
# x.add(5,6,9,10,11,1)

#方式三：from.....import.....(import后面具体到模块名，函数名，类名）从哪个文件导入什么模块或类或函数
# from class_0223.函数的参数类型 import add  #add(5,6,9,10,11,1)
# from class_0223 import 函数的参数类型     #函数的参数类型.add(5,6,9,10,11,1)
# from class_0223.函数的参数类型 import*    #add(5,6,9,10,11,1)
# add(5,6,9,10,11,1)

#方式三：from.....import....as  newname.(import后面具体到模块名，函数名，类名）从哪个文件导入什么模块或类或函数
# from class_0223.函数的参数类型 import add as x  #x(5,6,9,10,11,1)
# from class_0223 import 函数的参数类型 as  x    #x.add(5,6,9,10,11,1)
# x.add(5,6,9,10,11,1)