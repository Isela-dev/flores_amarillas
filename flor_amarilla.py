import turtle
import random


screen = turtle.Screen()
screen.bgcolor("black")


flor = turtle.Turtle()
flor.speed(20)


def dibujar_flor(x, y):
    flor.penup()
    flor.goto(x, y)
    flor.pendown()
    flor.color("yellow")
    flor.begin_fill()
    
    for _ in range(36):
        flor.circle(50, 60)  
        flor.left(120)
        flor.circle(50, 60)
        flor.left(120)
        flor.left(10)  
    
    flor.end_fill()
    flor.color("brown")
    flor.circle(15)  
    flor.penup()

def animar_flor():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    dibujar_flor(x, y)
    flor.clear()  
    screen.ontimer(animar_flor, 1000)  


animar_flor()
turtle.done()
