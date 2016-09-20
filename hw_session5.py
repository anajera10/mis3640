import math 
def circle(t,r):
    circumference=2*math.pi*r
    n=50
    length = circumference/n
    polygon(t,n,length)

def circle(t,r):
    circumference=2*math.pi*r
    n=int(circumference/3)+1
    length = circumference/n
    polygon(t,n,length)

def arc(t,r,angle):
    arc_length= 2*math.pi * r *angle
    n= int(arc_length / 3) + 1
    step_length=arc_length/n
    step_angle=angle/n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def polyline (t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t,n,length):
    angle=360.0/ n 
    polyline(t,n,length,angle)

def arc(t,r,angle):
    arc_length=2*math.pi*r*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle= float(angle)/n
    polyline(t,n,step_length,step_angle)

    def circle(t,r):
        arc(t,r,360)

   
