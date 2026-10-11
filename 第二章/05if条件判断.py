#if条件判断：如果超过680，就去清华
# score=700
# if score>680:
#     print("欢迎来到清华")
#     print("恭喜你")
# print('------------')



#案例，实现成功登录的功能(正确账号密码1999999999，8888888888）
#正确的账号密码
# ok_account="1999999999"
# ok_password="8888888888"
# #1.接受用户账号和密码
# account=input("请输入您的账号:")
# password=input("请输入您的密码:")
#
# #2.判断账号密码是否正确，正确，登录成功，进入网站
# if account==ok_account and password==ok_password:
#     print("登录成功")
#     print("进入")


# #3.判断账号密码是否有错误，如果有一个错误，则失败，提示错误
# if account!=ok_account or password!=ok_password:
#     print("登录失败")
#     print("请重试")




# 案例，实现成功登录的功能(正确账号密码1999999999，8888888888）
# 正确的账号密码
# ok_account = "1999999999"
# ok_password = "8888888888"
# # 1.接受用户账号和密码
# account = input("请输入您的账号:")
# password = input("请输入您的密码:")
#
# # 2.判断账号密码是否正确，正确，登录成功，进入网站
# if account == ok_account and password == ok_password:
#     print("登录成功")
#     print("进入")
#
# # 3.判断账号密码是否有错误，如果有一个错误，则失败，提示错误
# else:
#     print("登录失败")
#     print("请重试")


# 案例：根据用户输入的年份，判断这一年是闰年还是平年（非整百年份，且被4整除的年份是闰年；整百年份（1900，2000）必须被400整除才是闰年）
# year=int(input("请输入要判断的年份:"))
# if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")


#练习1，判断奇数偶数
# num=int(input("请输入您要判断的数字"))
# if num % 2 == 0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")


#练习2：判断用户是否成年
# age=int(input("请输入您的年龄："))
# if age>=18:
#     print("您已成年")
# else:
#     print("您是未成年")


#练习3：判断这个数是正数还是负数
# num=int(input("请输入数字"))
# if num>0:
#     print(f"{num}是正数")
# elif num<0:
#     print(f"{num}是负数")
# else:
#     print(f"{num}为0")


#练习4：判断是否及格
# score=int(input("请输入您的分数:"))
# if score>=60:
#     print("及格")
# else:
#     print("不及格")



#案例：根据输入的用户名和密码进行登录----admin/66666   root/123456     sss/88888
# username=input("请输入用户名")
# password=input("请输入密码")
# if username=="admin" and password=="66666":
#     print("登录成功")
# elif username=="root" and password=="123456":
#     print("登录成功")
# elif username == "sss" and password == "88888":
#     print("登录成功")
# else:
#     print("登录失败，用户名或密码错误")


##练习1：判断成绩等级
# score=input("请输入您的成绩:")
# if score>="85":
#     print("您的成绩为优秀")
# elif score<"85" and score>="60":
#     print("您的成绩为及格")
# else:
#     print("您的成绩为不及格")

#练习二：输入购物车商品总金额，根据折扣规则，算出应付金额
# num=int(input("请输入您的总金额:"))
# if num>=500:
#     ok=num*0.8
#     print(f"您应付金额为,{ok}")
# elif num>=300 and num<500:
#     ok=num*0.9
#     print(f"您应付金额为:{ok}")
# elif num >= 100 and num < 300:
#     ok = num * 0.95
#     print(f"您应付金额为:{ok}")
# else:
#     print(f"您应付金额为:{num}")


'''
 案例：三角形类型判断：根据输入的三条边（正整数），判断等边三角形，等腰三角形，普通三角形，还是不能构成三角形，
 1.两边之和大于第三边
 2.三边相等：等边
 两边相等：等腰
 三边不相等：普通三角形
'''
# #接受三边边长
# a=int(input("请输入第一边边长："))
# b=int(input("请输入第二边边长："))
# c=int(input("请输入第三边边长："))
# #判断类型   pass 是一个空语句，起到语法展位的作用
# if a+b>c and a+c>b and b+c>a:
#     if a==b==c:
#         print(f"{a},{b},{c}这三边边长构成等边三角形")
#     elif a==b or b==c or a==c:
#         print(f"{a},{b},{c}这三边边长构成等腰三角形")
#     else:
#         print(f"{a},{b},{c}这三边边长构成普通三角形")
# else:
#     print(f"{a}{b}{c}这三个边长不能构成三角形")


