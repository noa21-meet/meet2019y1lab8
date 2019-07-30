import turtle
turtle.color('pink')
turtle.pensize(10)
turtle.goto(0,0)

def up():
    print("You pressed the up key.")
    turtle.goto(turtle.xcor(), turtle.ycor() + 50)


turtle.onkey(up, "Up")

turtle.listen()

def down():
    print("You pressed the dowm key.")
    turtle.goto(turtle.xcor(), turtle.ycor() - 50)
    
turtle.onkey(down, "Down")

turtle.listen()

def right():
    print("You pressed the right key.")
    turtle.goto(turtle.xcor() +50, turtle.ycor())


turtle.onkey(right, "Right")

turtle.listen()

def left():
    print("You pressed the left key.")
    turtle.goto(turtle.xcor() - 50, turtle.ycor())


turtle.onkey(left, "Left")

turtle.listen()

def space():
    print("You pressed the space key.")
    turtle.penup()


turtle.onkey(space, "A")

turtle.listen()

    
turtle.mainloop()


