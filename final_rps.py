# This file was created by: Rohan Angelo

'''

Goals:

When a user click on their choice, the computer randomly chooses and displays the result


Sources:

https://www.geeksforgeeks.org/turtle-onclick-function-in-python/


'''
 
# import package

import turtle

from turtle import *

import random

import time

from random import randint

# The os module allows us to access the current directory in order to access assets

import os

print("The current working directory is (getcwd): " + os.getcwd())

print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module

game_folder = os.path.dirname(__file__)

images_folder = os.path.join(game_folder, 'images')


# setup the width and height for the window

WIDTH, HEIGHT = 1000, 400

 

rock_w, rock_h = 256, 280

 

paper_w, paper_h = 256, 204

 

scissors_w, scissors_h = 256, 170

 

# setup the Screen class using the turtle module

screen = turtle.Screen()

screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar

screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")

# canvas object

cv = screen.getcanvas()

# hack to make window not resizable for more reliable coordinates

cv._rootwindow.resizable(False, False)

 
# setup the rock image using the os module as rock_image

rock_image = os.path.join(images_folder, 'rock.gif')

# instantiate (create an instance of) the Turtle class for the rock

rock_instance = turtle.Turtle()

# setup the paper image using the os module as paper_image

paper_image = os.path.join(images_folder, 'paper.gif')

# instantiate (create an instance of) the Turtle class for the paper

paper_instance = turtle.Turtle()

# setup the scissors image using the os module as scissors_image

scissors_image = os.path.join(images_folder, 'scissors.gif')

# instantiate (create an instance of) the Turtle class for the scissors

scissors_instance = turtle.Turtle()

def show_rock(x,y):

    # add the rock image as a shape

    screen.addshape(rock_image)

    # attach the rock_image to the rock_instance

    rock_instance.shape(rock_image)

    # remove the pen option from the rock_instance so it doesn't draw lines when moved

    rock_instance.penup()

    # set the position of the rock_instance

    rock_instance.setpos(x,y)

def show_paper(x,y):

    # add the paper image as a shape

    screen.addshape(paper_image)

    # attach the paper_image to the paper_instance

    paper_instance.shape(paper_image)

    # remove the pen option from the paper_instance so it doesn't draw lines when moved

    paper_instance.penup()

    # set the position of the paper_instance

    paper_instance.setpos(x,y)

def show_scissors(x,y):

    # add the scissors image as a shape

    screen.addshape(scissors_image)

    # attach the scissors_image to the scissors_instance

    scissors_instance.shape(scissors_image)

    # remove the pen option from the scissors_instance so it doesn't draw lines when moved

    scissors_instance.penup()

    # set the position of the scissors_instance

    scissors_instance.setpos(x,y)

# instantiate a turtle for writing text

text = turtle.Turtle()

text.color('Midnight blue')

text.hideturtle()

text.penup()

show_rock(-300, 0)

show_paper(0, 0)

show_scissors(300, 0)

# this function uses and x y value, an obj, and width and height

def collide(x,y,obj,w,h):

    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:

        return True

    else:

        return False
    
# function that passes through wn onlick
text2 = turtle.Turtle()

text2.penup()

text2.color("Dark green")

compchoices = ["Rock" , "Paper" , "Scissors"]

 
def comprandchoose():

    compchose = ""

    compchose = random.choice(compchoices)

    return str(compchose)

 
def clearimages():

    paper_instance.hideturtle()

    rock_instance.hideturtle()

    scissors_instance.hideturtle()

compchose = ""

