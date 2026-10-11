
# 循环嵌套：输入一个长度m，宽度n，打印一个长方体
# 长度10，宽度5，的长方体
#   **********
#   **********
#   **********
#   **********
#   **********

# print("*"):自带换行效果，每一次执行都会输出到新一行
# print("*", end="  ")end表示每一次输出以什么结束；默认\n，换行


# #1.接受键盘录入m，n
# #长度
# m=int(input("请输入长度："))
# #宽度
# n=int(input("请输入宽度："))
# # 2.打印长方体
# for o in range(n ):#控制行数
#     for i in range(m):#控制列数
#         print("*",end="  ")
#     print()




#九九乘法表
# for i in range(1,10):#外层循环，控制行
#     for j in range(1,i+1):#内层循环，控制列
#         print(f"{i}x{j}={i*j}",end="\t ")
#     print()


# 打印等腰三角形（腰长5）
# for a in range(1,6):
#     for b in range(1,a+1):
#         print("*",end="\t")
#     print()


# #打印数字金字塔
# for a in range(1,7):
#     for b in range(1,a+1):
#         print(f"{b}",end="\t")
#     print()