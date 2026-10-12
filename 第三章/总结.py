# 特性	    字符串（str）	列表（list）	元组（tuple）	集合（set）	字典（dict）
# 有序性	 有序	         有序	        有序	           无序    	有序 (3.7+)
# 重复元素	 允许	         允许	        允许	           不允许	key 不允许
# 可变性	 不可变	         可变	        不可变	        可变	    可变
# 索引访问	 支持	         支持	        支持	            不支持	不支持
# 切片操作	 支持	         支持	        支持	            不支持	不支持
# 使用场景	文本处理 	有序可重复数据集合	固定数据记录	去重数据集合	键值对



#教务管理系统
Educational_System={}
menu='''
#############################################################################################################
#  1.添加学生信息   2.修改学生信息  3.删除学生信息  4.查询学生信息    5.列出所有学生    6.统计班级成绩    7.退出系统   #
#############################################################################################################

'''
print("教育购物系统")

while True:
    print(menu)
    choice = input("请选择要执行的操作")
    match choice:
        case "1":  # 录入
            name = input("请输入姓名：")
            chinese_score = input("请输入语文成绩：")
            math_score= input("请输入数学成绩：")
            english_score = input("请输入英语成绩：")
            if name in Educational_System:
                print("该生信息已录入，请返回")
                continue
            else:
                Educational_System[name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
                print("录入成功")
        case "2":  # 修改
            name = input("请输入要修改的姓名：")
            if name not in Educational_System:
                print("未录入该生信息，请重新输入")
                continue


            chinese_score = input("请输入修改后的语文成绩：")
            math_score= input("请输入修改后的数学成绩：")
            english_score = input("请输入修改后的英语成绩：")
            Educational_System[name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
            print(f"{name}信息修改成功")
        case "3":  # 删除
            name = input("请输入要删除的姓名：")
            if name not in Educational_System:
                print("该生信息未录入，请重新输入")
                continue
            else:
                del Educational_System[name]
                print(f"{name}信息删除成功")
        case "4":  # 查
            for name in Educational_System.keys():
                all_score = Educational_System[name]
                print(f"学生：{name} 语文成绩：{all_score['chinese']} 英语成绩：{all_score['english']} 数学成绩：{all_score ['math']} ")
        case "5":  # 列出#遍历

            for name, score in Educational_System.items():
                print(f"学生：{name}，语文：{score['chinese']}，数学：{score['math']}，英语：{score['english']}")

        case _:
            print("非法操作，请重新输入")