# #函数定义----define(定义)
# #
# # def out_line():
# #     print("________")
# #     print("________")
# # #函数调用    函数定义的时候并不会执行，只有在被调用的时候，函数体的代码才会执行。；函数先定义，后调用
# # out_line()
#
# # 函数的参数与返回值
# # 函数1：计算圆的面积 -- 半径
# # def circle_area(r):
# #     area = 3.14 * r ** 2
# #     return area
# #
# # area=circle_area(10)
# # print(area)
# #
# #
# # 函数2：计算长方形的面积--长乘宽
#
# def Rectangle_Area(l,w):
#     """
#     根据长方形的长度和宽度，计算长方形的面积
#     :param l: 长度
#     :param w: 宽度
#     :return: 长方形的面积
#     """
#     area = l * w
#     return area
# # help(Rectangle_Area)
#
# print(Rectangle_Area(10,5))
#
#
#
# #函数3：计算圆的面积和周长-------如果有多个返回值，多个返回值逗号分割-------多个返回值封装到元组中
# def circle_area_len(r):
#     return round(3.14 * r * r,1),round( 2 * 3.14 * r,1)

# #round(四舍五入的数字，保留几位小数）

# area,len = circle_area_len(10)
# print(area)
# print(len)
#



# 函数的嵌套调用
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")

def function_b():
    print("b ... before")
    function_c()
    print("b ... after")

def function_c():
    print("c ...")

function_a()
print("函数调用完毕 ~")
