# def fizz_buzz(num):
#     for i in range(1,num+1):
#       if i%15==0:
#          print("fizzbuzz")
#       elif i%5==0:
#          print("buzz")
#       elif i%3==0:
#          print("fizz")
#       else:
#          print(i)
# fizz_buzz(10)

# def digit_sum(n):
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n=n//10
#     return sum
# print(digit_sum(1231))

# def altarnete_case(s):
#     sum=""
#     for a in range(len(s)):
#
#        if  a %2 == 0:
#          sum=sum+ s[a].upper()
#        else:
#          sum=sum+ s[a].lower()
#     return sum
#
# print(altarnete_case("hello world"))
# import turtle
# t=turtle.Turtle()
# screen=turtle.Screen()
# colors=("red","yellow","blue")
# def draw_polyong(t,side,length):
#     angle=360/side
#     for i in range(side):
#         t.fd(length)
#         t.left(angle)
#
# for i in range(3):
#   t.penup()
#   t.goto(-150+i*120,0)
#   t.pendown()
#   t.color(colors[i])
#   draw_polyong(t,i+3,60) n
# import turtle
# t=turtle.Turtle()
# Screen=turtle.Screen()
# colors=['red','blue']
# def filled_square(t,size,color):
#   for i in range(4):
#    color=colors[i%2]
#    t.fillcolor(color)
#    t.begin_fill()
#    for i in range(4):
#       t.forward(size)
#       t.left(90)
#    t.end_fill()
#    t.penup()
#    t.forward(size*2)
#    t.forward(size*2)
#
# filled_square(t,10,colors)
# Screen.exitonclick()

import turtle
t=turtle.Turtle()
screen=turtle.Screen()
# t.speed(20)
# t.pensize(2)
# length=80
# def square(t,length):
#     for i in range(4):
#         t.forward(length)
#         t.left(90)
#
# for i in range(12):
#     square(t,length)
#     t.left(30)

# def drawsquare(t,size,filled):
#     if filled:
#         t.begin_fill()
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#     if filled:
#         t.end_fill()
# size=40
# for row in range(6):
#     for col in range(6):
#         t.penup()
#         t.goto(-120+col*size,-120+row*size)
#         t.pendown()
#         drawsquare(t,40,(row+col)%2==0)
# screen.exitonclick()



