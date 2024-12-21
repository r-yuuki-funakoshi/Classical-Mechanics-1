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
sun_m=sun_v*M
earth_m=earth_v*m

g_v=graph(title="Y-velocity component vs. time: Earth", xtitle="Number of time intervals", ytitle="Y-velocity")
g_v2=graph(title="Y-velocity component vs. time: the Sun", xtitle="Number of time intervals", ytitle="Y-velocity")
g_p=graph(title="Y-momentum componen vs. timet: Earth", xtitle="Number of time intervals", ytitle="Y-momentum")
g_p1=graph(title="Y-momentum componen vs. timet: the Sun", xtitle="Number of time intervals", ytitle="Y-momentum")
g_p2=graph(title="X vs Y momenta: Earth", xtitle="X component of the momentum", ytitle="Y component of the momentum")
g_p3=graph(title="X vs Y momenta: the Sun", xtitle="X component of the momentum", ytitle="Y component of the momentum")
g1=gcurve(graph=g_v, color=color.red)
g2=gcurve(graph=g_v2, color=color.red)
g3=gcurve(graph=g_p, color=color.red)
g4=gcurve(graph=g_p1, color=color.red)
g5=gcurve(graph=g_p2, color=color.red)
g6=gcurve(graph=g_p3, color=color.red)

dt=1
t=0

while True:
    rate(10**10)
    t+=1
    sun_m=sun_m + (earth.pos - sun.pos)*G*m*M / (mag(earth.pos - sun.pos)**3)*dt
    sun_v=sun_m/M
    sun.pos=sun.pos+sun_v*dt
    
    earth_m=earth_m + (sun.pos - earth.pos)*G*M*m / (mag(sun.pos - earth.pos)**3)*dt
    earth_v=earth_m/m
    earth.pos=earth.pos+earth_v*dt
    
    g1.plot(t, earth_v.y)
    g2.plot(t, sun_v.y)
    g3.plot(t, earth_v.y*M)
    g4.plot(t, sun_v.y*m)
    g5.plot(earth_v.x*m, earth_v.y*m)
    g6.plot(sun_v.x*m, sun_v.y*m)
