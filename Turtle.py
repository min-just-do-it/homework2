import turtle as t

def draw_dim():
    dim = t.Turtle()
    dim.speed(0)
    dim.penup()
    dim.goto(-200, -150)  # 왼쪽 아래 시작점
    dim.pendown()
    dim.forward(400)      # x축 (가로축)
    dim.penup()
    dim.goto(-200, -150)
    dim.left(90)
    dim.pendown()
    dim.forward(300)      # y축 (세로축)
    dim.hideturtle()

    # y축 눈금
    dim.penup()
    for y in range(0, 301, 50):  # 50 간격
        dim.goto(-205, -150 + y)
        dim.write(str(y), align="right")


# 막대 그리는 함수
def draw_bar(x, height, label, color = "black"):
    bar_width = 40
    base_y = -150

    pen = t.Turtle()
    pen.speed(0)
    pen.fillcolor(color)
    pen.penup()
    pen.goto(x, base_y)
    pen.pendown()

    pen.begin_fill()
    pen.forward(bar_width)
    pen.left(90)
    pen.forward(height)
    pen.left(90)
    pen.forward(bar_width)
    pen.left(90)
    pen.forward(height)
    pen.left(90)
    pen.end_fill()

    # 점수 출력 (막대 위)
    pen.penup()
    pen.goto(x + bar_width / 2, base_y + height + 10)
    pen.write(f"{height:.6f}", align="center")

    # 과목명 출력 (막대 아래)
    pen.goto(x + bar_width / 2, base_y - 20)
    pen.write(label, align="center")

    pen.hideturtle()
