import turtle
import time

# Creamos la tortuga que va a ser un punto que se va a mover con instruciones

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=800, height=600)
t.speed(1)
t.color("red")

time.sleep(2)
# El guion abajo significa que no se va a utilizar esos valores.
for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.down()