def mouse_pos(x, y):

    compchose = comprandchoose()

    print("The CPU chose: " + compchose)

    if collide(x,y,rock_instance, rock_w, rock_h):

        print("rock chosen")

        text.clear()

        text.penup()

        text.write("You chose rock.", False, "left", ("Arial", 24, "normal"))

        if compchose == "Rock":

            clearimages()

            text2.penup()

            text2.setpos(160,0)

            text2.write("You both chose rock. There is a tie, try again.", True, "right", ("Arial",16,"normal"))

            rock_instance.showturtle()

            c = rock_instance.clone()

            c.showturtle()

            rock_instance.setpos(-300,0)

            c.setpos(300,0)

        elif compchose == "Paper":

            clearimages()

            text2.penup()

            text2.setpos(155,0)

            text2.write("The computer chose Paper, you lose.", True, "right", ("Arial",16,"normal"))

            rock_instance.showturtle()

            c = paper_instance.clone()

            c.showturtle()

            rock_instance.setpos(-300,0)

            c.setpos(300,0)

        elif compchose == "Scissors":

            clearimages()

            text2.penup()

            text2.setpos(155,0)

            text2.write("The computer chose Scissors, you win!", True, "right", ("Arial",16,"normal"))

            rock_instance.showturtle()

            c = scissors_instance.clone()

            c.showturtle()

            rock_instance.setpos(-300,0)

            c.setpos(300,0)

        # i need the computer to randomly choose...

        # i need to display what the computer chose and communicate winner

    #paper elif

    elif collide(x,y,paper_instance, paper_w, paper_h):

        print("Paper chosen.")

        text.clear()

        text.penup()

        text.write("You chose paper.", False, "left", ("Arial", 24, "normal"))

        clearimages()

        if compchose == "Rock":

            clearimages()

            text2.penup()

            text2.setpos(160,0)

            text2.write("The CPU chose rock, you win!", True, "right", ("Arial",16,"normal"))

            paper_instance.showturtle()

            c = rock_instance.clone()

            c.showturtle()

            paper_instance.setpos(-300,0)

            c.setpos(300,0)

        elif compchose == "Paper":

            clearimages()

            text2.penup()

            text2.setpos(155,0)

            text2.write("You both chose paper, you tie.", True, "right", ("Arial",16,"normal"))

            paper_instance.showturtle()

            c = paper_instance.clone()

            c.showturtle()

            paper_instance.setpos(-300,0)

            c.setpos(300,0)

        elif compchose == "Scissors":

            clearimages()

            text2.penup()

            text2.setpos(155,0)

            text2.write("The computer chose Scissors, you lose!", True, "right", ("Arial",16,"normal"))

            paper_instance.showturtle()

            c = scissors_instance.clone()

            c.showturtle()

            paper_instance.setpos(-300,0)

            c.setpos(300,0)

    elif collide(x,y,scissors_instance, scissors_w, scissors_h):

        print("Scissors chosen.")

        text.clear()

        text.penup()

        text.write("You chose scissors.", False, "left", ("Arial", 24, "normal"))

        clearimages()

        if compchose == "Rock":

            clearimages()

            text2.penup()

            text2.setpos(160,0)

            text2.write("The CPU chose rock, you lose!", True, "right", ("Arial",16,"normal"))

            scissors_instance.showturtle()

            c = rock_instance.clone()

            c.showturtle()

            scissors_instance.setpos(-300,0)

            c.setpos(300,0)

        elif compchose == "Paper":

            clearimages()

            text2.penup()

            text2.setpos(155,0)

            text2.write("The CPU chose paper, you win.", True, "right", ("Arial",16,"normal"))

            scissors_instance.showturtle()

            c = paper_instance.clone()

            c.showturtle()

            scissors_instance.setpos(-300,0)

            c.setpos(300,0)

        elif compchose == "Scissors":

            clearimages()

            text2.penup()

            text2.setpos(155,0)

            text2.write("The computer chose Scissors, you tied!", True, "right", ("Arial",16,"normal"))

            scissors_instance.showturtle()

            c = scissors_instance.clone()

            c.showturtle()

            scissors_instance.setpos(-300,0)

            c.setpos(300,0)

    elif collide(x,y,scissors_instance, scissors_w, scissors_h):

        print("scissors")

    else:

        print("player chose non-gui")
## after chosen

text.penup()

text.setpos(0,150)
# user this to get mouse position

screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()