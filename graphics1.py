#A unique star

import tkinter
import turtle

from turtle import *
color('blue', 'purple')
begin_fill()
while True:
    forward(300)
    left(200)
    right(100)
    speed(10)
    if abs(pos()) < 1:
        break
end_fill()
done()
