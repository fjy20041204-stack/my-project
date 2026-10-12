# #定义
# from os import remove
#
# s=[56,33,33,"hello",True]
# # print(type(s))
# 获取

# print(s[0])#正向索取，从0开始
# print(s[-5])#反向索取，从-1开始

# 修改
# s[0]=66
# print(s)
#
#
# #注意，如果指定索引超出范围，会报错list assignment index out of range
# #
# # s[10]=88
# # print(s)
#
# #删除
# del s[0]
# print(s)
#
# #遍历
# for x in s:
#     print(x)


# 定义列表
# s=[1,2,3,4,45,5,7,9,0]
#
# # 切片操作 s[开始索引：结束索引：步长]
# print(s[0:5:1])
# print(s[0:5:])
# print(s[0:5])
# print(s[0:5:2])


# # 常见方法
# append()   在列表尾部追加元素  s.append(1)
# insert()   在指定索引之前，插入该元素   s.insert(0,1)
# remove()   移除列表中第一个匹配到的值    s.remove()
# pop()      删除列表中指定索引位置的元素(未指定，默认删最后一个)    s.pop(2)/s.pop()
# sort()     对列表进行排序（os：必须同一类型)   s.sort()
# reverse()  反转列表元素  s.reverse()


# 案例  将用户输入的10个数字，存储到一个列表中，并将数字进行排序，输出最小值，最大值，和平均值
# 1.定义列表
# num_list=[]
# # #2.用户输入的十个数字存入列表
# for i  in range(10):
#     num=input("请输入数字")
#     num_list.append(num)
# print("列表",num_list)

# # 3.排序
# num_list.sort()
# print("排列后",num_list)
#
# # 4.输出最小值，最大值，和平均值----->sum()求和;len()获取元素个数(列表的长度)
# print("最小值:",num_list[0])
# print("最小值:", num_list[-1])
# print("平均值:", sum(num_list)/len(num_list))


# 案例2:合并两个列表,并去重
#
# num_list1=[23,65,23.5,77,245,77,2]
# num_list2=[23,34,72,78,24,89,24]
# # 1.合并列表
# #######方法一：for遍历创建新list
# for num in num_list2:
#     num_list1.append(num)
# print(num_list1)
#
#
# ######方法二：解包：将列表拆开成一个一个独立元素
# # 组包：将多个值合并到一个容器
# num_list=[*num_list1,*num_list2]
#
#
# #####方法三：算数运算符+
# num_list=num_list2+num_list1
#
#
# # 2.  去重####如何判断一个元素是否在列表中
#         #####使用in运算符，语法：元素 in 列表（返回结果为布尔值，true表示存在 ，false表示不存在
# new_list=[]#去重后的列表
# for num in num_list1:
#     #判断new_list中是否存在num元素，如果不存在，再添加
#     if num not in num_list:#判断元素是否存在新列表中，如果存在返回true，；如果不存在，返回false
#         new_list.append(num)
# print("去重后的列表",new_list)


# 1-20的平方注入列表
# num_list = []
# for i in range(1, 21):
#     num_list.append(i ** 2)
# print("平方列表", num_list)
