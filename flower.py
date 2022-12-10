import turtle as tur   
import colorsys as cs

tur.setup(900,700)
tur.speed(0)
tur.tracer(10)
tur.width(2)
tur.bgcolor("black")

for J in range(50):
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i/15,J/50,1))
        tur.right(90)
        tur.circle(200-J*4,90)
        tur.left(90)
        tur.circle(200-J*4,90)
        tur.right(180)
        tur.circle(50,24)
tur.hideturtle()
tur.done