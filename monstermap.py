#Lionel Lynch
#Monstermap.py
#Ask for a horizontal multiplier, a vertical multiplier, 
#and a constant from the user (as floats, or real numbers)

def map(horiz, vert, const):
    import turtle

    #Turtle attributes
    turtle = turtle.Turtle()
    turtle.fillcolor("red")
    turtle.speed(100)

    #loop
    for i in range(10):
        for j in range(8):
            turtle.goto(25 * i, -25 * j)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle((horiz * i) + (vert * j) + const)
            turtle.end_fill()
            turtle.penup()

map(-1, 0.5 ,5) 