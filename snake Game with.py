from turtle import *
from random import randrange
from freegames import square, vector

# Initialize variables
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
speed = 100
paused = False

def change(x, y):
    """Change snake direction."""
    if (aim.x, aim.y) != (-x, -y):  # Prevent reversing direction
        aim.x = x
        aim.y = y

def toggle_pause():
    """Pause or resume the game."""
    global paused
    paused = not paused
    if not paused:
        move()

def inside(head):
    """Return True if head inside boundaries."""
    return -200 <= head.x <= 190 and -200 <= head.y <= 190

def wrap_around(head):
    """Wrap snake around screen edges."""
    if head.x > 190:
        head.x = -200
    if head.x < -200:
        head.x = 190
    if head.y > 190:
        head.y = -200
    if head.y < -200:
        head.y = 190

def move_food():
    """Move food to a new random location."""
    food.x = randrange(-15, 15) * 10
    food.y = randrange(-15, 15) * 10

def move():
    """Move snake forward one segment."""
    global speed
    if paused:
        return
    
    head = snake[-1].copy()
    head.move(aim)
    wrap_around(head)
    
    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    
    snake.append(head)
    
    if head == food:
        print('Snake:', len(snake))
        move_food()
        speed = max(50, speed - 2)  # Increase speed
    else:
        snake.pop(0)
    
    clear()
    for body in snake:
        square(body.x, body.y, 9, 'black')
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, speed)

# Setup the game screen
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Key bindings
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
onkey(toggle_pause, 'space')

move()
done()
