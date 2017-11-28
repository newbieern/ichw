
# coding: utf-8

# In[2]:


"""Planets.py: A python that simulates planetary operations.

__author__ = "KowPuErn"
__pkuid__  = "1700094617"
__email__  = "newbieern2@hotmail.com"
"""

import math
import turtle


def drawCircle(a,t,r):
    for i in range(a):
        t.forward((2*math.pi*r)/180)
        t.left(360/180)


wn=turtle.Screen()
wn.bgcolor("black")


#O'SoleMio
sun=turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.stamp()



def planet(a,p,speed,r):
    p.speed(speed)
    p.shape("circle")
    p.pensize("2")
    drawCircle(a,p,r)

def move(p,r):
    p.up()
    p.goto(0,-r)
    p.pendown()
    

    
mercury=turtle.Turtle()
venus=turtle.Turtle()
earth=turtle.Turtle()
mars=turtle.Turtle()
jupiter=turtle.Turtle()
saturn=turtle.Turtle()



def mercury_run():
    mercury.color("blue")
    planet(100,mercury,400,60)

def venus_run():
    venus.color("red")
    planet(77,venus,30,100)

def earth_run():
    earth.color("lightgreen")
    planet(64,earth,20,130)

def mars_run():
    mars.color("orange")
    planet(51,mars,4,170)

def jupiter_run():
    jupiter.color("cyan")
    planet(40,jupiter,3,220)

def saturn_run():
    saturn.color("yellow")
    planet(28,saturn,2,280)


def main():

    move(mercury,60)
    move(venus,100)
    move(earth,130)
    move(mars,170)
    move(jupiter,220)
    move(saturn,280)

    mercury_run()
    venus_run()
    earth_run()
    mars_run()
    jupiter_run()
    saturn_run()


if __name__ == '__main__':
    main()


