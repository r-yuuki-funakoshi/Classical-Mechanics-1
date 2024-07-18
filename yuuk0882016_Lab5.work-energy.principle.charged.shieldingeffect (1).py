from vpython import *
#Web VPython 3.2

from vpython import *

Me = 9.1094e-31
Mp = 1.6726e-27
Mn = 1.6749e-27
ε_0 = 8.85418e-12
eV = 1.6022e-19  # Corrected the value (J)

e = sphere(pos=vec(-5, 2, 0), radius=0.1, v=vec(5, -8, 0), force=vec(0, 0, 0), color=color.cyan, make_trail=True)
e2 = sphere(pos=vec(6, 2, 0), radius=0.1, v=vec(-5, -1, 0), force=vec(0, 0, 0), color=color.cyan, make_trail=True)
p1 = sphere(pos=vec(0, 0, 0), radius=0.2, v=vec(0, 0, 0), force=vec(0, 0, 0), color=color.red, make_trail=True)

e.p = e.v * Me
p1.p = p1.v * Mp
e2.p = e2.v * Me
p_system = e.p + p1.p + e2.p

gr1 = graph(title = "KE electron", xtitle = "time (s)", ytitle = "KE")
gr2 = graph(title = "Work doen by proton", xtitle = "time (s)", ytitle = "W")
gr3 = graph(title = "U the potential energy", xtitle = "time (s)", ytitle = "U")
gr4 = graph(title = "KE, KE + U, and U", xtitle = "time (s)", ytitle = "")
g1 = gcurve(graph = gr1)
g2 = gcurve(graph = gr2)
g3 = gcurve(graph = gr3)
gg4 = gcurve(graph = gr4, color = color.red)
gg5 = gcurve(graph = gr4, color = color.cyan)
gg6 = gcurve(graph = gr4, color = color.yellow)


t = 0
dt = 1e-5

while True:
    t += dt
    rate(10000)

    # Calculate forces
    F_e1_proton = (1 / (4 * pi * ε_0)) * (-eV * eV / (mag(p1.pos - e.pos))**3) * (e.pos - p1.pos)# Attractive force of proton on electron 1
    F_e2_proton = (1 / (4 * pi * ε_0)) * (-eV * eV / (mag(p1.pos - e2.pos))**3) * (e2.pos - p1.pos)
    p1.force = (1 / (4 * pi * ε_0)) * (-eV * eV / (mag(p1.pos - e.pos))**3) * (p1.pos - e.pos) + (1 / (4 * pi * ε_0)) * (-eV * eV / (mag(p1.pos - e2.pos))**3) * (p1.pos - e2.pos) 
    #Attractive force of electron on proton
    F_e1_e2 = (1 / (4 * pi * ε_0)) * (eV * eV / (mag(e2.pos - e.pos))**3) * (e.pos - e2.pos)  # Repulsive force between electron 1 and electron 2
    F_e2_e1 = (1 / (4 * pi * ε_0)) * (eV * eV / (mag(e.pos - e2.pos))**3) * (e2.pos - e.pos)  # Repulsive force between electron 2 and electron 1

    # Update forces on objects
    e.force = (F_e1_proton + F_e1_e2)
    e2.force = (F_e2_proton + F_e2_e1)

    # Update velocities using Newton's second law F = ma
    e.p += (e.force) * dt
    e2.p += (e2.force) * dt
    p1.p += (p1.force) * dt

    # Update positions using the updated velocities
    e.pos += (e.p / Me) * dt
    e2.pos += (e2.p / Me) * dt
    p1.pos += (p1.p / Mp) * dt
    p_system += e.p + p1.p + e2.p
    
    #work
    e.w = dot(e.force, e.p / Me) * dt
    e2.w = dot(e2.force, e2.p / Me) * dt
    p1.w = dot(p1.force, p1.p / Me) * dt
    
    e.w += dot(e.force, e.p / Me) * dt
    e2.w += dot(e2.force, e2.p / Me) * dt
    p1.w += dot(p1.force, p1.p / Me) * dt
    
    
    KE_system = (1 / 2) * Me * dot(e.p / Me, e.p / Me)**2 + (1 / 2) * Mp * dot(p1.p / Mp, p1.p / Mp)**2 + (1 / 2) * Me * dot(e2.p / Me, e2.p / Me)**2
    W_system = e.w + e2.w + p1.w
    U_system = (1 / (4 * pi * ε_0)) * (-eV * eV / (mag(p1.pos - e.pos))) + (1 / (4 * pi * ε_0)) * (eV * eV / (mag(e2.pos - e.pos))) + (1 / (4 * pi * ε_0)) * (eV * eV / (mag(e.pos - e2.pos)))
    
    
    g1.plot(t, KE_system)
    g2.plot(t, W_system)
    g3.plot(t, U_system)
    gg4.plot(t, KE_system + U_system) #red
    gg5.plot(t, KE_system) #cyan
    gg6.plot(t, U_system) #yellow
    

    