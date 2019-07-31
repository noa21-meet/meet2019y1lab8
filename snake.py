import turtle
import random
from pygame import mixer


turtle.tracer(1,0)
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
turtle.register_shape("pic2.gif")
snake = turtle.clone()
snake.shape("pic2.gif")

turtle.hideturtle()
def score():
    turtle.write("GAME OVER! your score is {}".format(len(stamp_list)- START_LENGTH), align = "center", font = ("Arial" , 20, "normal"))
    quit()        
def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos)

    snake_stamp=snake.stamp()

    stamp_list.append(snake_stamp)

for i in range(0, START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE
    snake.goto(x_pos, y_pos)
    new_stamp()

def remove_tail():
    old_stamp = stamp_list.pop(0) 
    snake.clearstamp(old_stamp) 
    pos_list.pop(0) 
snake.direction = None
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    snake.direction="Up"
    print("You pressed the up key!")

def down():
    snake.direction="Down"
    print("You pressed the down key!")

def right():
    snake.direction="Right" 
    print("You pressed the right key!")

def left():
    snake.direction="Left" 
    print("You pressed the left key!")

turtle.onkeypress(up, "Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")

turtle.listen()

turtle.register_shape("pic1.gif")
food = turtle.clone()
food.shape("pic1.gif") 
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
food.penup()

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    stamp = food.stamp()
    food_stamps.append(stamp)

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
    elif snake.direction=="Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved up")
    elif snake.direction=="Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
    new_stamp()
    remove_tail()
    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         score()
    elif new_x_pos <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         score()
    elif new_y_pos >= UP_EDGE:
         print("You hit the up edge! Game over!")
         score()
    elif new_y_pos <= DOWN_EDGE:
         print("You hit the down edge! Game over!")
         score()
         
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_index]) 
        food_pos.pop(food_index) 
        food_stamps.pop(food_index) 
        new_stamp()
        print("You have eaten the food!")
    print("The position list is ", pos_list)
    print("-----------------The snake position is ", snake.pos())
    #if snake.pos() in pos_list[0:-1]:
    s_pos_list = set(pos_list)
    if len(s_pos_list) != len(pos_list):
        print("You ate yourself")
        score()
        
        
    if len(food_stamps) <= 6 :
            make_food()
        
    turtle.ontimer(move_snake(),TIME_STEP)


def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food_stamps.append(food.stamp())

    


move_snake()
   

turtle.mainloop()
