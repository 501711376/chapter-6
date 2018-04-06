 #exercise 1
import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()
tess.pensize(3)
size=3

# The next four functions are our "event handlers".
def h1q():
   tess.color("red")

def h2q():
   tess.color("green")

def h3q():
   tess.color("blue")

def h4q():
    global size
    size += 1
    tess.pensize(size)

def h5q():
    wn.title("change!")
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()



wn.onkey(h1q, "r")
wn.onkey(h2q, "g")
wn.onkey(h3q, "b")
wn.onkey(h4q,"+")
wn.onkey(h5q,"c")
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")


wn.listen()
wn.mainloop()
