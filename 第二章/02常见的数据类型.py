#常见数据类型  type()获取指定的字面量或者变量的类型
# print("hello")
# # print(type("hello"))#str
# # print(type(1))#int
# # print(type(1.2))#float
# # print(type(True))#bool
# # print(type(False))#bool
# # print(type(None))#NoneType


# # #常见数据类型   isinstance(数据，类型)-->bool值--->判定是否是指定类型，是：Ture，否：False
# # num=100
# # print(type(num))
# # print(isinstance(num,int))
# # print(isinstance(num,float))
# # print(isinstance(num,bool))

# s1="hello"
# s2='world'
# s3='''
# sjfhsjkahfa
# '''
# print(s1)
# print(s2)
# print(s3)
# print(type(s1))
# print(type(s2))
# print(type(s3))


#转义字符 \'  \"  \n#换行  \t#缩进
# sum='It\'is very easy'
# print(sum)
#
# sum1="It\'is very easy"
# print(sum1)
#
# sum3="hello的意思就是\"您好\""
# print(sum3)
#
# sum4='hello的意思就是"您好"'
# print(sum4)
#
# print("\thello的意思\n\t就是您好")#\n换行   \t 按了TAB缩进



#字符串的拼接—------>str(int数字）
# name="范吉勇"
# age=22
# pro="物联网工程技术"
# happy="python"
# print("大家好，我是"+name+'，'+"今年"+str(age)+"岁，""学习专业是"+pro+",爱好"+happy)

#字符串格式化---->方式一：%s 占位符
# # name="范吉勇"
# # age=22
# # pro="物联网工程技术"
# # happy="python"
# print("大家好，我是%s，今年%s岁，学习专业%s,爱好%s"%(name,age,pro,happy))

# 方式二：f".......{变量名/表达式}......"------->推荐方式
# name="范吉勇"
# age=22
# pro="物联网工程技术"
# happy="python"
# print(f"大家好，我是{'范吉勇'}，今年{22}岁，学习专业{pro},爱好{happy}")



