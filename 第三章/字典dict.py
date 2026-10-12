# #Python 中的字典 (dict)，里面存储的是键值对 (key: value) 类型的数据，可以根据键 (key) 查找到对应的值 (value)。
# #特点：键值对（key：value）存储，键（key）不可重复，可修改
# # 字典---key不可重复（如果重复，后面的值覆盖前面的值），
# # key必须得是不可变类型（str，int。float，tuple），不能是list，set，dict
#
#
# #根据key获得value
# # 值=字典名称【key】 ---  score=dict【“key”】
#
#
dict1 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688}

print(dict1)
print(type(dict1))

# # # key必须得是不可变类型（str, int, float, tuple），不能是 list、set、dict
dict2 = {0:670, 1.5:608, (1,2):580, ('A','B'):688}
print(dict2)
# #
# # # 访问
print(dict1["李慕婉"]) # 获取
# # dict1["李慕婉"] = 688#修改
# # print(dict1)
#
# # 类型	操作	含义	样例
# # 添加	字典名称 [key] = value	往指定字典中添加 key-value 键值对	            dict1 ["涛哥"] = 688
# # 删除	字典名称.pop (key)	    删除字典中指定的 key，并返回该 key 对应的 value	score = dict1.pop ("涛哥")
# # 	    del 字典名称 [key]	    删除字典中指定的键值对	                        del dict1 ["涛哥"]
# # 修改	字典名称 [key] = value	修改字典中指定的 key 对应的值	                dict1 ["小智"] = 658
# # 查询	字典名称 [key]	        根据 key 获取 value	                        dict1 ["涛哥"]
# #   	字典名称.get (key)	    根据 key 获取 value	                        dict1.get ("涛哥")
# # 	    字典名称.keys ()	        获取所有的 key	                            dict1.keys()
# # 	     字典名称.values ()	    获取所有的 value	                            dict1.values()
# #   	字典名称.items ()	    获取所有的 key-value 键值对	                dict1.items()
#
#
# # ----------------字典 常见操作----------------
# dict1 = {"王林":670, "李慕婉":608, "许立国":580, "韩立":688}
# print(dict1)
#
# # 添加 - key不存在就是添加
# dict1["涛哥"] = 550
# print(dict1)
#
# # 修改 - key存在就是修改
# dict1["涛哥"] = 620
# print(dict1)
#
# # 查询
# print(dict1["涛哥"]) # 根据key获取value
# print(dict1.get("涛哥")) # 根据key获取value
# #
# print(dict1.keys()) # 获取所有的key
# print(dict1.values()) # 获取所有的value
# print(dict1.items()) # 获取所有的键值对 key:value
#
# # 删除
# score = dict1.pop("许立国")
# print(score)
# print(dict1)
#
#
# del dict1["韩立"]
# print(dict1)
#
# #遍历
for key in dict1.keys():
    print(f"{key}: {dict1[key]}")
#
# for item in dict1.items():
#     print(f"{item[0]}: {item[1]}")
#
# for k,m in dict1.items():
#     print(f"{k}: {m}")
#


#案例
# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
#
# 1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
#
# 2．修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息
#
# 3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
#
# 4．查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
#
# 5．退出购物车

#结构 shopping_cart={"mate80":{"price:2000,"num":1},”鼠标“：{，。。。}}
# shopping_cart={}
#
# menu='''
# ###########购物车#############
# #        1.添加购物车        #
# #        2.修改购物车        #
# #        3.删除购物车        #
# #        4.查询购物车        #
# #        5.退出购物车        #
# #############################
# '''
# print("欢迎使用购物车~")
# while True:
#     print(menu)
#
#     # 2.执行的操作
#     choice = input ("请选择要执行的操作")
#
#     match choice:
#         case "1":  # 添加购物车
#             goods_name = input("请输入要添加的商品")
#             goods_price = input("请输入要添加商品的价格")
#             goods_num = input("请输入要添加商品的数量")
#             # 如果商品存在，不执行
#             if goods_name in shopping_cart:
#                 print(f"{goods_name}已添加，请重新输入")
#             else:
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#                 print("添加成功！")
#
#         case "2":  # 修改购物车
#             goods_name = input("请输入要修改的商品")
#             # 如果商品不存在，无法修改
#             if goods_name not in shopping_cart:
#                 print(f"{goods_name}未录入，无法修改，请重新选择")
#                 continue
#             goods_price = float(input("请输入要修改商品的价格"))
#             goods_num = int(input("请输入要修改商品的数量"))
#             shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print("修改成功！")
#
#         case "3":  # 删除购物车
#             goods_name = input("请输入要修改的商品")
#             # 如果商品不存在，无法删除
#             if goods_name not in shopping_cart:
#                 print(f"{goods_name}未录入，无法删除，请重新选择")
#             else:
#                 del shopping_cart[goods_name]
#                 print("删除成功！")
#
#         case "4":  # 查询购物车
#
#
#             for goods_name in shopping_cart.keys():
#                 goods_flot = shopping_cart[goods_name]
#                 print(f"商品名称:{goods_name} 商品价格:{goods_flot["price"]} 商品数量:{goods_flot["num"]}")
#
#
#
#         case "5":  # 退出购物车
#             print("下次见~")
#             break
#         case _:  # 匹配其他操作
#             print("非法操作，请重新输入")


