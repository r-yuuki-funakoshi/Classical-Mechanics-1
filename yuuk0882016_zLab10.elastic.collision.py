from vpython import *
#Web VPython 3.2
from vpython import *

op=0.7
visibility=True
indicator1=arrow(pos=vec(0,0,0), axis=vec(100,0,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.red)
indicator2=arrow(pos=vec(0,0,0), axis=vec(0,100,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.cyan)
indicator3=arrow(pos=vec(0,0,0), axis=vec(0,0,100), shaftwidth=0.1, visible=visibility, opacity=op, color=color.green)

v1 = float(input("The initial speed of M1 (red ball): ", ))
v2 = -float(input("The initial speed of M2 (red ball): ", ))

M1 = sphere(pos = vec(-7, 0, 0), radius = 3.5, mass = int(input("The mass of M1 (red ball): ", )), velocity = vec(v1, 0, 0), color = color.red)
M2 = sphere(pos = vec(7, 0, 0), radius = 3.5, mass = int(input("The mass of M2 (blue ball): ", )), velocity = vec(v2, 0, 0), color = color.blue)
spring = helix(pos = vec(-0.25, 0, 0), axis = vec(0.25, 0, 0), radius = 0.2, thickness = 0.03, coil = 5, k_stiffness = 15, visible = False)

eq_length = 0.5

gr1 = graph(title = "Velocity of M1 (red), M2 (blue)", xtitle = "time (s)", ytitle = "v")
gr2 = graph(title = "Momentum of M1 (red), M2 (blue)", xtitle = "time (s)", ytitle = "p")
gr3 = graph(title = "Total momenta of the system", xtitle = "time (s)", ytitle = "Total momenta")
gr4 = graph(title = "Total KE(orange), M1 energy(red), M2 energy(blue)", xtitle = "time (s)", ytitle = "E")
gr5 = graph(title = "Total mechanical energy (KE and elastic energy)", xtitle = "time (s)", ytitle = "E")

g1_1 = gcurve(graph = gr1, color = color.red)
g1_2 = gcurve(graph = gr1, color = color.blue)
g2_1 = gcurve(graph = gr2, color = color.red)
g2_2 = gcurve(graph = gr2, color = color.blue)
g3 = gcurve(graph = gr3, color = color.red)
g4_1 = gcurve(graph = gr4, color = color.orange)
g4_2 = gcurve(graph = gr4, color = color.red)
g4_3 = gcurve(graph = gr4, color = color.blue)
g5 = gcurve(graph = gr5, color = color.red)

Fsp = vec(0, 0, 0)
M1_momentum = M1.velocity * M1.mass
M2_momentum = M2.velocity * M2.mass
KE1_initial = 0.5 * M1.mass * v1**2
KE2_initial = 0.5 * M2.mass * v2**2
KE1 = 0.5 * M1.mass * dot(M1.velocity, M1.velocity)
KE2 = 0.5 * M2.mass * dot(M2.velocity, M2.velocity)
KE_total = KE1 + KE2
E_internal = 0

print("The total momenta of the system before collision: ", M1.mass * M1.velocity + M2.mass * M2.velocity)
print("The total kinetic energy of the system before collision: ", KE_total)

dt = 1e-5
t = 0
while True:
    rate(1 / dt)
    t += dt
    
    M1.pos += M1.velocity * dt
    M2.pos += M2.velocity * dt
    
    if t > 10:
        break
    
    if mag(M1.pos - M2.pos) <= eq_length:
        spring.axis = M2.pos
        spring.pos = M1.pos
        
        Fsp.x = -spring.k_stiffness * (mag(M1.pos - M2.pos) - eq_length) #Scalar quantity
        
        M1.velocity.x += (Fsp.x / M1.mass) * dt
        M2.velocity.x += (Fsp.x / M2.mass) * dt
        
        M1.pos += M1.velocity * dt
        M2.pos += M2.velocity * dt
        
        KE1 = 0.5 * M1.mass * dot(M1.velocity, M1.velocity)
        KE2 = 0.5 * M2.mass * dot(M2.velocity, M2.velocity)
        KE_total = KE1 + KE2
        
        E_internal = (KE1_initial + KE2_initial) - KE_total
    
    if abs(mag(M1.pos - M2.pos) - eq_length) <= sqrt(2 * KE_total / spring.k_stiffness):
        spring.axis = M2.pos
        spring.pos = M1.pos
        
        Fsp.x = -spring.k_stiffness * (mag(M1.pos - M2.pos) - eq_length) #Scalar quantity
        deltax_1 = sqrt((2 / spring.k_stiffness) * 0.5 * M1.mass * v1**2)
        deltax_2 = sqrt((2 / spring.k_stiffness) * 0.5 * M2.mass * v2**2)
        
        if M1.mass > M2.mass or M1.mass == M2.mass:
            M1.velocity.x = ((v1 + M2.mass * v2 / M1.mass) - (M2.mass / M1.mass) * sqrt(v1**2 + v2**2 - (spring.k_stiffness * deltax_2**2 / M2.mass)))
            M2.velocity.x = -((v2 + M1.mass * v1 / M2.mass) - (M1.mass / M2.mass) * sqrt(v1**2 + v2**2 - (spring.k_stiffness * deltax_1**2 / M1.mass)))
            M1.pos += M1.velocity * dt
            M2.pos += M2.velocity * dt
            
        if M2.mass > M1.mass:
            M1.velocity.x = ((M1.mass * v1 + M2.mass * v2) / (M1.mass + M2.mass))
            M2.velocity.x = M1.velocity.x
            M1.pos += M1.velocity * dt
            M2.pos += M2.velocity * dt
        
        KE1 = 0.5 * M1.mass * dot(M1.velocity, M1.velocity)
        KE2 = 0.5 * M2.mass * dot(M2.velocity, M2.velocity)
        KE_total = KE1 + KE2
        
        E_internal = (KE1_initial + KE2_initial) - KE_total
    
    g1_1.plot(t, M1.velocity.x)
    g1_2.plot(t, M2.velocity.x)
    g2_1.plot(t, M1.velocity.x * M1.mass)
    g2_2.plot(t, M2.velocity.x * M2.mass)
    
    g3.plot(t, M1.velocity.x * M1.mass + M2.velocity.x * M2.mass)

    g4_1.plot(t, KE_total)
    g4_2.plot(t, KE1)
    g4_3.plot(t, KE2)
    
    g5.plot(t, KE_total + E_internal)

        
print("-----------------------------------------------------")
print("Object1 mass: ", M1.mass, "   Object2 mass: ", M2.mass)
print("Object1 initial velocity: ", v1, "   Object2 initial velocity: ", v2)
print("The total momenta of the system after collision: ", M1.mass * M1.velocity + M2.mass * M2.velocity)
print("The total kinetic energy of the system after collision: ", KE_total)
print("The total energy of the system including elastic mechanical energy: ", KE_total + E_internal)
        
    