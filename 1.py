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
# a = 321
# print(a + 123, a - 123, a * 123, a / 123)
# a += 100
# print(a)
# print(200 > 100)

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
