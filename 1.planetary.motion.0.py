from vpython import *
#Web VPython 3.2

from vpython import *

#Difining quantities
dist=1.5*10**11
G=6.67*10**-11
M=2*10**30
m=6*10**24

sun=sphere(pos=vec(0,0,0), radius=100, make_trail=True) #two objects
earth=sphere(pos=vec(dist,0,0), radius=1, make_trail=True)

sun_v=vec(0,0,0)
earth_v=vec(0,29000,0) #Initial velocities

g_v=graph(title="Y-velocity component vs. time: Earth", xtitle="Number of time intervals", ytitle="Y-velocity")
g_v2=graph(title="Y-velocity component vs. time: the Sun", xtitle="Number of time intervals", ytitle="Y-velocity")
g1=gcurve(graph=g_v, color=color.red)
g2=gcurve(graph=g_v2, color=color.red)

dt=1
t=0

while True:
    rate(1000000000)
    t+=1
    sun_v=sun_v + (earth.pos - sun.pos)*G*m / (mag(earth.pos - sun.pos)**3)*dt #velocity update
    sun.pos=sun.pos+sun_v*dt #positional update
    
    earth_v=earth_v + (sun.pos - earth.pos)*G*M / (mag(sun.pos - earth.pos)**3)*dt 
    earth.pos=earth.pos+earth_v*dt
    
    g1.plot(t, earth_v.y)
    g2.plot(t, sun_v.y)

    if t > 3e7 and earth.pos.y > 0:
        break
num_days = t*dt/(60*60*24)
print("The estimated length of one revolution and thus a year in days", num_days)
    
    

    
