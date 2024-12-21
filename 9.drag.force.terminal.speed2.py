from vpython import *
#Web VPython 3.2

from vpython import *
op=0.7
visibility=True
indicator1=arrow(pos=vec(0,0,0), axis=vec(100,0,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.red)
indicator2=arrow(pos=vec(0,0,0), axis=vec(0,100,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.cyan)
indicator3=arrow(pos=vec(0,0,0), axis=vec(0,0,100), shaftwidth=0.1, visible=visibility, opacity=op, color=color.green)

object = sphere(pos = vec(0, 0, 0), radius = float(input("Object radius?", )), color = color.cyan, emissive = True, mass = float(input("Object mass?", )), speed = 0, velocity = vec(0, 0, 0), initial_velocity = vec(0, 0, 0), make_trail = True)
object2 = sphere(pos = vec(5, 0, 0), radius = float(input("Object2 radius?", )), color = color.red, emissive = True, mass = float(input("Object2 mass?", )), speed = 0, velocity = vec(0, 0, 0), initial_velocity = vec(0, 0, 0), make_trail = True)
object3 = sphere(pos = vec(10, 0, 0), radius = float(input("Object3 radius?", )), color = color.yellow, emissive = True, mass = float(input("Object3 mass?", )), speed = 0, velocity = vec(0, 0, 0), initial_velocity = vec(0, 0, 0), make_trail = True)
object4 = sphere(pos = vec(15, 0, 0), radius = float(input("Object4 radius?", )), color = color.blue, emissive = True, mass = float(input("Object4 mass?", )), speed = 0, velocity = vec(0, 0, 0), initial_velocity = vec(0, 0, 0), make_trail = True)

ρ = input("1000 kg/m^-3 for water, 700-950 for unsaturated oil, and 1.225 for air :", )
Cd = input("0.47 for a sphere, 1 for a block", )
A = float(pi * object.radius**2)
A2 = float(pi * object2.radius**2)
A3 = float(pi * object3.radius**2)
A4 = float(pi * object4.radius**2)
print("Medium density: ", ρ, "\nDrag coefficient: ", Cd, "\nCross-sectional area: ", A)

F_air = vec(0, 0, 0)
F_air2 = vec(0, 0, 0)
F_air3 = vec(0, 0, 0)
F_air4 = vec(0, 0, 0)

g = 9.8
dt = 1e-5
t = 0
e = 2.7182818284
q = int(input("If simulating viscous drag, type 1 otherwise 0", ))

gr = graph(title = "(Cyan = object 1, red = object2, yellow = object3, blue = object4)", xtitle = "time (s)", ytitle = "v (m/s)")
gr2 = graph(title = "(Cyan = object 1, red = object2, yellow = object3, blue = object4)", xtitle = "time (s)", ytitle = "a (m/s^2)")
gr3 = graph(title = "(Cyan = object 1, red = object2, yellow = object3, blue = object4)", xtitle = "time (s)", ytitle = "Net force (N)")
g1_1 = gcurve(graph = gr, color = color.cyan)
g1_2 = gcurve(graph = gr, color = color.red)
g1_3 = gcurve(graph = gr, color = color.yellow)
g1_4 = gcurve(graph = gr, color = color.blue)
g2_1 = gcurve(graph = gr2, color = color.cyan)
g2_2 = gcurve(graph = gr2, color = color.red)
g2_3 = gcurve(graph = gr2, color = color.yellow)
g2_4 = gcurve(graph = gr2, color = color.blue)
g3_1 = gcurve(graph = gr3, color = color.cyan)
g3_2 = gcurve(graph = gr3, color = color.red)
g3_3 = gcurve(graph = gr3, color = color.yellow)
g3_4 = gcurve(graph = gr3, color = color.blue)

while True:
    rate(10 / dt) # For a real-time simulation, use 1/dt as the rate
    
    t += dt

    #Constant force
    F_gravity = vec(0, -g * object.mass, 0)
    F_gravity2 = vec(0, -g * object2.mass, 0)
    F_gravity3 = vec(0, -g * object3.mass, 0)
    F_gravity4 = vec(0, -g * object4.mass, 0)
    
    a = F_gravity / object.mass
    a2 = F_gravity / object2.mass
    a3 = F_gravity / object3.mass
    a4 = F_gravity / object4.mass
    object.velocity += a * dt
    object2.velocity += a2 * dt
    object3.velocity += a3 * dt
    object4.velocity += a4 * dt
    object.pos += object.velocity * dt
    object2.pos += object2.velocity * dt
    object3.pos += object3.velocity * dt
    object4.pos += object4.velocity * dt

    #Air drag
    F_air = (1 / 2) * ρ * dot(object.velocity, object.velocity) * Cd * A * (-1 * object.velocity / mag(object.velocity)) * q
    F_air2 = (1 / 2) * ρ * dot(object2.velocity, object2.velocity) * Cd * A2 * (-1 * object2.velocity / mag(object2.velocity)) * q
    F_air3 = (1 / 2) * ρ * dot(object3.velocity, object3.velocity) * Cd * A3 * (-1 * object3.velocity / mag(object3.velocity)) * q
    F_air4 = (1 / 2) * ρ * dot(object4.velocity, object4.velocity) * Cd * A4 * (-1 * object4.velocity / mag(object4.velocity)) * q
    k1 = (-1 / 2) * ρ * dot(object.velocity, object.velocity) * Cd * A / mag(object.velocity)
    k2 = (-1 / 2) * ρ * dot(object2.velocity, object2.velocity) * Cd * A2 / mag(object2.velocity)
    k3 = (-1 / 2) * ρ * dot(object3.velocity, object3.velocity) * Cd * A3 / mag(object3.velocity)
    k4 = (-1 / 2) * ρ * dot(object4.velocity, object4.velocity) * Cd * A4 / mag(object4.velocity)
        
    Fnet = F_gravity + F_air
    Fnet2 = F_gravity2 + F_air2
    Fnet3 = F_gravity3 + F_air3
    Fnet4 = F_gravity4 + F_air4
    object.velocity.y = (e**(-k1 * t / object.mass) - Fnet.y) / k1
    object2.velocity.y = (e**(-k2 * t / object2.mass) - Fnet2.y) / k2
    object3.velocity.y = (e**(-k3 * t / object3.mass) - Fnet3.y) / k3
    object4.velocity.y = (e**(-k4 * t / object4.mass) - Fnet4.y) / k4
    object.pos += object.velocity * dt
    object2.pos += object2.velocity * dt
    object3.pos += object3.velocity * dt
    object4.pos += object4.velocity * dt
    
    g1_1.plot(t, object.velocity.y)
    g1_2.plot(t, object2.velocity.y)
    g1_3.plot(t, object3.velocity.y)
    g1_4.plot(t, object4.velocity.y)
    g2_1.plot(t, a.y)
    g2_2.plot(t, a2.y)
    g2_3.plot(t, a3.y)
    g2_4.plot(t, a4.y)
    g3_1.plot(t, Fnet.y)
    g3_2.plot(t, Fnet2.y)
    g3_3.plot(t, Fnet3.y)
    g3_4.plot(t, Fnet4.y)
    
 #   if t < 10 and mag(a4) < 0.001:
#        break

print("")
print("Mass")
print("Object1: ", object.mass, " Object2: ", object2.mass, " Object3: ", object3.mass, " Object4: ", object4.mass)
print("")
print("Radius")
print("Object1: ", object.radius, " Object2: ", object2.radius, " Object3: ", object3.radius, " Object4: ", object4.radius)
print("")
print("Acceleration")
print("Object1: ", mag(a), " Object2: ", mag(a2), "Object3: ", mag(a3)," Object4: ", mag(a4))
print("")
print("Terminal velocity")
print("Object1: ", mag(object.velocity), " Object2: ", mag(object2.velocity), " Object3: ", mag(object3.velocity), " Object4: ", mag(object4.velocity))
print("")
print("Total displacement (y-axis)")
print("Object1: ", object.pos.y, " Object2: ", object2.pos.y, " Object3: ", object3.pos.y, "Object4: ", object4.pos.y, )
    
    
