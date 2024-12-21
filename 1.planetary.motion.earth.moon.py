from vpython import *
#Web VPython 3.2
from vpython import *

G = 6.67*10**-11
sunearth_r = 1.496*10**11 #(m)
earthmoon_r = 344400e3 #(m)
m_Earth = 5.972*10**24 #(kg)
m_moon = 7.4e22
m_sun = m_Earth*3.3*10**5
radi_Earth = 6.4*10**5
radi_sun = 6.957*10**8
radi_moon = 1700e3


earth = sphere(pos=vec(0,0,0), radius=radi_Earth, color=color.blue, make_trail=True)
moon = sphere(pos=vec(earthmoon_r + radi_Earth + radi_moon,0,0), radius=radi_moon, make_trail=True)

sun_v = vec(0,0,0)
moon_v = vec(0,1050,0)
earth_v = vec(0,0,0)

earth_p=m_Earth*earth_v
moon_p=m_moon*moon_v

dt=0.1
t=0

gr=graph(title="Change in the magnitude of moon's velocity", xtitle="time", ytitle="Speed")
gr2=graph(title="Chnage in momentum", xtitle="time", ytitle="x-component of momenta")
gr3=graph(title="change in momentum", xtitle="time", ytitle="y-componet of momenta")
g1=gcurve(graph=gr, color=color.red)
g2=gcurve(graph=gr2, color=color.red)
g3=gcurve(graph=gr3, color=color.red)

while True:
    rate(100000000)
    t+=1
    
    earth_v = earth_v + (moon.pos - earth.pos)*G*m_moon / (mag(moon.pos - earth.pos)**3)*dt
    earth.pos = earth.pos + earth_v*dt
    
    moon_v = moon_v + (earth.pos - moon.pos)*G*m_Earth / (mag(earth.pos - moon.pos)**3)*dt
    moon.pos = moon.pos + moon_v*dt
    
    moon_p = moon_p + (earth.pos - moon.pos)*G*m_Earth*m_moon / (mag(earth.pos - moon.pos)**3)*dt
    earth_p = earth_p + (moon.pos - earth.pos)*G*m_moon*m_Earth / (mag(moon.pos - earth.pos)**3)*dt
    
    Fnet_system = (earth.pos - moon.pos)*G*m_Earth*m_moon / (mag(earth.pos - moon.pos)**3) + (moon.pos - earth.pos)*G*m_moon*m_Earth / (mag(moon.pos - earth.pos)**3)
    
    if t > 2e7 and moon.pos.y > 0:
        break

print("The estimated duration of a complete orbit of the moon around the earth", t*dt/60/60/24)
 
