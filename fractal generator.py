#for real numbers 
import random
import turtle 

dx = 0.03
scalar = 50


#Functions for Calculation of Fractaals 

def burningShip():
  global doesConverge 
  global x
  global y 
  global z
  global iterator
  z = 0
  y =-y
  for _ in range(10):
   z = complex(abs(z.real),abs(z.imag))
   z = z*z + complex(x,y)
   if z.real >2 or z.imag >2:
    iterator = _ 
    y = -y
    break
  if z.real < 2 and z.imag < 2: 
    doesConverge = True
    y =-y

def juliaSet():
  global doesConverge 
  global x
  global y 
  global z
  global iterator 
  z = complex(x,y)
  for _ in range(10):
   z = z*z + c
   if z.real >2 or z.imag >2:
    iterator = _
    break
  if z.real < 2 and z.imag < 2: 
    doesConverge = True    
    
def mandelbrot():
  global doesConverge 
  global x
  global y 
  global z
  global iterator 
  z = complex(x,y)
  for _ in range(10):
   z = z*z + complex(x,y)
   if z.real >2 or z.imag >2:
    iterator = _ 
    break
  if z.real < 2 and z.imag < 2: 
    doesConverge = True    
    
#FUNCTIONS FOR TURTLING / TURTLE SETUP 

t = turtle.Turtle()
t.fillcolor("black")
sc=turtle.Screen()
sc.tracer(2,100000)
t.penup()
turtle.Screen().bgcolor("blue")

def saveScreen():
  t.goto(0,0)
  t.hideturtle()
  turtle.forward(1)
  ts = turtle.getscreen()
  ts.getcanvas().postscript(file=("drawing.eps" + str(j)))
  t.clear()

def turtleDraw():
  positionA = (x-(dx))*scalar
  positionB= (y+(dx))*scalar
  t.goto(positionA,positionB)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
    t.forward(dx*scalar)
    t.right(90)
  t.end_fill()
  t.penup()
  
def colorAtPoint():
  turtle.colormode(255)
  t.color(int(iterator*25.5),0,255)

#Execution 
j=0
iterator = 0 
doesConverge = False 
while True:
  a = random.random()*(-1**random.randint(1,2))
  b = random.random()*(-1**random.randint(1,2))
  c = complex(a,b)
  print("Valaue a: " + str(a) + " at " + str(j) + " iteration.")
  print("Valaue b: " + str(b) + " at " + str(j) + " iteration.")
  y=-1.4
  j+= 1 
  for q in range(int(1.4/dx*2)):
    x = -3
    for p in range(int(7/dx)):
    # the function inside of this for loop determines the kind of fractal that will be rendered 
      #juliaSet()
      #mandelbrot()
      burningShip()
      if doesConverge == True: 
        t.fillcolor(0,0,0)
        t.color(0,0,0)
        turtleDraw()
      elif iterator > 3:
        colorAtPoint()
        turtleDraw()
      x+=dx 
      doesConverge = False
    y+=dx
  print("Complete")
  #This section saves the turtle screen as an Ep file you need to manually convert from EP to Png/Jpg etc 
  saveScreen()
  t.clear()
