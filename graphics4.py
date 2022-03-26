#A weird sun-like figure 2

import tkinter
import turtle

from turtle import *
color('blue', 'light blue')
begin_fill()
while True:
    forward(100)
    left(20)
    right(300)
    backward(40)
    speed(10)
    if abs(pos()) < 1:
        break
end_fill()
done()
