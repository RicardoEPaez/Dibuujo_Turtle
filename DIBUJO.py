#Importacion de hacer grafics en pyhton con la libreria turtle
import turtle
turtle.bgcolor("Black")
squary = turtle.Turtle()
squary.speed(50)
for i in range(160):
    for color in ["red", "blue", "yellow", "green"]:
        squary.pencolor(color)
        squary.forward(i)
        squary.left(60)
        squary.right(12)