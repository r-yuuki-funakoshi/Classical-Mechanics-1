from vpython import *
#Web VPython 3.2

from vpython import *
op=0.7
visibility=True
indicator1=arrow(pos=vec(0,0,0), axis=vec(100,0,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.red)
indicator2=arrow(pos=vec(0,0,0), axis=vec(0,100,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.cyan)
indicator3=arrow(pos=vec(0,0,0), axis=vec(0,0,100), shaftwidth=0.1, visible=visibility, opacity=op, color=color.green)

initial_st = int(input("Initial compression or strech?", ))
spring = helix(pos = vec(0, 0, 0), axis = vec(5, 0, 0), radius = 0.4, thickness = 0.05,
                coil = 8, k_stiffness = 10)
object = sphere(pos = vec(5 + initial_st, 0, 0), radius = float(input("Object radius?", )), color = color.cyan, emissive = True, mass = float(input("Object mass?", )), speed = 0, velocity = vec(0, 0, 0), initial_velocity = vec(0, 0, 0), force = vec(0, 0, 0), make_trail = True)

ρ = input("1000 kg/m^-3 for water, 700-950 for unsaturated oil, and 1.225 for air :", )
Cd = input("0.47 for a sphere, 1 for a block", )
A = float(pi * object.radius**2)
print("Medium density: ", ρ, "\nDrag coefficient: ", Cd, "\nCross-sectional area: ", A)
# simulating the motion
# Ignoring the mass of the spring in this simulation

equilibrium_pos = spring.pos - spring.axis
g = 9.8
dt = 1e-5
t = 0
e = 2.7182818284
ψ = (1 / 2) * ρ * Cd * A
q = int(input("If simulating viscous drag, type 1 otherwise 0", ))
object.force = -spring.k_stiffness * (mag(object.pos - spring.pos) - mag(equilibrium_pos)) * ((object.pos - spring.pos) / mag(object.pos - spring.pos))
F_gravity = vec(0, -g * object.mass, 0)
F_air = (1 / 2) * ρ * dot(object.velocity, object.velocity) * Cd * A * (-1 * object.velocity / mag(object.velocity)) * q

#Things to calculate and plot: Work done by gravitational force. Work done by the spring force. Spring potential energy, Gravitational potential energy. KE + U
#Air drag

gr = graph(title = "Work by Gravity", xtitle = "time (s)", ytitle = "Work")
gr2 = graph(title = "Work by Spring", xtitle = "time (s)", ytitle = "Work")
gr22 = graph(title = "Work by drag in a fluid medium", xtitle = "time (s)", ytitle = "Work")
gr3 = graph(title = "Gravitational potential energy", xtitle = "time (s)", ytitle = "Ug")
gr4 = graph(title = "Spring potential energy ", xtitle = "time (s)", ytitle = "Us")
gr5 = graph(title = "KE (red), KE + U(yellow), U (cyan), Energy lost(orange)", xtitle = "time (s)", ytitle = "")
gr6 = graph(title = "ΔKE + ΔU (Includes potential energy loss by drag)", xtitle = "time (s)", ytitle = "ΔKE + ΔU")
gr7 = graph(title = "velocity", xtitle = "time (s)", ytitle = "v")
g1 = gcurve(graph = gr, color = color.blue)
g2 = gcurve(graph = gr2, color = color.blue)
g_air = gcurve(graph = gr22, color = color.blue)
g3 = gcurve(graph = gr3, color = color.blue)
g4 = gcurve(graph = gr4, color = color.blue)

g5_1 = gcurve(graph = gr5, color = color.red)
g5_2 = gcurve(graph = gr5, color = color.yellow)
g5_3 = gcurve(graph = gr5, color = color.cyan)
g5_4 = gcurve(graph = gr5, color = color.orange)

g6 = gcurve(graph = gr6, color = color.blue)
g7 = gcurve(graph = gr7, color = color.red)

Ws = dot(object.force, object.velocity) * dt
Wg = dot(F_gravity, object.velocity) * dt
Us = (1 / 2) * spring.k_stiffness * (mag(object.pos - spring.pos) - mag(equilibrium_pos))**2
Ug = object.mass * g * (5 - abs(spring.pos.y))
Us_initial = (1 / 2) * spring.k_stiffness * (mag(object.pos - spring.pos) - mag(equilibrium_pos))**2
Ug_initial = object.mass * g * (5 - abs(object.pos.y))
KE = 0
KE_initial = (1 / 2) * object.mass * dot(object.initial_velocity, object.initial_velocity)
Enet = Us_initial + Ug_initial + KE_initial
print("Total energy of the system: ", Enet)

while True:
    rate(10 / dt) # For a real-time simulation, use 1/dt as the rate
    
    t += dt
    
    #Spring fore equation with unit vector that determines the direction
    object.force = -spring.k_stiffness * (mag(object.pos - spring.pos) - mag(equilibrium_pos)) * ((object.pos - spring.pos) / mag(object.pos - spring.pos))
    #Constant force
    F_gravity = vec(0, -g * object.mass, 0)
    
    Fnet = object.force + F_gravity
    a = Fnet / object.mass #+ e**(-t / ψ) * t / (ψ**2) #a = Fnet / m if not considering drag
    object.velocity += a * dt
    object.pos += object.velocity * dt
    spring.axis = object.pos - spring.pos
    
    #Calculating work and energy
    Ws += dot(object.force, object.velocity) * dt
    Wg += dot(F_gravity, object.velocity) * dt
    
    #Air drag
    F_air = (1 / 2) * ρ * dot(object.velocity, object.velocity) * Cd * A * (-1 * object.velocity / mag(object.velocity)) * q
    F_airunit = (object.velocity / mag(object.velocity))
    Wa = dot(F_air, object.velocity) * dt #MUST BE DEFINED after its variable velocity is defined in the loop
    
    Fnet2 = object.force + F_gravity + F_air
    a = Fnet2 / object.mass #+ e**(-t / ψ) * t / (ψ**2) #a = Fnet / m if not considering drag
    object.velocity += a * dt
    object.pos += object.velocity * dt
    spring.axis = object.pos - spring.pos
    
    KE = 0.5 * object.mass * dot(object.velocity, object.velocity)
    
    #Calculating work and energy
    Ws += dot(object.force, object.velocity) * dt
    Wg += dot(F_gravity, object.velocity) * dt
    Wa += dot(F_air, object.velocity) * dt
    
    Us = (1 / 2) * spring.k_stiffness * (mag(object.pos - spring.pos) - mag(equilibrium_pos))**2
    Ug = object.mass * g * (5 - abs(object.pos.y))
    Unet = Us + Ug
    
    ΔKE = KE - KE_initial
    ΔU = (Unet) - (Ug_initial + Us_initial)
    Enet = Unet + KE
    
    g1.plot(t, Wg)
    g2.plot(t, Ws)
    g_air.plot(t, Wa)
    g3.plot(t, Ug)
    g4.plot(t, Us)
    
    g5_1.plot(t, KE)
    g5_2.plot(t, Enet)
    g5_3.plot(t, Unet)
    g5_4.plot(t, Wa)
    
    g6.plot(t, ΔKE + ΔU)
    g7.plot(t, mag(object.velocity))
    
    if t > 30:
        break
print("")
print("Object and medium properties")
print("Mass: ", object.mass, " Radius: ", object.radius, " Density of the fluid medium: ", ρ)
print("")
print("The work done by gravitational force = ", Wg)
print("The work done by the spring force = ", Ws)
print("The work done by the air drag or \"energy loss\"", Wa)
print("The potential energy loss U by drag", -Wa)
print("")
print("The gravitational potential energy = ", Ug)
print("The spring potential energy = ", Us)
print("")
print("The change in kinetic energy = ", ΔKE)
print("The total work done in the system omitting drag", Ws + Wg)
print("The total work done in the system including the medium", Ws + Wg + Wa)
print("The total change in potential energy", ΔU)
print("")
print("Total energy of the system (does not include the medium) at the end: ", Enet + Wa)
print("Total energy of the system (includes the medium) at the end: ", Enet)

    
    

