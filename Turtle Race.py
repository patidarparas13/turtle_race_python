#!/bin/python3
from turtle import *
from random import randint
speed(10)
penup()
goto(-140,140)
for steps in range(15):
  write(steps,align="center")
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
forward(20)
ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()

bob = Turtle()
bob.color('green')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()

jack = Turtle()
jack.color('yellow')
jack.shape('turtle')
jack.penup()
jack.goto(-160,40)
jack.pendown()

Joe = Turtle()
Joe.color('blue')
Joe.shape('turtle')
Joe.penup()
Joe.goto(-160,10)
Joe.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  jack.forward(randint(1,5))
  Joe.forward(randint(1,5))
  
  

  


