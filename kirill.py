import turtle as t
import draw_pear as d
import math
if __name__=='__main__':
    t.setup(width=1.0, height=1.0)
    t.speed(50)
    t.pensize(5)
    t.pu()
    t.goto(-255,-400)
    t.pd()
    t.lt(90)
    t.fd(820)
    t.pu()
    t.goto(255,-400)
    t.pd()
    t.fd(820)
    t.setheading(0)
    t.pu()

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
    dx = t.xcor()
    dy = t.ycor()
    for i in range(deg):
        rad = math.radians(i)
        x = bigrad * math.sin(rad) + dx
        y = -littlerad * math.cos(rad) + littlerad + dy
        t.goto(x,y)

def pattern(change1, change2, change3, change4, change5, standard):
    '''
    This function draws half of the Python logo, and with opposite (in sign) change-arguments, draws the other half.
    :param change1: x-radius of ellipse
    :param change2: y-radius of ellipse
    :param change3: x-diameter of ellipse
    :param change4: x-adjustment for drawing a circle
    :param change5: y-adjustment for drawing a circle
    :param standard: length of the center line before turns
    :return: None
    '''

    t.begin_fill()
    t.pd()
    t.fd(standard)
    t.circle(standard//4,90)
    t.fd(standard)
    t.pu()
    t.goto(t.xcor() - change1, t.ycor() - change2)
    t.pd()

    ellipsoid(change1,change2,270)
    t.rt(180)
    t.fd(abs(change2))
    t.lt(90)
    t.fd(abs(change1))
    t.rt(90)
    t.fd(standard//8)
    t.rt(90)
    t.fd(abs(change1) + 40)
    t.pu()
    t.goto(t.xcor(),t.ycor() - change3)
    t.pd()

    ellipsoid(change2,change1,360)
    t.lt(180)
    t.fd(standard//8*3)
    t.lt(90)
    t.fd(standard//8*3)
    t.circle(-standard//8*3,90)
    t.end_fill()
    t.pu()

    t.goto(t.xcor() + change4,t.ycor() + change5)
    t.pd()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.pu()

if __name__=='__main__':
    change1, change2, change3, change4, change5, standard = 60, 30, 120, 5, 85, 80

    t.goto(-550,5)
    t.pensize(2)
    t.pencolor('Cornflowerblue')
    t.fillcolor('Cornflowerblue')

    pattern(change1, change2, change3, change4, change5, standard)
    t.goto(t.xcor() + 75, t.ycor() - 95)
    t.setheading(180)

    t.pencolor('DarkGoldenrod1')
    t.fillcolor('DarkGoldenrod1')
    pattern(-change1, -change2, -change3, -change4, -change5, standard)
    t.setheading(0)
    t.pu()

    # letter P
    d.rectangle(-650, 200, 8, 60, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
    d.letter(-642, 220, 1, 20, 'DarkGoldenrod1', 'DarkGoldenrod1')
    d.letter(-642, 230, 1, 10, 'white', 'white')

    # letter Y
    d.rectangle(-596, 200, 8, 30, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
    t.lt(30)
    d.rectangle(-588, 230, -8, 35, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
    t.rt(30)
    d.rectangle(-596, 230, 8, 35, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')

    # letter T
    d.rectangle(-542, 200, 8, 60, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
    t.lt(90)
    d.rectangle(-518, 260, -8, 40, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')

    # letter H
    d.rectangle(-504, 200, 8, 60, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
    d.rectangle(-472, 200, 8, 60, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
    t.lt(90)
    d.rectangle(-464, 234, -8, 40, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')

    # letter O
    t.goto(-430, 200)
    t.begin_fill()
    t.pd()
    ellipsoid(20, 30, 360)
    t.end_fill()
    t.goto(-430, 210)
    t.fillcolor('white')
    t.begin_fill()
    ellipsoid(10, 20, 360)
    t.end_fill()
    t.pu()

    # letter N
    d.rectangle(-395, 200, 8, 60, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
    d.rectangle(-363, 200, 8, 60, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
    t.begin_fill()
    t.pd()
    t.goto(-387, 244)
    t.goto(-387, 260)
    t.goto(-363, 216)
    t.goto(-363, 200)
    t.end_fill()
    t.pu()
    t.done()