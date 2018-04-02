 #exercise 1
import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()
tess.pensize(3)
pensize=3

# The next four functions are our "event handlers".
def h1():
   tess.color("red")

def h2():
   tess.color("green")

def h3():
   tess.right("blue")
def h4():
    global pensize
    pensize+1
    tess.pensize()
def h5():
    wn.title("change!")




wn.onkey(h1, "R")
wn.onkey(h2, "G")
wn.onkey(h3, "B")
wn.onkey(h4,"+")
wn.onkey(h5,"c")


wn.listen()
wn.mainloop()
