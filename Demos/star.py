import turtle
import random
import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("画一个随机颜色的五角星")
root.geometry("500x500")

# 随机颜色列表
colors = (
    ["red"] * 20
    + ["orange"] * 12
    + ["yellow"] * 10
    + ["green"] * 6
    + ["cyan"] * 5
    + ["blue"] * 3
    + ["purple"] * 1
)

# 初始化 Turtle 画布
canvas = turtle.ScrolledCanvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
pen = turtle.RawTurtle(screen)
pen.speed(3)


# 画五角星函数
def draw_star():
    # 清除画布上已有的图形
    pen.clear()
    # 随机选择颜色
    fill_color = random.choice(colors)
    pen.color("black")  # 设置星星边框为黑色
    pen.fillcolor(fill_color)  # 设置星星填充颜色
    # 绘制五角星
    pen.penup()
    pen.goto(-100, 0)
    pen.setheading(0)  # 确保起始方向
    pen.pendown()
    pen.begin_fill()
    for _ in range(5):
        pen.forward(200)
        pen.right(144)
    pen.end_fill()


# 创建按钮
button = tk.Button(root, text="生成星星", command=draw_star)
button.pack(pady=20)

# 运行 Tkinter 主循环
root.mainloop()
