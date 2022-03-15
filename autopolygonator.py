#Lionel Lynch
#autopolygonator.py
#output a polygon usings a turtle based on the number of sides and 
#perimeter given by user

from operator import length_hint
import turtle





def drawPolygon(theTurtle, numSides, length):
        #prompt user for side and length
        numSides = int(input('Enter the # of Sides of the polygon: '))
        length = int(input('Enter the length of the polygon: '))
        
        #formula for polyogonal shapes
        length = (numSides - 2) * 180

        #move turtle to orgin
        theTurtle.penup()
        theTurtle.goto(0,0)
        theTurtle.pendown()

        #user input movement
        theTurtle.forward(numSides)
        theTurtle.forward(length)
    
myScreen = turtle.getscreen()
myTurtle = turtle.Turtle()

drawPolygon(myTurtle, 5, 10)