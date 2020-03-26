# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 21:38
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 字典内置函数.py
# d={'name':'lemon','age':22,'score':99.99}

#增删改查

#增加和改 赋值运算
#key 要求数据类型是不可变  唯一不重复 取值方式：字典名[key]
# print(d['name'])
# d['name']='summer'#key是唯一的
# d['sex']='男'
# print(d)
#字典名[key]=value 如果key是已经存在的  那就是修改  如果key是不存在的 那么就是新增

#查 取值 字典名[key]

#删除 pop() 删除键值对
d={'name':'lemon','age':22,'score':99.99}
# d.pop('age')
# d.popitem()#随机删除
# d.clear()#清空  --->空字典

# res=d.copy()#复制字典
# res=d.items()#dict_items([('age', 22), ('score', 99.99), ('name', 'lemon')])
# res=d.keys()#dict_keys(['name', 'score', 'age'])
# res=d.values()#dict_values([22, 'lemon', 99.99])

res=d.get('name')#根据key取值 get里面传递的参数 是key 字典名[key]
print(res)


