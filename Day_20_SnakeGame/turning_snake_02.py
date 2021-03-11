from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #make the snake appears to be insync when moving

starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update() #updates the screen
    time.sleep(0.1)
    #This will be changed to set the snake to turn 
    # for seg in segments: 
    #     seg.forward(20)

    for seg_num in range( len(segments) - 1 , 0, -1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(10)

screen.exitonclick()