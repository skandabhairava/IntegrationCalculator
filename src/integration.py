#!/usr/bin/env python3
from squareroot import Squareroot
import turtle
import math

# CONSTANTS
AREA_Q1_Q2 = 0
AREA_Q3_Q4 = 0

NEGATIVE = True

def draw_rect(turtle: turtle.Turtle, height: float, width: float):
    turtle.begin_fill()
    turtle.seth(0)
    turn = turtle.left if height >= 0 else turtle.right
    height = height if height >= 0 else height * -1
    for _ in range(2):
        turtle.forward(width)
        turn(90)
        turtle.forward(height)
        turn(90)
    turtle.end_fill()
    turtle.forward(width)

def draw_func(function, upper_limit, lower_limit, dx, turtle_local: turtle.Turtle, zoom):
    turtle_local.penup()
    try:
        initial = function(-1000)
    except ZeroDivisionError:
        raise
    if isinstance(initial, Squareroot):
        try:
            initial = max(initial.items)
        except ValueError:
            initial = 0
    turtle_local.goto(-1000, initial)

    turtle_local.pendown()
    range_func = (-500, 500)
    x_pos = range_func[0]

    for x_pos in range(-500, 500):
        try:
            result = function(x_pos/zoom)
        except ZeroDivisionError:
            result = 0
        if isinstance(result, Squareroot):
            for y in result.items:
                turtle_local.penup()
                turtle_local.goto(x_pos, y*zoom)
                turtle_local.pendown()
                turtle_local.dot(2)

            continue
        turtle_local.goto(x_pos, result*zoom)
        turtle_local.dot(1)

    turtle_local.penup()
    turtle_local.goto(lower_limit, 0)
    turtle_local.color("blue")

    while ((x_pos:=(turtle_local.pos()[0])) + dx)/zoom <= upper_limit:
        try:
            result = function(x_pos/zoom)
        except ZeroDivisionError:
            result = 0
        except OverflowError:
            result = 1000

        if isinstance(result, Squareroot):
            try:
                result = max(result.items)
            except ValueError:
                result = 0

        draw_rect(turtle_local, result*zoom, dx)

def calc(function, upper_limit, lower_limit, dx):
    global AREA_Q1_Q2, AREA_Q3_Q4
    x_pos = lower_limit

    while (x_pos + dx) <= upper_limit:
        try:
            result = function(x_pos)
        except ZeroDivisionError:
            raise
        except OverflowError:
            result = 5000

        if isinstance(result, Squareroot):
            try:
                result = max(result.items)
            except ValueError:
                result = 0

        if result >= 0:
            AREA_Q1_Q2 += (dx*result)
        else:
            AREA_Q3_Q4 += (dx*result) * -1

        x_pos += dx

def main(function, upper_limit, lower_limit, dx, dx_calc, zoom):

    if (dx == 0) or (upper_limit <= lower_limit):
        return

    integration = turtle.Turtle()
    screen = turtle.Screen()

    turtle.color("black", "black")
    screen.screensize(5000, 5000)

    axis = turtle.Turtle()
    axis.color("red3")
    for i in range(-1, 2):
        axis.goto(i*3000, 0)
    axis.home()
    for i in range(-1, 2):
        axis.goto(0, i*3000)

    axis.shapesize(0.1, 5)
    axis.shape("square")
    axis.pu()

    draw_func(function, upper_limit, lower_limit, dx, integration, zoom)
    calc(function, upper_limit, lower_limit, dx_calc)

    if NEGATIVE:
        print(f"Total Area: {AREA_Q1_Q2 - AREA_Q3_Q4} which is approx. ~{round(AREA_Q1_Q2 - AREA_Q3_Q4)}")
        #print(AREA_Q1_Q2, AREA_Q3_Q4)
    else:
        print(f"Total Area: {AREA_Q1_Q2 + AREA_Q3_Q4}")
        #print(AREA_Q1_Q2, AREA_Q3_Q4)

if __name__ == "__main__":
    turtle.tracer(0)
    turtle.speed(10000)

    zoom = 25

    #integration_function = lambda x: Squareroot(100 - (x**2))
    #upper_limit = 50
    
    integration_function = lambda x: (math.sin(x) + math.cos(x))/(math.sin(x)**4 + math.cos(x)**4)
    upper_limit = math.pi*2

    #integration_function = lambda x: x
    #upper_limit = 20

    lower_limit = 0
    dx_size_graph = 0.01
    dx_calc = 0.0001

    main(integration_function, upper_limit, lower_limit, dx_size_graph, dx_calc, zoom)
    turtle.exitonclick()