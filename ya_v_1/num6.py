from turtle import *
tracer(0)
screensize(10000, 10000)
m = 35
lt(90)

rt(60)
fd(4*m)
rt(120)
for i in range(4):
    fd(3*m)
    rt(240)
    fd(3*m)
    rt(120)
fd(4*m)
rt(90)
fd(8*(3**(0.5))*m)
rt(90)
fd(8*m)
up()

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*m, y*m)
        dot(3, 'blue')

update()
exitonclick()

#38
