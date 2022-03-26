#A cool looking figure

import tkinter
import turtle

from turtle import *
color('purple', 'pink')
begin_fill()
while True:
    forward(10)
    right(10)
    forward(20)
    right(20)
    forward(30)
    right(30)
    forward(40)
    right(40)
    forward(50)
    right(50)
    forward(60)
    right(60)
    forward(70)
    right(70)
    forward(80)
    right(80)
    forward(90)
    right(90)
    forward(100)
    right(100)
    forward(110)
    right(110)
    if abs(pos()) < 1:
        break
end_fill()
done()
