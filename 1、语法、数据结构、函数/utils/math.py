def multiply(*args):
    total = 1
    for item in args:
        total *= item
    return total


# __name__ 是 Python 中一个隐含的变量它代表了模块的名字
# 只有被 Python 解释器直接执行的模块的名字才是 __main__
if __name__ == "__main__":
    print("call!!")
