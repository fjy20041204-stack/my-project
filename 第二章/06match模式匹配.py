#match....case  模式匹配：工作日程安排
# day=input("请输入星期几：")
#
# match day:
#     case "1":
#         print("周一")
#     case "2":
#         print("周二")
#     case "3":
#         print("周三")
#     case "4":
#         print("周四")
#     case "5":
#         print("周五")
#     case "6" | "7":
#         print("周末")
#     case _:#匹配其他所有情况
#         print("输入有误")



#案例 基于match。。。case 实现一个简易计算器 可以实现+ - * / 运算，用户输入需要运算的两个数及运算符之后，就可以进行计算
# num1=float(input("请输入第一个数："))
# num2=float(input("请输入第二个数："))
# oper=input("请输入运算符(+ - * / ):")
# match oper:
#     case "+":
#         print(f"{num1}+{num2}={num1+num2}")
#     case "-":
#         print(f"{num1}-{num2}={num1-num2}")
#     case "*":
#         print(f"{num1}*{num2}={num1*num2}")
#     case "/" if num2 !=0:  ##if 成立，才匹配这个case
#         print(f"{num1}//{num2}={num1/num2}")
#     case _:
#         print("操作不支持!!!!!!")




#游戏系统操作
# move=input("请输入动作")
# match move:
#     case "w"|"W":
#         print("玩家向上移动")
#     case "s"|"S":
#         print("玩家向下移动")
#     case "a"|"A":
#         print("玩家向左移动")
#     case "d"|"D":
#         print("玩家向右移动")
#     case " ":
#         print("玩家跳跃")
#     case "j"|"J":
#         print("玩家攻击")
#     case "esc"|"ESC":
#         print("玩家退出")
#     case _:
#         print("请输入正确按键")