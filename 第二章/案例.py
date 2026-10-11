# break：只能出现在循环中，表示结束，跳出循环（break跳出循环时，while后面的else中的代码不再执行）
#continue：只能出现在循环中，中断本次循环，直接进入下一次循环

# while True:
#     #接受输入的用户名密码
#     username=input("请输入正确用户名")
#     password = input("请输入正确密码")
#     #校验：输入的用户名和密码不能为空
#     if username == "" or password == "":
#         print("输入的用户名密码不能为空，请重新输入")
#         continue#结束当前循环，进入下一次循环
#     #判断用户名和密码的正确性，执行登录操作
#     if username == "admin" and password == "111":
#         print("登录成功")
#         break
#     if username == "a" and password == "333":
#         print("登录成功")
#         break
#     if username == "b" and password == "123":
#         print("登录成功")
#         break
#     else:
#         print("用户名或密码错误，请重新输入")
#



# for n in range(5):
#
#     #接受输入的用户名密码
#     username=input("请输入正确用户名")
#     password = input("请输入正确密码")
#     #校验：输入的用户名和密码不能为空
#     if username == "" or password == "":
#         print("输入的用户名密码不能为空，请重新输入")
#         continue#结束当前循环，进入下一次循环
#     #判断用户名和密码的正确性，执行登录操作
#     if username == "admin" and password == "111":
#         print("登录成功")
#         break
#     if username == "a" and password == "333":
#         print("登录成功")
#         break
#     if username == "b" and password == "123":
#         print("登录成功")
#         break
#     else:
#         print("用户名或密码错误，请重新输入")



#猜数字游戏

import random
random_num = random.randint(1, 100)#生成随机数

while True:
    # 接收输入的数字
    num = int(input("请输入一个数字"))
    # 比较
    if num > random_num:
        print("您输入的数字太大了！")
    elif num < random_num:
        print("您输入的数字太小了")
    else:
        print("好棒猜对啦，6666")
        break
print("随机数为",random_num)

