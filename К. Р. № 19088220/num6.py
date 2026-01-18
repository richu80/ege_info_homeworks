from turtle import *

tracer(0)
screensize(10000, 10000)
m = 40
lt(90)

for i in range(6):
    fd(13*m)
    rt(120)
up()

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*m, y*m)
        dot(3, 'red')

update()
exitonclick()