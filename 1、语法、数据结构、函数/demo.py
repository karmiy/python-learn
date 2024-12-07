"""
Version: 0.1
Author: Karmiy
"""

"""print"""

# num = {1, 2, 3}
# print("hello")
# %d 是整数，后面的 1,2,3 会被填到前面
# print("%d + %d = %d" % (1, 2, 3))

"""import"""
# import this
# import module1 as m1
# import module2 as m2

# m1.foo()
# m2.foo()

# from module1 import foo
# from module2 import foo
# foo()

"""turtle"""
# python 内置模块，turtle 在屏幕上绘制图形
# import turtle

# 画笔粗细
# turtle.pensize(4)
# turtle.pencolor("red")

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

# # 保持绘图窗口打开。它实际上是一个事件循环，等待用户的操作（如关闭窗口）而不让程序立即退出
# turtle.mainloop()

"""运算符"""
a = 321
# print(a + 123, a - 123, a * 123, a / 123)
# a += 100
# print(a)
# print(200 > 100)
# 整除
# print(a // 100)

"""类型获取/转换"""
# print(type(123), type(12.1), type(1 + 5j), type("d"), type(True))

# a = int("123")
# print("类型转换结果：%d" % (a))

"""input 获取键盘输入"""
# 拿到的会是字符串
# f = float(input("请输入华氏温度: "))
# c = (f - 32) / 1.8
# print("摄氏度：%d" % (c))

""""if else"""
# x = float(input("x = "))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     if x >= -5 or x == -6:
#         y = x + 2
#     elif x < -6 and x > -10:
#         y = x + 1
#     else:
#         y = x
# print("f(%.2f) = %.2f" % (x, y))

"""for-in"""
# range(101)：[0, 100)
# range(1, 101)：[1, 100)
# range(1, 101, 2)：[1, 100)，其中 2 是步长，即每次数值递增的值，1, 3, 5, ..., 99
# range(100, 0, -2)：[100, 0)，其中 -2 是步长，即每次数字递减的值
# sum = 0
# count = 0
# for x in range(101):
#     sum += x
#     if x >= 90:
#         count += x
# print("输出", sum, count)

"""while"""
# import random

# answer = random.randint(1, 3)  # [1, 3] 随机数
# counter = 0
# while True:
#     counter += 1
#     number = int(input("请输入: "))
#     if number < answer:
#         print("大一点")
#     elif number > answer:
#         print("小一点")
#     else:
#         print("恭喜你猜对了!")
#         break
# print("你总共猜了%d次" % counter)

"""function"""
# 注：同名函数后者覆盖前者


# def add(a, b=10):
#     return a + b


# print(add(10, 12))
# print(add(10))
# print(add.__name__)  # 函数名


# def subtract(a, b):
#     return a - b


# print(subtract(12, 2))
# # 可以参数不按顺序
# print(subtract(b=2, a=12))

"""lambda 匿名函数"""

# heapq 模块主要用于高效地处理排序或获取极值的操作

# import heapq

# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {"name": "IBM", "shares": 100, "price": 91.1},
#     {"name": "AAPL", "shares": 50, "price": 543.22},
#     {"name": "FB", "shares": 200, "price": 21.09},
#     {"name": "HPQ", "shares": 35, "price": 31.75},
#     {"name": "ACME", "shares": 75, "price": 115.65},
# ]
# # 找出最大的 3 个数
# print(heapq.nlargest(3, list1))
# # lambda 是匿名函数，这里等价与 (x) => x.price
# print(heapq.nlargest(2, list2, key=lambda x: x["price"]))


"""module, __name__"""
# from utils import math

# print(math.multiply(1, 2, 3, 4, 5))

# from utils import math as m

# print(m.multiply(1, 2, 3, 4, 5))

# from utils.math import multiply

# print(multiply(1, 2, 3, 4, 5))

"""global, nonlocal var"""
# python 中作用域里的变量是局部变量，不会像 JS 一样自动往上层找

# global
# def testGlobal():
#     global g
#     g = 100


# testGlobal()
# print(g)


# nonlocal
# def outer():
#     x = 10  # 外层函数的局部变量

