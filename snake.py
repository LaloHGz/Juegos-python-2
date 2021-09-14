"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""
from random import choice
from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ['black','green','yellow','blue','brown','orange','purple']
colorbody = choice(colors)
colorfood = choice(colors)
while(colorbody == colorfood):
            colorfood = choice(colors)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
    "La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana"
    food.x = randrange(-18, 18) * 10
    food.y = randrange(-18, 18) * 10


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)


    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    
    global colorbody
    global colorfood

    if head == food:
        print('Snake:', len(snake))
        
        food.x = randrange(-18, 18) * 10
        food.y = randrange(-18, 18) * 10

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorbody)

    square(food.x, food.y, 9, colorfood)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()