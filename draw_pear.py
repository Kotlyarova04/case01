from turtle import *
speed(15)
color("greenyellow", "yellow")  # цвет рисования и цвет заливки
bgcolor("orange")       # цвет фона
pensize(5)             # размер пера
begin_fill()           # начало заливки
pu()
goto(-3, 70)
pd()                   # опустить перо
rt(0)                # идти вперед
fd(31)                # повернуть вправо на угол
rt(50)
fd(50)
rt(40)
fd(60)
lt(45)
fd(50)
rt(45)
fd(30)
lt(45)
fd(50)
rt(45)
fd(70)
rt(60)
fd(80)
rt(30)
fd(120)
rt(30)
fd(80)
rt(60)
fd(70)
rt(45)
fd(50)
lt(45)
fd(30)
rt(45)
fd(50)
lt(45)
fd(60)
rt(40)
fd(50)
rt(50)
fd(22)
end_fill()
pu()


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
    goto(x, y)
    color(pencolour, fillcolor)
    pensize(pensizee)
    begin_fill()
    pd()
    lt(20)
    for i in range(2):
        fd(a)
        rt(60)
        fd(b)
        rt(120)
    end_fill()
    pu()
    setheading(0)


def rectangle(x, y, a, b, fillcolor, pensizee, pencolour):
    """


    Function for drawing triangle.
    :param x: first coordinate
    :param y:
    :param a:
    :param fillcolor:
    :param pensizee:
    :param pencolour:
    :return:


    """
    goto(x, y)
    color(pencolour, fillcolor)
    pensize(pensizee)
    begin_fill()
    pd()
    for i in range(2):
        fd(a)
        lt(90)
        fd(b)
        lt(90)
    end_fill()
    pu()
    setheading(0)


def circlee(x, y, pensizee, r, pencolor, fillcolor):
    """

    :param pensizee:
    :param r:
    :param pencolor:
    :param fillcolor:
    :return:


    """
    goto(x,y)
    pd()
    rt(45)
    pensize(pensizee)
    color(pencolor, fillcolor)
    begin_fill()
    for i in range(2):
        circle(r, 90)
        circle(r, 90)
        pu()
    end_fill()

def smile(x, y, pensizee, r, pencolor):


    '''
    :param x:
    :param y:
    :param pensizee:
    :param r:
    :param pencolor:
    :return:
    '''

    goto(x, y)
    pd()
    pensize(pensizee)
    color(pencolor)
    for i in range(2):
        circle(r, 90)


rectangle(2, 70, 5, 55, "brown", 3, "brown")
rhomb(8, 120, 60, 60, "green", 3, "green")
circlee(-30, -20, 1, 10, "black", "black")
circlee(19, -12, 1, 10, "black", "black")
smile(-30, -80, 3, 35, "black")
mainloop()
