from turtle import Turtle, Screen
import turtle


tim =  Turtle()
screen = Screen()

turtle.listen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_right():   
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

turtle.onkey(move_forward,"w")
turtle.onkey(move_backward,"s")
turtle.onkey(turn_right,"d")
turtle.onkey(turn_left,"a")
turtle.onkey(clear,"c")

screen.exitonclick()