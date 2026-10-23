#exercise1

# import turtle
# tess= turtle.Turtle()
# screen= turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.color("pink")
# tess.pensize(5)
# def drawPoly(tess,a,b):
#     tess.penup()
#     tess.goto(-10,0)
#     tess.pendown()
#     for i in range(a):
#         tess.forward(b)
#         tess.left(72)
# a=8
# b=50
# drawPoly(tess,a,b)
#
# screen.exitonclick()

# import turtle
# tess=turtle.Turtle()
# screen=turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.color("blue")
#
# def drawpoly(someturtle,someside,somesize):
#     angle=360/someside
#     for i in range (someside):
#         someturtle.forward(somesize)
#         someturtle.left(angle)
#exercise2

# for i in range(20):
#     drawpoly(tess,4,100)
#     tess.left(18)

# def drawspiral(someturtle,angle):
#     size=1
#     for i in range(100):
#         someturtle.forward(size)
#         someturtle.right(angle)
#         size=size+2
#exercise3

# tess.pencolor("blue")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# drawspiral(tess,90)
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawspiral(tess,89)

# def drawEguitriangle(someturtle,somesize):
#     drawpoly(someturtle,3,somesize)
# def drawStart(someturtle,size):
#     for i in range(5):
#         someturtle.forward(size)
#         someturtle.right(144)
# def drawSprite(someturtle,legs,length):
#     angle=360/legs
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
#         someturtle.left(angle)

#exercise4
# drawEguitriangle(tess,100)


#exercise5
# tess.color("hotpink")
# for i in range(5):
#     drawStart(tess,50)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()

#exercise6
# drawSprite(tess,15,120)
#
#
#
#
#
# screen.exitonclick()



