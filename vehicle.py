#Lionel Lynch
#vehicle.py
#using python tutrle module draw a vehicle 

import turtle

from numpy import shape, square

turtle.speed(10)

#propeler: attributes
turtle.pensize(20)

#upper right propeler
turtle.penup()
turtle.forward(200)
turtle.pendown()
turtle.circle(50)

#upper left propeler
turtle.penup()
turtle.backward(200)
turtle.pendown()
turtle.circle(50)

#bottom left propeler
turtle.penup()
turtle.backward(50)
turtle.right(90)
turtle.forward(100)
turtle.pendown()
turtle.circle(50)

#bottom right propeler
turtle.penup()
turtle.forward(50)
turtle.left(90)
turtle.forward(250)
turtle.pendown()
turtle.circle(50)

#center
turtle.left(90)
turtle.penup()
turtle.forward(130)
turtle.left(90)
turtle.forward(100)
turtle.pendown()
turtle.circle(10)

#frame: attributes
turtle.pensize(7)

#frame: bottom left & upper right
turtle.left(90)
turtle.penup()
turtle.forward(10)
turtle.right(55)
turtle.pendown()
turtle.forward(70)
turtle.left(180)  
turtle.forward(155)

#frame: upper left & bottom right
turtle.penup()
turtle.right(180)
turtle.forward(85)
turtle.right(75)
turtle.pendown()
turtle.forward(80)
turtle.right(180)
turtle.forward(155)

#cage: attributes
turtle.pensize(3)

#cage
turtle.right(180)
turtle.penup()
turtle.forward(38)
turtle.right(50)
turtle.pendown()
turtle.forward(45)
turtle.left(90)
turtle.penup()
turtle.forward(55)
turtle.left(90)
turtle.pendown()
turtle.forward(43)

turtle.left(130)
turtle.penup()
turtle.forward(35)



#EXIT
input("Press any key to exit ...")