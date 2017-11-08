from turtle import *
speed(0)
ht()
lt(90)


axiom=[]
function=[]
n=0
axiomStr=""
functionStr=""
level=0
angle=0

##--------------------------------------------------------------------------------------------------
##      Axiom           Function
##  F-F-F-F         FF-F-F-F-FF
##
##  F-F-F-F     FF-F-F-F-F-F+F
##
## (F-F+F-FF)   (F-F+F-FF)
## (F--FF++F)   (F+F-F)
##--------------------------------------------------------------------------------------------------

def F ():
    forward(d)

def f ():
    penup()
    forward(d)
    pendown()


def F_function(level):
    if (level != n+1):
       exec(functionStr)
    else: F()

def getXYZR():
    x=xcor()
    y=ycor()
    r=heading()
    return [x,y,r]

def setXYZR(pos):
    pu()
    goto(pos[0],pos[1])
    pd()
    setheading(pos[2])

def start_system ():
    exec(axiomStr)

##--------------------------------------------------------------------------------------------------

##moeglichkeit axiom und funktion fix als string einzugeben fehlt noch


d=0
x=0 ## int(input("x start Coordinates?"))
y=0## int(input("y start Coordinates?"))
goto(x,y)

if (axiom == []):
    axiom=list(input("Axiom? in format [F-F-F-F] ?"))
if (function == []):
    function=list(input("Function? (F-> [F+F--F+F])?"))
if (n==0):
    n=int(input("Iterations?"))
if (angle==0):
    angle=float(input("angle?"))
if (d==0):
    d=int(input("size of each line in the end?"))



for i in range (len(axiom)):
    if (axiom[i] == "-"):
        axiom[i]="right(angle)\n"
    elif (axiom[i] == "+"):
        axiom[i]="left(angle)\n"
    elif (axiom[i] == "F"):
        axiom[i]="F_function(level+1)\n"
    elif (axiom[i] == "f"):
        axiom[i]="f()\n"
    elif (axiom[i] == "["):
        axiom[i]="pos=getXYZR()\n"
    elif (axiom[i] == "]"):
        axiom[i]="setXYZR(pos)\n"

for i in range (len(function)):
    if (function[i] == "-"):
        function[i]="right(angle)\n"
    elif (function[i] == "+"):
        function[i]="left(angle)\n"
    elif (function[i] == "F"):
        function[i]="F_function(level+1)\n"
    elif (function[i] == "f"):
        function[i]="f()\n"
    elif (function[i] == "["):
        function[i]="pos=getXYZR()\n"
    elif (function[i] == "]"):
        function[i]="setXYZR(pos)\n"

for i in range (len(axiom)):
    axiomStr+=axiom[i]

for i in range (len(function)):
       functionStr+=function[i]

start_system()

done()