#     def inner():
#         nonlocal x  # 声明使用外层作用域的 x
#         x += 5  # 修改外层函数中的 x

#     inner()
#     print(x)  # 输出：15，因为 inner() 中的修改生效了


# outer()


"""String"""
# print(
#     """
# hello,
# world!
# """
# )

# print("\n\\hello, world!\\\n")

# r 前缀，则 \ 不会转义
# print(r"\n\\hello, world!\\\n")

# 复制 3 次
# print("hello " * 3)

# 存在，例如 include
# print("ll" in "ll1")

# print("123"[1])

# [1, 3)
# print("12345"[1:3])

# [1,]
# print("12345"[1:])

# bdf, 从 1 开始，每隔 2 个字符串取一下
# print("abcdefg"[1::2])

# aceg, 从 0 开始，每隔 2 个字符串取一下
# print("abcdefg"[::2])

# print("abcdefg".upper())

# f 格式化字符串
# k1 = 11
# k2 = 22
# print(f"{k1} * {k2} = {k1 * k2}")

"""String 正则"""
# import re

# m = re.match(r"^[0-9a-zA-Z_]{6,20}$", "TestUser_12345")
# if not m:
#     print("不符合正则")
# else:
#     print("符合正则")

"""Array"""
# list = [1, 3, 5, 7, 100]
# 添加元素
# list.append(200)
# 在 index 1 的前面插入一个 4
# list.insert(1, 4)
# print(list)

# 合并
# list = [10]
# list.extend([20, 30, 40])
# print(list, len(list))

# 移除
# list = [10, 20, 30, 40]
# list.remove(30)
# print(list)

# 在某位移除
# list = [10, 20, 30, 40]
# list.pop(1)
# print(list)

# 清空
# list = [10, 20, 30, 40]
# list.clear()
# print(list)

# 列表推导式
# names = ["A1", "A2"]
# courses = ["语文", "数学", "英语"]
# scores = [[None] * len(courses) for _ in range(len(names))]
# print(scores)  # [[None, None, None], [None, None, None]]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f"请输入{name}的{course}成绩: "))
# print(scores)

"""生成式和生成器"""
# f = [x for x in range(1, 10)]
# print(f)
# f = [x + y for x in "ABCDE" for y in "1234567"]
# print(f)

# import sys

# f = [x**2 for x in range(1, 10)]
# print(sys.getsizeof(f))  # 查看对象占用内存的字节数
# print(f)

"""tuple 元组"""
# 元组中的元素是无法修改的
# 元组在创建时间和占用的空间上面都优于列表

# t = ("a", True, 1)
# print(t)
# print(t[1])
# t = list(t)
# print(t)
# t = tuple(t)
# print(t)

"""set 集合"""
# 不重复
# print({1, 2, 3})
# print(set((2, 3, 4)))
# s = {1, 2, 3}
# s.add(2)
# s.update([2, 3])
# print(s)  # 还是 1,2,3,不可重复
# print({1, 2, 3} & {2, 3, 4})  # {2, 3}
# print({1, 2, 3} ^ {2, 3, 4})  # {1, 4}, 对称差,只存在一个集合里的
# print({1, 2, 3} | {2, 3, 4})  # {1, 2, 3, 4}
# print({1, 2, 3} - {2, 3, 4})  # {1}
# print({1, 2, 3} < {1, 2, 3, 4})  # True

"""dict 字典(类似 map)"""
# print({"a": 1, "b": 2})
# print(dict(a=1, b=2))

# {'a': '1', 'b': '2', 'c': '3'},zip 会构造出 [('a', '1'), ('b', '2'), ('c', '3')]
# print(dict(zip("abc", "123")))

# print({"a": 1, "b": 2}.get("b"))

# d = {"a": 1, "b": 2}
# d.update(c=3)
# d.pop("b")
# print(d)

# 推导式
# d = {"a": 100, "b": 200, "c": 300}
# d2 = {key: value for key, value in d.items() if value > 100}
# print(d2)

"""pass 占位语句"""
# pass，表示“这里暂时没有实现内容，或者没有操作，但语法上需要一条语句”
# 可以避免语法错误，方便之后添加实际代码


# def my_function():
#     pass  # 先占位，之后再实现功能
