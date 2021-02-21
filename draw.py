from turtle import *
from time import sleep
screen=Screen()
speed(0)

screen.bgcolor("black")
colormode(255)
red=(223, 35, 35); green=(75, 183, 75); yellow=(252, 210, 9); blue=(86, 146, 195)
r=120
speed(0)
seth(-150)
up()

#Warna merah
color(red)
begin_fill()
fd(r)
down()
right(90)
circle(-r, 120)
fd(r*3**.5)
left(120)
circle(2*r, 120)
left(60)
fd(r*3**.5)
end_fill()

#Warna Hijau
left(180)
color(green)
begin_fill()
fd(r*3**.5)
left(120)
circle(2*r, 120)
left(60)
fd(r*3**.5)
left(180)
circle(-r, 120)
end_fill()

#Warna Kuning
left(180)
circle(r, 120)
color(yellow)
begin_fill()
circle(r, 120)
right(180)
fd(r*3**.5)
right(60)
circle(-2*r, 120)
right(120)
fd(r*3**.5)
end_fill()

#Warna Biru
up()
left(90)
fd(r/20)
seth(60)
color(blue)
down()
begin_fill()
circle(distance(0,0))
end_fill()
ht()
sleep(5)

#Done
screen=getscreen()

clear()
ht()
up()
goto(-300, 0)

st()
down()
goto(0.0)
color("yellow")
write("@esone.s1", font=("Arial", 30, "bold"))
goto(160, 0)