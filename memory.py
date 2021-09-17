"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

"""

from random import *
from turtle import *
from typing import Counter

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
tiles = list(range('Z'))*2
state = {'mark': None}
hide = [True] * 64

sum  = 0
aux = 0


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    global sum, aux
    sum += 1
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        aux += 1
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None



def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()

        "Centrar el dígito en el cuadrado"
        if tiles[mark] < 10:
            goto(x + 15,y)
        else:
            goto(x + 5, y)
        
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    "Cantidad de taps, juego terminado, detecta que todos los cuadrados se han destapado"
    if aux == 32:
        goto(-160,0)
        color('white')
        write("Cantidad de Taps: ", font=('Arial', 25, 'normal'))
        goto(110,0)
        write(sum, font=('Arial', 25, 'normal'))
        goto(-140,-50)
        write("Juego Terminado", font=('Arial', 25, 'normal'))
    else:
        update()
        ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()