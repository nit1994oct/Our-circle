import turtle

my_turtle = turtle.Turtle()

def square(angle):
    my_turtle.right(angle)
    for i in range(4):
         my_turtle.right(90)
         my_turtle.forward(100)

   
    angle = angle + 5
    
angle=0
square(angle)
angle =5
while True:
    square(angle)
    
    
