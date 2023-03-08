import turtle
import math
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

#510 пикселей - одна треть
#765 пикселей - одна половина

def square(x):
    for _ in range(0,4):
        turtle.fd(x)
        turtle.rt(90)

def ellipsoid_hor(bigrad,littlerad,deg):
    '''
    This function draws an ellips.
    :param bigrad: radius along the OX axis
    :param littlerad: radius along the OY axis
    :param deg: ellipse sector angle (=360 if we want to draw a full ellipse)
    :return: None
    '''
    dx = turtle.xcor()
    dy = turtle.ycor()
    for i in range(deg):
        rad = math.radians(i)
        x = bigrad * math.sin(rad) + dx
        y = -littlerad * math.cos(rad) + littlerad + dy
        turtle.goto(x,y)

def ellipsoid_vert(bigrad,littlerad,deg):
    '''
    This function draws an ellips.
    :param bigrad: radius along the OX axis
    :param littlerad: radius along the OY axis
    :param deg: ellipse sector angle (=360 if we want to draw a full ellipse)
    :return: None
    '''
    dx = turtle.xcor()
    dy = turtle.ycor()
    for i in range(deg):
        rad = math.radians(i)
        y = bigrad * math.sin(rad) + dy
        x = -littlerad * math.cos(rad) + littlerad + dx
        turtle.goto(x,y)

bigrad, littlerad = 60, 30
standard = 80

turtle.goto(-600,5)
turtle.pensize(2)
turtle.fillcolor('Cornflowerblue')
turtle.begin_fill()
turtle.pd()
turtle.pencolor('Cornflowerblue')

turtle.rt(90)
turtle.fd(standard)
turtle.circle(standard//4,90)
turtle.fd(standard)
turtle.pu()
turtle.goto(turtle.xcor() - bigrad,turtle.ycor() - littlerad)
turtle.pd()


ellipsoid_hor(bigrad,littlerad,270)
turtle.rt(180)
turtle.fd(littlerad)
turtle.lt(90)
turtle.fd(bigrad)
turtle.rt(90)
turtle.fd(standard//8)
turtle.rt(90)
turtle.fd(bigrad + 40)
turtle.pu()
turtle.goto(turtle.xcor() + 30,turtle.ycor() - 60)
turtle.pd()

ellipsoid_vert(bigrad,-littlerad,270)
turtle.lt(180)
turtle.fd(standard//8*3)
turtle.lt(90)
turtle.fd(standard//8*3)
turtle.circle(-standard//8*3,90)
turtle.end_fill()
turtle.pu()

turtle.goto(turtle.xcor() + 5,turtle.ycor() + 85)
turtle.pd()
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.pu()
turtle.goto(turtle.xcor() - 5,turtle.ycor() - 85)
turtle.done()