from vpython import *
#Web VPython 3.2

from vpython import *

#Axis indicator
#Opacity and visibility
op=0.7
visibility=True
indicator1=arrow(pos=vec(0,0,0), axis=vec(100,0,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.red)
indicator2=arrow(pos=vec(0,0,0), axis=vec(0,100,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.cyan)
indicator3=arrow(pos=vec(0,0,0), axis=vec(0,0,100), shaftwidth=0.1, visible=visibility, opacity=op, color=color.green)

#camera position and axis (axis is the object of interest with DIRECTION, and position is the observer's position)
scene.camera.pos=vec(2,0,2)
scene.center=vec(2,0,0)

#Difining quantities
G = 6.67*10**-11
theta = radians(45) #launch angle
theta2 = radians(45) #launch angle
speed = 10
speed2 = 10
escape_v = 1.2e4 #escape velocity from Earth
initial_v = speed * vec(cos(theta), sin(theta), 0)
initial_v2 = speed2 * vec(cos(theta), sin(theta), 0)


ball1 = sphere(pos = vec(0, 0, 0), radius = 0.5, mass = 0.5, force = vec(0, 0, 0), work = 0, velocity = speed * vec(cos(theta), sin(theta), 0),
        color = color.red, make_trail = True, billboard = True)
ball2 = sphere(pos = vec(0, 0, 0), radius = 0.5, mass = 10, force = vec(0, 0, 0), work = 0, velocity = speed2 * vec(cos(theta), sin(theta), 0),
        color = color.blue, make_trail = True, billboard = True)
        
#Difining quantities
KE = (1 / 2) * ball1.mass * dot(ball1.velocity, ball1.velocity)
U = -G * ball1.mass * 6e24 / (6.4e6 - mag(ball1.pos - vec(0, 0, 0)))
KE2 = (1 / 2) * ball2.mass * dot(ball2.velocity, ball2.velocity)
U2 = -G * ball2.mass * 6e24 / (6.4e6 - mag(ball2.pos - vec(0, 0, 0)))


g = 9.8 #m/s^2
dt = 0.0001
Fg = vec(0, -ball1.mass * g, 0)
Fg2 = vec(0, -ball2.mass * g, 0)
t = 0

gr1 = graph(title = "Kinetic energy KE", xtitle = "time (s)", ytitle = "KE")
gr2 = graph(title = "Work", xtitle = "time (s)", ytitle ="Work")
gr3 = graph(title = "KE + U", xtitle = "time (s)", ytitle = "KE + U")
g1 = gcurve(graph = gr1)
g2 = gcurve(graph = gr2)
g3 = gcurve(graph = gr3)

gr12 = graph(title = "Kinetic energy KE2", xtitle = "time (s)", ytitle = "KE2")
gr22 = graph(title = "Work2", xtitle = "time (s)", ytitle ="Work2")
gr32 = graph(title = "KE2 + U2", xtitle = "time (s)", ytitle = "KE2 + U2")
g12 = gcurve(graph = gr12)
g22 = gcurve(graph = gr22)
g32 = gcurve(graph = gr32)

gg = graph(title = "KE, U, KE + U", xtitle = "time (s)", ytitle = "")
kineticE = gcurve(graph = gg, color = color.cyan)
Upotential = gcurve(graph = gg, color = color.red)
KplusU = gcurve(graph = gg, color = color.yellow)

gg2 = graph(title = "KE, U, KE + U", xtitle = "time (s)", ytitle = "")
kineticE2 = gcurve(graph = gg2, color = color.cyan)
Upotential2 = gcurve(graph = gg2, color = color.red)
KplusU2 = gcurve(graph = gg2, color = color.yellow)

#Right endpoint rule approximation using kinematics formula
work_Rn = []
a = 0
b = 8
n = 1e5
Δt = (b - a) / n
for i in range(1, int(n)):
    Rn = Δt * ((dot(Fg, ball1.velocity)) + (dot(Fg, Fg) / ball1.mass) * (a + Δt * i))
    work_Rn.append(Rn)

work_Rn2 = []
a = 0
b = b
n = 1e5
Δt = (b - a) / n
for i in range(1, int(n)):
    Rn2 = Δt * ((dot(Fg2, ball2.velocity)) + (dot(Fg2, Fg2) / ball2.mass) * (a + Δt * i))
    work_Rn2.append(Rn2)
                
#Kinematic calculation + work-energy calculation
while True:
    rate(1 / dt)
    t += dt
    ball1.velocity += Fg / ball1.mass * dt
    ball1.pos += ball1.velocity * dt
    
    ball2.velocity.y += -g * dt
    ball2.pos += ball2.velocity * dt
    
    #Work done on the ball1 by gravity
    ball1.work += dot(Fg, ball1.velocity) * dt
    ball2.work += dot(Fg2, ball2.velocity) * dt
    
    #kinetic energy
    KE = (1 / 2) * ball1.mass * dot(ball1.velocity, ball1.velocity)
    U = -G * ball1.mass * 6e24 / (6.4e6 - mag(ball1.pos - vec(0, 0, 0)))
    KE2 = (1 / 2) * ball2.mass * dot(ball2.velocity, ball2.velocity)
    U2 = -G * ball2.mass * 6e24 / (6.4e6 - mag(ball2.pos - vec(0, 0, 0)))
    
    g1.plot(t, KE)
    g2.plot(t, ball1.work)
    g3.plot(t, KE + U)
    kineticE.plot(t, KE)
    Upotential.plot(t, U)
    KplusU.plot(t, KE + U)
    
    g12.plot(t, KE2)
    g22.plot(t, ball2.work)
    g32.plot(t, KE2 + U2)
    kineticE2.plot(t, KE2)
    Upotential2.plot(t, U2)
    KplusU2.plot(t, KE2 + U2)
    
    if t != 0 and ball1.velocity.y <= 0:
        break

initial_KE = (1 / 2) * ball1.mass * dot(initial_v, initial_v)
final_KE = (1 / 2) * ball1.mass * dot(ball1.velocity, ball1.velocity)
change_in_KE = final_KE - initial_KE

initial_KE2 = (1 / 2) * ball2.mass * dot(initial_v2, initial_v2)
final_KE2 = (1 / 2) * ball2.mass * dot(ball2.velocity, ball2.velocity)
change_in_KE2 = final_KE2 - initial_KE2
print("Work upon ball1 by gravity at the highest altitude = ", ball1.work)
print("Change in kinetic energy KE when ball1 goes through the highest altitude = ",
      change_in_KE)
print("")
print("Work upon ball1 by gravity at the highest altitude = ", ball2.work)
print("Change in kinetic energy KE when ball1 goes through the highest altitude = ",
      change_in_KE2)
print("")

while True:
    rate(1 / dt)
    rate(1 / dt)
    t += dt
    ball1.velocity += Fg / ball1.mass * dt
    ball1.pos += ball1.velocity * dt
    
    ball2.velocity.y += -g * dt
    ball2.pos += ball2.velocity * dt
    
    #Work done on the ball1 by gravity
    ball1.work += dot(Fg, ball1.velocity) * dt
    ball2.work += dot(Fg2, ball2.velocity) * dt
    
    #kinetic energy
    KE = (1 / 2) * ball1.mass * dot(ball1.velocity, ball1.velocity)
    U = -G * ball1.mass * 6e24 / (6.4e6 - mag(ball1.pos - vec(0, 0, 0)))
    KE2 = (1 / 2) * ball2.mass * dot(ball2.velocity, ball2.velocity)
    U2 = -G * ball2.mass * 6e24 / (6.4e6 - mag(ball2.pos - vec(0, 0, 0)))
    
    g1.plot(t, KE)
    g2.plot(t, ball1.work)
    g3.plot(t, KE + U)
    kineticE.plot(t, KE)
    Upotential.plot(t, U)
    KplusU.plot(t, KE + U)
    
    g12.plot(t, KE2)
    g22.plot(t, ball2.work)
    g32.plot(t, KE2 + U2)
    kineticE2.plot(t, KE2)
    Upotential2.plot(t, U2)
    KplusU2.plot(t, KE2 + U2)
    
    if t != 0 and ball1.velocity.y <= 0 and ball1.pos.y < 0.00001:
        break

initial_KE = (1 / 2) * ball1.mass * dot(initial_v, initial_v)
final_KE = (1 / 2) * ball1.mass * dot(ball1.velocity, ball1.velocity)
change_in_KE = final_KE - initial_KE

initial_KE2 = (1 / 2) * ball2.mass * dot(initial_v2, initial_v2)
final_KE2 = (1 / 2) * ball2.mass * dot(ball2.velocity, ball2.velocity)
change_in_KE2 = final_KE2 - initial_KE2
print("Work upon ball1 by gravity at the same altitude as the starting point = ", ball1.work)
print("Change in kinetic energy KE when ball1 goes through the same altitude as the starting point = ",
      change_in_KE)
print("")
print("")


while True:
    rate(1 / dt)
    t += dt
    ball1.velocity += Fg / ball1.mass * dt
    ball1.pos += ball1.velocity * dt
    
    ball2.velocity.y += -g * dt
    ball2.pos += ball2.velocity * dt
    
    #Work done on the ball1 by gravity
    ball1.work += dot(Fg, ball1.velocity) * dt
    ball2.work += dot(Fg2, ball2.velocity) * dt
    
    #kinetic energy
    KE = (1 / 2) * ball1.mass * dot(ball1.velocity, ball1.velocity)
    U = -G * ball1.mass * 6e24 / (6.4e6 - mag(ball1.pos - vec(0, 0, 0)))
    KE2 = (1 / 2) * ball2.mass * dot(ball2.velocity, ball2.velocity)
    U2 = -G * ball2.mass * 6e24 / (6.4e6 - mag(ball2.pos - vec(0, 0, 0)))
    
    g1.plot(t, KE)
    g2.plot(t, ball1.work)
    g3.plot(t, KE + U)
    kineticE.plot(t, KE)
    Upotential.plot(t, U)
    KplusU.plot(t, KE + U)
    
    g12.plot(t, KE2)
    g22.plot(t, ball2.work)
    g32.plot(t, KE2 + U2)
    kineticE2.plot(t, KE2)
    Upotential2.plot(t, U2)
    KplusU2.plot(t, KE2 + U2)
    
    if t > b:
        break

initial_KE = (1 / 2) * ball1.mass * dot(initial_v, initial_v)
final_KE = (1 / 2) * ball1.mass * dot(ball1.velocity, ball1.velocity)
change_in_KE = final_KE - initial_KE

initial_KE2 = (1 / 2) * ball2.mass * dot(initial_v2, initial_v2)
final_KE2 = (1 / 2) * ball2.mass * dot(ball2.velocity, ball2.velocity)
change_in_KE2 = final_KE2 - initial_KE2

#The Work-Energy Theorem: work done by a net force is equal the change in kinetic energy!!
print("Initial velocity of ball", initial_v)
print("Initial velocity of rock", initial_v2)
print("")
print("The total work done on ball1 by gravity: ", ball1.work)
print("Change in kinetic energy: ",  change_in_KE)
print("Right-hand Riemann sum approximation", sum(work_Rn))
print("")
print("The total work done on rock by gravity: ", ball2.work)
print("Change in kinetic energy of the rock: ",  change_in_KE2)
print("Right-hand Riemann sum approximation", sum(work_Rn2))
    

    