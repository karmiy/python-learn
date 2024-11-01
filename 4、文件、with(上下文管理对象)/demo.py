"""open file"""

import os


# def getDemoFile():
#     f = open(os.path.join(os.path.dirname(__file__), "open.txt"), "r", encoding="utf-8")
#     print(f.read())
#     f.close()


# getDemoFile()

"""open file error, finally"""


# def openErrorFile():
#     f = None
#     try:
#         f = open("open.txt", "r", encoding="utf-8")
#         print(f.read())
#     except FileNotFoundError:
#         print("无法打开指定的文件!")
#     except LookupError:
#         print("指定了未知的编码!")
#     except UnicodeDecodeError:
#         print("读取文件时解码错误!")
#     finally:
#         if f:
#             f.close()


# openErrorFile()

"""open file, with"""


# def openFileWith():
#     try:
#         # 打开文件并分配给变量 f
#         # 当离开 with 语句的代码块时，Python 会自动调用 f.close() 关闭文件，即使代码中发生异常
#         with open("open.txt", "r", encoding="utf-8") as f:
#             print(f.read())
#     except FileNotFoundError:
#         print("无法打开指定的文件!")
#     except LookupError:
#         print("指定了未知的编码!")
#     except UnicodeDecodeError:
#         print("读取文件时解码错误!")


# openFileWith()


# “上下文管理协议”的对象都可以使用 with, 这种协议包括实现 __enter__ 和 __exit__ 两个特殊方法
# class CustomContext:
#     def __enter__(self):
#         print("进入上下文")
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("退出上下文")


# with CustomContext() as c:
#     print("在上下文中")

"""write file"""


# def writeFile():
#     try:
#         with open(
#             os.path.join(os.path.dirname(__file__), "open.txt"), "r", encoding="utf-8"
#         ) as fs1:
#             data = fs1.read()
#             print(data)
#         with open(
#             os.path.join(os.path.dirname(__file__), "write.txt"), "w", encoding="utf-8"
#         ) as fs2:
#             fs2.write(data + "??")
#     except FileNotFoundError as e:
#         print("指定的文件无法打开.")
#     except IOError as e:
#         print("读写文件时出现错误.")
#     print("程序执行结束.")


# writeFile()

"""读写二进制"""
# 复制图片


# def copySuzyImg():
#     try:
#         with open(os.path.join(os.path.dirname(__file__), "suzy.png"), "rb") as fs1:
#             data = fs1.read()
#         with open(
#             os.path.join(os.path.dirname(__file__), "suzy-copy.png"), "wb"
#         ) as fs2:
#             fs2.write(data)
#     except FileNotFoundError as e:
#         print("指定的文件无法打开.")
#     except IOError as e:
#         print("读写文件时出现错误.")
#     print("程序执行结束.")


# copySuzyImg()

"""JSON"""
import json


def createJSON():
    myDict = {
        "name": "Karmiy",
        "age": 18,
        "friends": ["f1", "f2"],
        "cars": [
            {"brand": "BYD", "maxSpeed": 180},
            {"brand": "Audi", "maxSpeed": 280},
            {"brand": "Benz", "maxSpeed": 320},
        ],
    }
    try:
        with open(
            os.path.join(os.path.dirname(__file__), "data.json"), "w", encoding="utf-8"
        ) as fs:
            # Python 对象转换为 JSON 格式，并将其直接写入文件
            json.dump(myDict, fs, ensure_ascii=False, indent=4)
    except IOError as e:
        print(e)
    print("保存数据完成!")


createJSON()
