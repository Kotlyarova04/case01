'''
Dreamteam:
Kotlyarova Polina
Rafaevich Vita
Leonov Kirill
'''

# import reguired modules
import turtle as t
import kirill as k
import draw_pear as d
import math

# divide into 3 parts
t.setup(width=1.0, height=1.0)
t.speed(0)
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

# Part of Kirill
change1, change2, change3, change4, change5, standard = 60, 30, 120, 5, 85, 80

t.goto(-550,5)
t.pensize(2)
t.pencolor('Cornflowerblue')
t.fillcolor('Cornflowerblue')

k.pattern(change1, change2, change3, change4, change5, standard)
t.goto(t.xcor() + 75, t.ycor() - 95)
t.setheading(180)

t.pencolor('DarkGoldenrod1')
t.fillcolor('DarkGoldenrod1')
k.pattern(-change1, -change2, -change3, -change4, -change5, standard)
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
k.ellipsoid(20, 30, 360)
t.end_fill()
t.goto(-430, 210)
t.fillcolor('white')
t.begin_fill()
k.ellipsoid(10, 20, 360)
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

# Part of Polina
d.pear(-3, 70, 5, "yellowgreen", "greenyellow")
d.rectangle(0, 70, 5, 55, "brown", 3, "brown")
d.rhomb(6, 120, 60, 60, "green", 3, "green")
d.circlee(-30, -20, 2, 10, "black", "black")
d.circlee(19, -12, 2, 10, "black", "black")
d.smile(-13, -90, 3, 15, "black")
d.circlee(55, -55, 2, 5, "pink", 'pink')
d.circlee(-45, -55, 2, 5, "pink", 'pink')
d.rectangle(-130, 200, 8, 60, "goldenrod", 5, "goldenrod")
d.letter(-120, 215, 1, 23, "goldenrod", "goldenrod")
d.letter(-120, 230, 1, 10, "white", "white")
d.rectangle(-70, 200, 8, 57, "goldenrod", 5, "goldenrod")
d.rectangle(-70, 200, 45, 8, "goldenrod", 5, "goldenrod")
d.rectangle(-70, 225, 45, 8, "goldenrod", 5, "goldenrod")
d.rectangle(-70, 250, 45, 8, "goldenrod", 5, "goldenrod")
t.setheading(65)
d.rectangle(10, 200, 65, 8, "goldenrod", 5, "goldenrod")
t.setheading(210)
d.rectangle(35, 260, 8, 65, "goldenrod", 5, "goldenrod")
t.setheading(0)
d.rectangle(20, 220, 30, 8, "goldenrod", 5, "goldenrod")
t.setheading(0)
d.rectangle(95, 200, 8, 60, "goldenrod", 5, "goldenrod")
d.letter(105, 220, 1, 21, "goldenrod", "goldenrod")
d.letter(105, 230, 1, 10, "white", "white")
t.setheading(245)
d.rectangle(105, 220, 8, 30, "goldenrod", 5, "goldenrod")
t.mainloop()

# Part of Vita


def draw_pear(x, y, color, border):
    '''

    :param x:
    :param y:
    :param color:
    :param border:
    :return: None
    '''

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