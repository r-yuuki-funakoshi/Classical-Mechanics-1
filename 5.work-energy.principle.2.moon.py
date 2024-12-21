from vpython import *
#Web VPython 3.2

from vpython import *

G = 6.67e-11
sunearth_r = 1.496e11  # (m)
earthmoon_r = 344400e3  # (m)
m_Earth = 5.972e24  # (kg)
m_moon = 7.4e22
m_sun = m_Earth * 3.3e5
radi_Earth = 6.4e6
radi_sun = 6.957e8
radi_moon = 1700e3

earth = sphere(pos=vec(0, 0, 0), radius=radi_Earth, color=color.blue, emmissive = True, make_trail=True)
moon = sphere(pos=vec(earthmoon_r + radi_Earth + radi_moon, 0, 0), radius=radi_moon, make_trail=True)

sun_v = vec(0, 0, 0)
moon_v = vec(0, 300, 0)
earth_v = vec(0, 0, 0)

moon_p = m_moon * moon_v
earth_p = -moon_p #conservation of momentum

dt = 1e3
t = 0

gr = graph(title="Moon momentum", xtitle="time (s)", ytitle="Momentum")
gr2 = graph(title="KE", xtitle="time (s)", ytitle="Kinetic energy of moon")
gr3 = graph(title = "U",  xtitle = "time (s)", ytitle = "U the potential energy")
gr4 = graph(title="Work done by Earth on moon", xtitle="time (s)", ytitle="W")
gr5 = graph(title = "KE + U = constant", xtitle = "time (s)", ytitle = "KE + U")
g1 = gcurve(graph=gr, color=color.red)
g2 = gcurve(graph=gr2, color=color.red)
g3 = gcurve(graph=gr3, color=color.red)
g4 = gcurve(graph=gr4, color=color.red)
g5 = gcurve(graph=gr5, color=color.red)

while t < 2e7:
    rate(100)
    
    W = dot((earth.pos - moon.pos) * G * m_Earth * m_moon / (mag(earth.pos - moon.pos) ** 3), moon_v)
    KE_moon = (1 / 2) * m_moon * dot(moon_v, moon_v)
    KE_earth = (1 / 2) * m_Earth * dot(earth_v, moon_v)
    U = -G * m_moon * m_Earth / mag(earth.pos - moon.pos)
    E_total = KE_moon + U

    moon_p += (earth.pos - moon.pos) * G * m_Earth * m_moon / (mag(earth.pos - moon.pos) ** 3) * dt
    moon_v = moon_p / m_moon
    earth_p = -moon_p
    earth_v = earth_p / m_Earth
    moon.pos += moon_v * dt
    earth.pos += earth_v * dt
 
    Fnet_system = (earth.pos - moon.pos) * G * m_Earth * m_moon / (mag(earth.pos - moon.pos) ** 3) + (
                moon.pos - earth.pos) * G * m_moon * m_Earth / (mag(moon.pos - earth.pos) ** 3)

    W += dot((earth.pos - moon.pos) * G * m_Earth * m_moon / (mag(earth.pos - moon.pos) ** 3), moon_v)
    KE_moon = (1 / 2) * m_moon * dot(moon_v, moon_v)
    KE_earth = (1 / 2) * m_Earth * dot(earth_v, moon_v)
    U = -G * m_moon * m_Earth / mag(earth.pos - moon.pos)
    E_total = KE_moon + U

    g1.plot(t, mag(moon_p))
    g2.plot(t, KE_moon)
    g3.plot(t, U)
    g4.plot(t, W)
    g5.plot(t, E_total)


    t += dt
