import turtle
if __name__=='__main__':
    turtle.pensize(5)
    turtle.pu()
    turtle.goto(-134,-400)
    turtle.pd()
    turtle.lt(90)
    turtle.fd(800)
    turtle.pu()
    turtle.goto(133,-400)
    turtle.pd()
    turtle.fd(800)
    turtle.pu()
    turtle.goto(0,0)
    turtle.pd()

def square(x):
    for _ in range(0,4):
        turtle.fd(x)
        turtle.rt(90)

