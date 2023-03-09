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

def ellipsoid(bigrad,littlerad,deg):
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

def pattern(change1, change2, change3, change4, change5, standard):
    '''
    :param change1:
    :param change2:
    :param change3:
    :param change4:
    :param change5:
    :param standard:
    :return:
    '''

    turtle.begin_fill()
    turtle.pd()
    turtle.rt(90)
    turtle.fd(standard)
    turtle.circle(standard//4,90)
    turtle.fd(standard)
    turtle.pu()
    turtle.goto(turtle.xcor() - change1, turtle.ycor() - change2)
    turtle.pd()

    ellipsoid(change1,change2,270)
    turtle.rt(180)
    turtle.fd(abs(change2))
    turtle.lt(90)
    turtle.fd(abs(change1))
    turtle.rt(90)
    turtle.fd(standard//8)
    turtle.rt(90)
    turtle.fd(abs(change1) + 40)
    turtle.pu()
    turtle.goto(turtle.xcor(),turtle.ycor() - change3)     #120
    turtle.pd()

    ellipsoid(change2,change1,360)
    turtle.lt(180)
    turtle.fd(standard//8*3)
    turtle.lt(90)
    turtle.fd(standard//8*3)
    turtle.circle(-standard//8*3,90)
    turtle.end_fill()
    turtle.pu()

    turtle.goto(turtle.xcor() + change4,turtle.ycor() + change5)    #change4, change5 = 5, 85
    turtle.pd()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.pu()

change1, change2, change3, change4, change5, standard = 60, 30, 120, 5, 85, 80

turtle.goto(-550,5)
turtle.pensize(2)
turtle.pencolor('Cornflowerblue')
turtle.fillcolor('Cornflowerblue')

pattern(change1, change2, change3, change4, change5, standard)
turtle.goto(turtle.xcor() + 75, turtle.ycor() - 95)
turtle.rt(90)

turtle.pencolor('DarkGoldenrod1')
turtle.fillcolor('DarkGoldenrod1')
pattern(-change1, -change2, -change3, -change4, -change5, standard)
turtle.done()