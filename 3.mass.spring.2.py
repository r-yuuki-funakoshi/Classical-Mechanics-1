from vpython import *
#Web VPython 3.2

from vpython import *
op=0.7
visibility=True
indicator1=arrow(pos=vec(0,0,0), axis=vec(100,0,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.red)
indicator2=arrow(pos=vec(0,0,0), axis=vec(0,100,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.cyan)
indicator3=arrow(pos=vec(0,0,0), axis=vec(0,0,100), shaftwidth=0.1, visible=visibility, opacity=op, color=color.green)

spring = helix(pos = vec(0, 0, 0), axis = vec(15, 0, 0), radius = 0.4, thickness = 0.05,
                coil = 8, k_stiffness = 10)
object = sphere(pos = vec(5, 0 ,0), radius = 0.5, color = color.red, emissive = True,
                mass = 1, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
                
plane = box(pos = vec(0, -0.5, 0), axis = vec(100, 0, 0), height = 0.000001, width = 100, length = 100)
                
# simulating the motion

equilibrium_pos = spring.pos - spring.axis
g = 9.8
dt = 0.01
t = 0
uk = 1
gr = graph(title = "The Velocity of the Object as a Function of Time", xtitle = "time (s)", ytitle = "Velocity")
g1 = gcurve(graph = gr, color = color.blue)

T = 2 * pi * sqrt(object.mass / spring.k_stiffness) * 100

while True:
    rate(1/dt) # For a real-time simulation, use 1/dt as the rate
    
    t += 1
    
    #Spring fore equation with unit vector that determines the direction
    object.force = -spring.k_stiffness * (mag(object.pos - spring.pos) - mag(equilibrium_pos)) * (object.pos - spring.pos) / mag(object.pos - spring.pos)
    
    F_gravity = vec(0, -g * object.mass, 0)
    F_normal = - F_gravity
    F_fric = vec(-g * object.mass * uk, 0, 0)
    
    if t > 1200 and object.velocity.x < 0.00001:
        break

    if object.velocity.x > 0:
        object.velocity.x += ((object.force.x + F_fric.x)/object.mass) * dt
    
    else:
        object.velocity.x += ((object.force.x - F_fric.x)/object.mass) * dt
        
    object.pos.x += object.velocity.x * dt
    spring.axis = object.pos - spring.pos
    
 
    g1.plot(t, object.velocity.x)
    
print("The final position of the mass = ", object.pos.x)
print("The predicted time period = ", T)
