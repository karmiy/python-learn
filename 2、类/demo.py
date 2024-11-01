"""class"""

# class Student(object):
#     id = 1
#     # 私有变量
#     __id = 2

#     # __init__ 是一个特殊方法用于在创建对象时进行初始化操作
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def study(self, course_name):
#         print(f"{self.name} 正在学习{course_name}, __id: {self.__id}")

#     # 私有函数
#     def __bar(self):
#         print("__bar")


# stu = Student("karmiy", 30)
# stu.study("数学")
# print(stu.id)

"""@property"""


# class Person(object):

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     # 访问器 - getter方法
#     @property
#     def name(self):
#         return self._name

#     # 访问器 - getter方法
#     @property
#     def age(self):
#         return self._age

#     # 修改器 - setter方法
#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         if self._age <= 16:
#             print(f"{self._name}正在玩飞行棋")
#         else:
#             print(f"{self._name}正在玩围棋")


# person = Person("karmiy", 16)
# person.play()
# person.age = 22
# person.play()

"""__slots__"""
# 限定对象只能绑定某些属性
# 对子类无效


# class Person(object):
#     __slots__ = ("_name", "_age", "_gender")

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     # 访问器 - getter方法
#     @property
#     def name(self):
#         return self._name

#     # 访问器 - getter方法
#     @property
#     def age(self):
#         return self._age

#     # 修改器 - setter方法
#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         if self._age <= 16:
#             print(f"{self._name}正在玩飞行棋")
#         else:
#             print(f"{self._name}正在玩围棋")


# person = Person("karmiy", 16)
# person._gender = 1
# person._code = 2 # error

"""static，classmethod 类方法"""
# classmethod 可以拿到类自己


# class Triangle(object):

#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c

#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and b + c > a and a + c > b

#     @classmethod
#     def build(cls):
#         return cls(1, 2, 3)

#     def print(self):
#         print(f"{self._a}, {self._b}, {self._c}")


# print(Triangle.is_valid(1, 2, 3))
# triangle = Triangle.build()
# triangle.print()

"""extends 继承"""


# class Person(object):

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     # 访问器 - getter方法
#     @property
#     def name(self):
#         return self._name

#     # 访问器 - getter方法
#     @property
#     def age(self):
#         return self._age

#     # 修改器 - setter方法
#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         if self._age <= 16:
#             print(f"{self._name}正在玩飞行棋")
#         else:
#             print(f"{self._name}正在玩围棋")


# class Teacher(Person):
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title

#     @property
#     def title(self):
#         return self._title


# teacher = Teacher("karmiy", 18, "K")
# print(teacher.title)

"""abstract 抽象类"""
# 多态：方法重写让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为

# from abc import ABCMeta, abstractmethod

# from abc import ABCMeta, abstractmethod


# class Pet(object, metaclass=ABCMeta):
#     def __init__(self, nickname):
#         self._nickname = nickname

#     @abstractmethod
#     def make_voice(self):
#         pass


# class Dog(Pet):
#     def make_voice(self):
#         print(f"{self._nickname} say ~~")


# dog = Dog("苏西")
# dog.make_voice()
