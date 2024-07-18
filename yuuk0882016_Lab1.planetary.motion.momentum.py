from vpython import *
#Web VPython 3.2
from vpython import *

dist=1.5*10**11
G=6.67*10**-11
M=2*10**30
m=6*10**24

sun=sphere(pos=vec(0,0,0), radius=100, make_trail=True)
earth=sphere(pos=vec(dist,0,0), radius=1, make_trail=True)

sun_v=vec(0,0,0)
earth_v=vec(0,29000,0)
sun_p=sun_v*M
earth_p=earth_v*m

g_v=graph(title="x-component total momneta of the system", xtitle="Number of time intervals", ytitle="Total momenta x-component")
gr2=graph(title="y-component total momenta", xtitle="time", ytitle="Total momenta y-component")
gr3=graph(title="total momenta plotted", xtitle="Momenta Earth + sun", ytitle="Momenta")
g1=gcurve(graph=g_v, color=color.red)
g2=gcurve(graph=gr2, color=color.red)
g3=gcurve(graph=gr3, color=color.red)

dt=1
t=0

while True:
    rate(10**10)
    t+=1
    sun_v=sun_v + (earth.pos - sun.pos)*G*m / (mag(earth.pos - sun.pos)**3)*dt
    sun.pos=sun.pos+sun_v*dt
    
    earth_v=earth_v + (sun.pos - earth.pos)*G*M / (mag(sun.pos - earth.pos)**3)*dt
    earth.pos=earth.pos+earth_v*dt
    
    sun_p = sun_p + (earth.pos - sun.pos)*G*m*M / (mag(earth.pos - sun.pos)**3) #update in momenta
    earth_p = earth_p + (sun.pos - earth.pos)*G*M*m / (mag(sun.pos - earth.pos)**3)
    
  
    g1.plot(t, earth_p.x + sun_p.x) #Plotting the total momenta
 