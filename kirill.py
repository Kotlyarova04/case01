import turtle
if __name__=='__main__':
    turtle.setup(width=1.0, height=1.0)
    turtle.pensize(5)
    turtle.pu()
    turtle.goto(-255,-400)
    turtle.pd()
    turtle.lt(90)
    turtle.fd(820)
    turtle.pu()
    turtle.goto(255,-400)
    turtle.pd()
    turtle.fd(820)
    turtle.pu()
    turtle.goto(0,0)
    turtle.pd()
#510 пикселей - одна треть
#765 пикселей - одна половина
def square(x):
    for _ in range(0,4):
        turtle.fd(x)
        turtle.rt(90)

