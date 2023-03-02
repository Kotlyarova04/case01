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
    penMsize(5)  # размер пера
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
