#set 无序的、不可重复、可修改
#
# s1={1,34,5,24,61,13,561,22}
# print(s1)
# print(type(s1))
#
# #定义空集合---不可使用s={}（s={}是空字典）
# s2=set()
# print(s2)
# print(type(s2))


#
# add(..)	            添加元素到集合中	                                s1.add('t')	集合元素不可重复；添加已存在元素不会报错，无效果
# remove(..)	        移除集合中的指定元素（元素不存在将报错）	        s1.remove('t')	❗元素不存在 → KeyError；只删单个元素
# pop()	                 随机删除集合中的元素并返回	                    e = s1.pop()	集合无序，随机删一个；空集合 pop 会报错
# clear()	             清空集合	                             s1.clear()	集合对象保留，变成空集合 set()
# difference()	        差集：在 s1 里、不在 s2 里的元素	        s1.difference(s2)	等价运算符：s1 - s2，返回新集合，不修改原集合
# union()	            并集：两个集合所有元素，自动去重	        s1.union(s2)	等价运算符：`s1	s2`，返回新集合
# intersection()	    交集：同时在 s1 和 s2 中的元素	              s1.intersection(s2)	等价运算符：s1 & s2，返回新集合

