'''
Dreamteam:
Kotlyarova Polina
Rafaevich Vita
Leonov Kirill
'''

#divide into 3 parts

import turtle
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
turtle.done()
def triangle(x, y, a, b, angle, color):
    '''
    Function for drawing triangle.
    :param x:
    :param y:
    :param a:
    :param b:
    :param angle:
    :param color:
    :return: None
    '''
    import turtle

    pass


def draw_pear(x, y, color, border):
    '''

    :param x:
    :param y:
    :param color:
    :param border:
    :return: None
    '''
    from turtle import *
    color("greenyellow", "yellow")  # цвет рисования и цвет заливки
    bgcolor("blue")  # цвет фона
    pensize(5)  # размер пера
    begin_fill()  # начало заливки
    pd()  # опустить перо
    fd(100)  # идти вперед
    rt(90)  # повернуть вправо на угол
    fd(100)
    rt(90)
    fd(100)
    rt(90)
    fd(100)
    rt(90)

    pass


def draw_cat():
    pass


def main():
    '''
    Maim function.
    :return:
    '''
    draw_cat()
    draw_dog()


if __name__ == '__main__':
    main()