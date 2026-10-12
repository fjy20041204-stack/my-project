# #索引------不可变（无法修改）、有序性、可迭代
# s="hello,world"
# print(s[4])#正向索引
# print(s[-4])#反向索引
# #
#
# for i in s:
#     print(i)
#
# # 切片
# print(s[0:5:1])
# print(s[6:12:1])
# print(s[6::1])
#
# #步长----正数：从前往后；负数：从后往前
# print(s[-1:-6:-1])
# print(s[::-1])


# 方法	作用	样例
# find()	在字符串中查找子串，返回第一次出现的索引位置，找不到返回 - 1	s.find('Python')
# count()	统计子串在字符串中出现的次数	                               s.count('H')
# upper()	将字符串中的所有字母转换为大写	                        s.upper()
# lower()	将字符串中的所有字母转换为小写	                        s.lower()
# split()	将字符串按指定分隔符分割成列表	                        s.split(' ')
# strip()	去除字符串两端的空白字符或指定字符	                         s.strip() / s.strip('*')
# replace()	将字符串中的指定子串替换为新的子串	                         s.replace('H','C')
# startswith()	检查字符串是否以指定子串开头，返回布尔值	                s.startswith('P')


# 案例
#方法1
# mail = input("请输入邮箱")
# if mail.count("@") == 1 and mail.count(".") >= 1:
#     print = {f"{mail}是正确邮箱"}
# else:
#     print = {f"{mail}是不正确邮箱"}
#

# 方法二：in运算符
# mail = input("请输入邮箱")
# if mail.count("@") == 1 and "." in mail:
#     print = {f"{mail}是正确邮箱"}
# else:
#     print = {f"{mail}是不正确邮箱"}


