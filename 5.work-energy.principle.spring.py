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
object = sphere(pos = vec(10, 0 ,0), radius = 0.5, color = color.red, emissive = True,
                mass = 1, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
                
plane = box(pos = vec(0, -0.5, 0), axis = vec(100, 0, 0), height = 0.000001, width = 100, length = 100)
                
# simulating the motion

equilibrium_pos = spring.axis - spring.pos
g = 9.8
dt = 0.01
t = 0
uk = 0.1
gr = graph(title = "The Velocity of the Object as a Function of Time", xtitle = "time (s)", ytitle = "Velocity")
gr2 = graph(title = "Kinetic energy of mass", xtitle = "time (s)", ytitle = "KE")
gr3 = graph(title = "U", xtitle = "time (s)", ytitle = "U")
gr4 = graph(title = "Work", xtitle = "time (s)", ytitle = "W")
gr5 = graph(title = "U + KE = constant", xtitle = "time (s)", ytitle = "U + KE")
g1 = gcurve(graph = gr, color = color.blue)
g2 = gcurve(graph = gr2, color = color.blue)
g3 = gcurve(graph = gr3, color = color.blue)
g4 = gcurve(graph = gr4, color = color.blue)
g5 = gcurve(graph = gr5)
T = 2 * pi * sqrt(object.mass / spring.k_stiffness)

U_potential = -spring.k_stiffness * (mag(object.pos - equilibrium_pos))**2
KE = KE_initial = 0 #Kinetic energy
FE = FE_initial = 0 #Fritional energy
W = 0
W_list = []
KE_list =[]
FE_list =[]

while True:
    rate(1000) # For a real-time simulation, use 1/dt as the rate
    
    t += dt
    
    #Spring fore equation with unit vector that determines the direction
    object.force = -spring.k_stiffness * (mag(object.pos - spring.pos) - mag(equilibrium_pos)) * (object.pos - spring.pos) / mag(object.pos - spring.pos)
    
    F_gravity = vec(0, -g * object.mass, 0)
    F_normal = - F_gravity
    F_fric = vec(-g * object.mass * uk, 0, 0)
    Fnet = -spring.k_stiffness * (mag(object.pos - spring.pos) - mag(equilibrium_pos)) * (object.pos - spring.pos) / mag(object.pos - spring.pos) + F_fric

    if object.velocity.x > 0:
        object.velocity.x += ((object.force.x + F_fric.x)/object.mass) * dt
     
    else:
        object.velocity.x += ((object.force.x - F_fric.x)/object.mass) * dt
    
    Fnet = object.force + F_fric
    FE += dot(F_fric, object.velocity) * dt
    KE += (1 / 2) * object.mass * dot(object.velocity, object.velocity)
    W += dot(Fnet, object.velocity) * dt
    KE_list.append(KE)
    W_list.append(W)
    FE_list.append(FE)
    
    
    #Right endpoint rule approximation using kinematics formula
    work_Rn = []
    a = 0
    b = 30
    n = 1e5
    Δt = (b - a) / n
    for i in range(1, n):
        Rn = Δt * ((dot(Fnet, object.velocity)) + ((dot(Fnet, Fnet)) / object.mass) * (a + Δt * i))
        work_Rn.append(Rn)
    
    U_potential += -spring.k_stiffness * (mag(object.pos - equilibrium_pos))**2
    
    object.pos.x += object.velocity.x * dt
    spring.axis = object.pos - spring.pos
    
    
    g1.plot(t, object.velocity.x)
    g2.plot(t, KE)
    g3.plot(t, U_potential)
    g4.plot(t, W)
    g5.plot(t, U_potential + KE)
    
    if t > b:
        break

KE_final = max(KE_list)
dKE = KE_final - KE_initial


print("The position vector of the mass", object.pos)
print("The predicted time period of one cycle without friction = ", T)
print("Change in KE", dKE)
print("Frictional energy", sum(FE_list))
print("Work", max(W_list))
print("Right hand sum approximation of W", sum(work_Rn)) 
print("Energy lost", sum(W_list) + dKE + sum(FE_list))
