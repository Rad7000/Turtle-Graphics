#A weird sun-like figure

import tkinter
import turtle

from turtle import *
color('green', 'brown')
begin_fill()
while True:
    forward(200)
    left(300)
    right(200)
    backward(100)
    speed(10)
    if abs(pos()) < 1:
        break
end_fill()
done()
