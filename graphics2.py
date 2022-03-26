#A spikey circle

import tkinter
import turtle

from turtle import *
color('Red', 'orange')
begin_fill()
while True:
    forward(40)
    left(30)
    right(20)
    backward(10)
    speed(10)
    if abs(pos()) < 1:
        break
end_fill()
done()
