from vpython import *
#Web VPython 3.2

from vpython import *

spring = helix(pos = vec(0, 0, 0), axis = vec(0, -1, 0), radius = 0.4, thickness = 0.05,
                coil = 8, k_stiffness = 4)
object = sphere(pos = spring.axis, radius = 0.5, color = color.cyan, emissive = True,
                mass = 0.5, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
                
# simulating the motion

equilibrium_pos = spring.pos - spring.axis
g = 9.8
dt = 0.01
t = 0

gr = graph(title = "The Velocity of the Object as a Function of Time", xtitle = "time (s)", ytitle = "Velocity")
g1 = gcurve(graph = gr, color = color.blue)

while True:
    rate(1/dt) # For a real-time simulation, use 1/dt as the rate
    
    t += 1
    
    object.force = -spring.k_stiffness * (object.pos - equilibrium_pos)
    F_gravity = vec(0, -g * object.mass, 0)
    object.velocity += (object.force + F_gravity/object.mass) * dt
    object.pos += object.velocity * dt
    spring.axis = object.pos - spring.pos
    
    g1.plot(t, object.velocity.y)
    

