from turtle import *
tracer(0)
screensize(10000, 10000)
m = 50
lt(90)
for i in range(12):
    rt(60)
    fd(1*m)
    rt(60)
    fd(1*m)
    rt(270)
up()

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*m, y*m)
        dot(3, 'blue')

update()
exitonclick()

#38