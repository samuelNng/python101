import turtle
from turtle import *
from random import randint

john = Turtle()
bob  = Turtle()
sally  = Turtle()

john.color('red')
bob.color('green')
sally.color('blue')

john.penup()
john.goto(-160, 100)
john.pendown

bob.penup()
bob.goto(-160, 70)
bob.pendown

sally.penup()
sally.goto(-160, 100)
sally.pendown

for movement in range (100):
    john.forward(randint(1,5))
    bob.forward(randint(1,5))
    sally.forward(randint(1,5))

input("press Enter")