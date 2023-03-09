import turtle as t

t.speed(15)
if __name__ == '__main__':
    t.setup(width=1.0, height=1.0)
    t.pensize(5)
    t.pu()
    t.goto(-255, -400)
    t.pd()
    t.lt(90)
    t.fd(820)
    t.pu()
    t.goto(255, -400)
    t.pd()
    t.fd(820)
    t.pu()
t.setheading(0)
t.color("greenyellow", "yellow")  # цвет рисования и цвет заливки
t.pensize(5)  # размер пера
t.begin_fill()  # начало заливки
t.pu()
t.goto(-3, 70)
t.pd()  # опустить перо
t.rt(0)  # идти вперед
t.fd(31)  # повернуть вправо на угол
t.rt(50)
t.fd(50)
t.rt(40)
t.fd(60)
t.lt(45)
t.fd(50)
t.rt(45)
t.fd(30)
t.lt(45)
t.fd(50)
t.rt(45)
t.fd(70)
t.rt(60)
t.fd(80)
t.rt(30)
t.fd(120)
t.rt(30)
t.fd(80)
t.rt(60)
t.fd(70)
t.rt(45)
t.fd(50)
t.lt(45)
t.fd(30)
t.rt(45)
t.fd(50)
t.lt(45)
t.fd(60)
t.rt(40)
t.fd(50)
t.rt(50)
t.fd(22)
t.end_fill()
t.pu()


def rhomb(x, y, a, b, fillcolor, pensizee, pencolour):
    """
    :param x:
    :param y:
    :param a:
    :param b:
    :param fillcolor:
    :param pensizee:
    :param pencolour:
    :return:
    """
    t.goto(x, y)
    t.color(pencolour, fillcolor)
    t.pensize(pensizee)
    t.begin_fill()
    t.pd()
    t.lt(20)
    for i in range(2):
        t.fd(a)
        t.rt(60)
        t.fd(b)
        t.rt(120)
    t.end_fill()
    t.pu()
    t.setheading(0)


def rectangle(x, y, a, b, fillcolor, pensizee, pencolour):
    """
    Function for drawing retangle.
    :param x: first coordinate
    :param y:
    :param a:
    :param fillcolor:
    :param pensizee:
    :param pencolour:
    :return:
    """
    t.goto(x, y)
    t.color(pencolour, fillcolor)
    t.pensize(pensizee)
    t.begin_fill()
    t.pd()
    for i in range(2):
        t.fd(a)
        t.lt(90)
        t.fd(b)
        t.lt(90)
    t.end_fill()
    t.pu()
    t.setheading(0)


def circlee(x, y, pensizee, r, pencolor, fillcolor):
    """

    :param y:
    :param x:
    :param pensizee:
    :param r:
    :param pencolor:
    :param fillcolor:
    :return:


    """
    t.goto(x, y)
    t.pd()
    t.rt(45)
    t.pensize(pensizee)
    t.color(pencolor, fillcolor)
    t.begin_fill()
    for i in range(2):
        t.circle(r, 90)
        t.circle(r, 90)
        t.pu()
    t.end_fill()


def smile(x, y, pensizee, r, pencolor):
    '''
    :param x:
    :param y:
    :param pensizee:
    :param r:
    :param pencolor:
    :return:
    '''

    t.goto(x, y)
    t.pd()
    t.pensize(pensizee)
    t.color(pencolor)
    for i in range(2):
        t.circle(r, 90)
    t.pu()


def letter(x, y, pensizee, r, pencolor, fillcolor):
    '''
    :param x:
    :param y:
    :param pensizee:
    :param r:
    :param pencolor:
    :return:
    '''

    t.goto(x, y)
    t.pd()
    t.pensize(pensizee)
    t.color(pencolor, fillcolor)
    t.begin_fill()
    for i in range(2):
        t.circle(r, 90)
    t.end_fill()
    t.pu()
    t.lt(180)

rectangle(2, 70, 5, 55, "brown", 3, "brown")
rhomb(8, 120, 60, 60, "green", 3, "green")
circlee(-30, -20, 1, 10, "black", "black")
circlee(19, -12, 1, 10, "black", "black")
smile(-13, -90, 3, 15, "black")
circlee(55, -55, 2, 5, "pink", 'pink')
circlee(-45, -55, 2, 5, "pink", 'pink')
rectangle(-150, 200, 8, 60, "goldenrod", 5, "goldenrod")
letter(-140, 215, 1, 23, "goldenrod", "goldenrod")
letter(-140, 230, 1, 10, "white", "white")
rectangle(-100, 200, 8, 55, "goldenrod", 5, "goldenrod")
rectangle(-100, 200, 50, 8, "goldenrod", 5, "goldenrod")
rectangle(-100, 225, 50, 8, "goldenrod", 5, "goldenrod")
rectangle(-100, 250, 50, 8, "goldenrod", 5, "goldenrod")

t.mainloop()
