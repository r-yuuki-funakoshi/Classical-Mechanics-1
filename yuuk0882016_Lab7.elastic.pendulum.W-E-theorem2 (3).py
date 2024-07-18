from vpython import *
#Web VPython 3.2

from vpython import *
op=0.7
visibility=True
indicator1=arrow(pos=vec(0,0,0), axis=vec(100,0,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.red)
indicator2=arrow(pos=vec(0,0,0), axis=vec(0,100,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.cyan)
indicator3=arrow(pos=vec(0,0,0), axis=vec(0,0,100), shaftwidth=0.1, visible=visibility, opacity=op, color=color.green)

θ = radians(input("Initial angular position in degrees: ", ))
θi = θ
Xi = int(input("Initial compression or strech of the spring: ", ))
ob_mass = float(input("Object mass?", ))

spring = helix(pos = vec(0, 0, 0), axis = 5 * vec(sin(θ), -cos(θ), 0), radius = 0.4, thickness = 0.05,
                coil = 8, k_stiffness = 10)             

object = sphere(pos = (5 + Xi) * vec(sin(θ), -cos(θ), 0), rad = 0.5, color = color.cyan, emissive = True,
                mass = ob_mass, velocity = 0, initial_velocity = 0, ω = 0, force = vec(0, 0, 0), make_trail = True)
                
L0 = mag(vec(5, 0, 0) - vec(0, 0, 0))
L = mag(spring.axis - spring.pos)
strech = L - L0
KE = 0

ρ = input("1000 kg/m^-3 for water, 700-950 for unsaturated oil, and 1.225 for air :", )
Cd = 0.47
C = 0.003
Area = float(pi * object.rad**2)
A = Xi
print("Medium density: ", ρ, "\nDrag coefficient: ", Cd)
angular_v = sqrt((spring.k_stiffness / object.mass) - (Cd / (2 * object.mass))**2)
v_t = 0
T = 2 * pi / angular_v
ψ = (1 / 2) * ρ * Cd * Area
# simulating the motion
# Ignoring the mass of the spring in this simulation

g = 9.8
dt = 1e-5
t = 0
e = 2.7182818284

gr1 = graph(title = "The strech of the spring", xtitle = "time (t)", ytitle = "x(t)")
gr2 = graph(title = "The angular displacement of the elastic pendulum", xtitle = "time (t)", ytitle = "Angular displacement")
gr3 = graph(title = "Spring potential energy + graviational potentioal energy (red), KE + U (orange), Kinetic energy (cyan)", xtitle = "dr (m)", ytitle = "Energy")
g1 = gcurve(graph = gr1)
g2 = gcurve(graph = gr2)
g3_1 = gcurve(graph = gr3, color = color.red)
g3_2 = gcurve(graph = gr3, color = color.orange)
g3_3 = gcurve(graph = gr3, color = color.cyan)

object.force = -spring.k_stiffness * (mag(object.pos - spring.pos) - L0) * ((object.pos - spring.pos) / mag(object.pos - spring.pos))
F_gravity = vec(0, -g * object.mass, 0)


while True:
    rate(10 / dt) # For a real-time simulation, use 1/dt as the rate
    
    t += dt
    
    #a_t = A * e**(-C * t / (2 * object.mass)) * (((C**2 / (4 * object.mass**2)) - angular_v**2) * cos(angular_v * t)
        #  + (angular_v + 1) * (C / (2 * object.mass)) * sin(angular_v * t))
    
    #v_t += a_t * dt 
    
    strech = A * e**((-C / 2 * object.mass) * t) * cos(angular_v * t)
    
    F_net = (F_gravity.y / L) * sin(θ) - ψ * object.ω
    
    object.ω += (F_net / object.mass) * dt
    
    θ += object.ω * dt #θi * (object.mass / ψ) * e**(-0.01 * t) * cos(t) #object.ω * dt #A * e**((-Cd / 2 * object.mass) * t) * cos(angular_v * t)
    
    object.pos = (strech + L0) * (vec(sin(θ), -cos(θ), 0))
    spring.axis = object.pos
    v = object.ω * vec(sin(θ), -cos(θ), 0)
    
    object.force = -spring.k_stiffness * (mag(object.pos - spring.pos) - L0) * ((object.pos - spring.pos) / mag(object.pos - spring.pos))
    F_gravity = vec(0, -g * object.mass, 0)

    Us = (1 / 2) * spring.k_stiffness * strech
    Ug = object.mass * g * (5 - abs(object.pos.y))
    dr = object.pos - (5 + Xi) * vec(sin(θ), -cos(θ), 0)
    F = F_gravity + object.force - ψ * v
    KE = dot(F, dr) * mag(dr)
    
    g1.plot(t, strech)
    g2.plot(t, degrees(θ))
    g3_1.plot(t, Us + Ug)
    g3_2.plot(t, KE + Us + Ug)
    g3_3.plot(t, KE)

    if t > 100:
        break
    
print("ψ value (coefficient): ", ψ)