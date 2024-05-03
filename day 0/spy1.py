from turtle import * 
width(5)

#we want to paint a hause

color("blue") 
begin_fill()
speed(60000000000000000000000000000)

forward(200)

#steap 1: draw a square


left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)

#end of square
#drawing a door

forward(70)

color("blue")
left(90)
forward(120)       #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end fo door

#drawing a Window

color("black")

penup()
goto(15,120)
pendown()
left(30)
right(180)
forward(68)
right(90)
forward(40)

right(90)
forward(68)
right(90)
forward(40) 

penup()
goto(145,120)
pendown()
left(180)
forward(40)
left(90)
forward(68)
left(90)
forward(40)
left(90)
forward(68)
penup()

#done :)

exitonclick()