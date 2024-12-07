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

"""装饰器"""

# from functools import wraps
# from time import time


# def record_time(func):
#     """自定义装饰函数的装饰器"""

#     # args 是位置参数，如 add(1, 2, 3, 4) 里 (1,2,3,4) 元组
#     # kwargs 是关键字参数 my_function(name="Alice", age=30)
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         print(f"{func.__name__}: {time() - start}秒")
#         return result

#     return wrapper


# class Person(object):
#     @record_time
#     def test(self):
#         print("run test")


# person = Person()
# person.test()

"""参数化的装饰器"""
# 其实就是多包一层函数返回一个装饰器
# from functools import wraps
# from time import time


# def record(output):
#     def decorate(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time()
#             result = func(*args, **kwargs)
#             output(func.__name__, time() - start)
#             return result

#         return wrapper

#     return decorate


# def print_output(func_name, duration):
#     print(f"{func_name} executed in {duration:.4f} seconds")


# # 使用参数化装饰器
# @record(print_output)
# def test():
#     for _ in range(10):
#         pass


# test()

"""定义类的方式定义装饰器"""
# from functools import wraps
# from time import time


# class Record:

#     def __init__(self, output):
#         self.output = output

#     def __call__(self, func):

#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time()
#             result = func(*args, **kwargs)
#             self.output(func.__name__, time() - start)
#             return result

#         return wrapper


# def output_function(name, duration):
#     print(f"Function '{name}' executed in {duration:.4f} seconds")


# @Record(output_function)
# def test():
#     for _ in range(10):
#         pass


# test()

"""装饰器创建单例"""
# 但这个单例有线程安全问题：
#   线程共享 instances
#   如下多个线程同时 create_person_instance
#       是有可能线程 1 走到 if cls not in instances，但还没 instances[cls] = cls(*args, **kwargs) 创建，线程 2 又 if cls not in instances，判断就不对了

# from functools import wraps
# from threading import Thread, current_thread


# def singleton(cls):
#     instances = {}

#     @wraps(cls)
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]

#     return wrapper


# @singleton
# class Person(object):
#     __id = 1

#     def getId(self):
#         self.__id += 1
#         return self.__id


# def create_person_instance():
#     person = Person()
#     print(f"Instance ID in thread {current_thread().name}: {person.getId()}")


# threads = []
# for i in range(5):
#     thread = Thread(target=create_person_instance)
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

"""装饰器创建单例（线程安全）"""
# from functools import wraps
# from threading import RLock
# from threading import Thread, current_thread


# def singleton(cls):
#     instances = {}
#     locker = RLock()

#     @wraps(cls)
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             with locker:
#                 if cls not in instances:
#                     instances[cls] = cls(*args, **kwargs)
#         return instances[cls]

#     return wrapper


# @singleton
# class Person(object):
#     __id = 1

#     def getId(self):
#         self.__id += 1
#         return self.__id


# def create_person_instance():
#     person = Person()
#     print(f"Instance ID in thread {current_thread().name}: {person.getId()}")


# threads = []
# for i in range(5):
#     thread = Thread(target=create_person_instance)
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()
