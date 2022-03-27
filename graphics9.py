#An interesing figure

import tkinter
import turtle

from turtle import *
color('orange', 'yellow')
begin_fill()
while True:
    forward(90)
    backward(90)
    right(100)
    left(100)
    backward(90)
    left(100)
    right(100)
    forward(90)
    left(100)
    backward(90)
    right(100)
    backward(90)
    left(100)
    speed(10)
    if abs(pos()) < 1:
        break
end_fill()
done()
