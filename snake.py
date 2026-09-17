from random import choice, randrange
from turtle import *
from freegames import square, vector

# Lista de 5 colores permitidos (sin incluir el rojo)
COLORES_DISPONIBLES = ['blue', 'green', 'purple', 'orange', 'brown']

# Elegir colores aleatorios diferentes para la serpiente y la comida al iniciar
color_serpiente = choice(COLORES_DISPONIBLES)
color_comida = choice([c for c in COLORES_DISPONIBLES if c != color_serpiente])

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
  "))Change snake direction."""
  aim.x = x
  aim.y = y


def inside(head):
  """Return True if head inside boundaries."""
  return -200 < head.x < 190 and -200 < head.y < 190


def draw_boundaries():
  """Draw visible walls around the play area."""
  up()
  goto(-200, -200)
  down()
  color('gray')
  width(2)
  for _ in range(4):
    forward(390)
    left(90)
  up()


def move():
  """Move snake forward one segment."""
  head = snake[-1].copy()
  head.move(aim)

  if not inside(head) or head in snake:
    square(head.x, head.y, 9, 'red')
    update()
    return

  snake.append(head)

  if head == food:
    print('Snake:', len(snake))
    food.x = randrange(-15, 15) * 10
    food.y = randrange(-15, 15) * 10
  else:
    snake.pop(0)

  # Mover la comida al azar un paso a la vez sin salir de la ventana
  food_aim = choice(
      [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
  )
  new_food = food.copy()
  new_food.move(food_aim)
  if inside(new_food):
    food.move(food_aim)

  clear()

  # Redibujar las paredes estáticas en cada fotograma
  draw_boundaries()

  for body in snake:
    square(body.x, body.y, 9, color_serpiente)

  square(food.x, food.y, 9, color_comida)
  update()
  ontimer(move, 200)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Dibujar las paredes al iniciar el juego
draw_boundaries()

move()
done()
