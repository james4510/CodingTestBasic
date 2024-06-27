import turtle

t = turtle.Turtle()
t.width(3)
t.color("blue")
n = int(input("몇 각형을 그려줄까요?: "))


for i in range(n):
    t.forward(120)
    t.right(360/n)
