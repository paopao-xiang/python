# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 19:47
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : guess_number.py
#猜大小
# 生成随机整数，从1-9取出来。然后输入一个数字，来猜，
# 如果大于，则打印bigger。
# 小了，则打印less。如果相等，则打印equal

# #要把你们的眼光 放到课堂之外？
# import random
# num=random.randint(1,9)
# #print(num)#随机数可以打印出来 查看大小
# my_num=int(input('请输入你心目中的整数:'))
#
# #猜大小
# if my_num>num:
#     print('没有猜中，太大了！')
# elif my_num<num:
#     print('没有猜中，太小了！')
# else:
#     print('猜中了，两者相等')
#
# from openpyxl import load_workbook
# wb=load_workbook("testcase.xlsx")
# sheet=wb["Sheet1"]
# l=[]
# for i in range(1,sheet.max_row+1):
#     l1=[]
#     for j in range(1,sheet.max_column+1):
#         resp=sheet.cell(i,j).value
#         l1.append(resp)
#     l.append(l1)
#     wb.close()
# print(l)


l= ["A","B","C",1,2,3]
l1=["B","C","D",2,3,4]
l2=["B","C","D",2,3,4]
L=[]#交集
L1=[]#差集
L2=[]#并集
L2.extend(l)#将l赋值给并集L2
for s in l:
    for m in l1:
        if s==m:
            L.append(s)#如果相等就加入到交集中
            l1.remove(m)#剔除l1中与l相交的值
        else:
            if m not in L1 and m not in l:
                L1.append(m)
L1.extend(l1)
L2.extend(l1)#并集中l加入被剔除相交值的l1,就是两个列表并集
# L1.extend(L2)#并集中去掉交集值就是差集
# for a in L2:
#     for b in L:
#         if a==b:
#             L1.remove(a)
print("并集{}，交集{}，差集{}".format(L2,L,L1))


l= ["A","B","C",1,2,3]
l1=["B","C","D",2,3,4]
jiao=[]
bing=[]
cha=[]
for i in l:
    if i not in l1:
        cha.append(i)
    else:
        jiao.append(i)
for s in l1:
    if s not in l:
        cha.append(s)
bing.extend(cha)
bing.extend(jiao)
print("并集{}，交集{}，差集{}".format(bing,jiao,cha))