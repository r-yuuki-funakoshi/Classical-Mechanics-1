from vpython import *
#Web VPython 3.2

from vpython import *
dt = 3600
t = 0
time = 0.1e10

#Difining quantities
G = 6.67*10**-11
c = 3e8 #m/s speed of light
μ = 2e29
μ2 =  2.85586e-108
#The two stars in a binary star system
s1 = sphere(pos = vec(-1.1e11, 0, 0), radius = 2e10, mass = 1e24, v = vec(0, 0, 0), F = vec(0, 0, 0), make_trail=True, color = color.red) 
s2 = sphere(pos = vec(1.5e11, 0 , 0), radius = 1e10, mass = 1e24, v = vec(0, 1e1, 0), F = vec(0, 0, 0), make_trail=True, color = color.green)
#rad1 = sphere(pos = vec(-1.1e11, 0, 0), radius = 1e10, mass = 0, v = vec(0, 0, 0), F = vec(0, 0, 0), make_trail=True) 
#rad2 = sphere(pos = vec(1.5e11, 0 , 0), radius = 1e10, mass = 0, v = vec(0, 1e1, 0), F = vec(0, 0, 0), make_trail=True)

s1.p = (1 / sqrt(1 - (mag(s1.v) / c)**2)) * s1.mass * s1.v #relativistic momemtum formulae for velocities closer to c
s2.p = (1 / sqrt(1 - (mag(s2.v) / c)**2)) * s2.mass * s2.v

#Defining quantities to calculate
KE1 = (1 / 2) * s1.mass * dot(s1.v, s1.v)
KE1_initial = (1 / 2) * s1.mass * dot(vec(0, 0, 0,), vec(0, 0, 0,))
KE2 = (1 / 2) * s2.mass * dot(s2.v, s2.v)
KE2_initial = (1 / 2) * s2.mass * dot(vec(0, 1e1, 0), vec(0, 1e1, 0))
W1 = dot(s1.F, s1.v) * dt
W1_initial = dot(vec(0, 0, 0), vec(0, 0, 0)) * dt
W2 = dot(s2.F, s2.v) * dt
W2_initial = dot(vec(0, 0, 0), vec(0, 1e1, 0)) * dt
U1 = -G * s1.mass * s2.mass / (mag(s1.pos - s2.pos))
U1_initial = -G * s1.mass * s2.mass / (mag(vec(-1.1e11, 0, 0) - vec(1.5e11, 0 , 0)))
U2 = -G * s1.mass * s2.mass / (mag(s2.pos - s1.pos))
U2_initial = -G * s1.mass * s2.mass / (mag(vec(1.5e11, 0 , 0) - vec(-1.1e11, 0, 0)))

ΔΚΕ_system = 0
ΔU_system = 0
E1_rad = E2_rad = rad1 = rad2 = 0
rad_sum = 0

g_v = graph(title = "Total momenta of the system", xtitle = "time (s)", ytitle = "System momenta")
g_v2 = graph(title = "Work done by the system", xtitle = "time (s)", ytitle = "W")
gr1 = graph(title = "Kinetic energy of the system", xtitle = "time (s)", ytitle = "KE")
gr2 = graph(title = "ΔU the change in potential energy = -W", xtitle = "time (s)", ytitle = "U")
gr3 = graph(title = "Total energy change", xtitle = "time (s)", ytitle = "ΔKE + ΔU")
gr4 = graph(title = "Radiated energy", xtitle = "time (s)", ytitle = "Erad")

g1=gcurve(graph=g_v, color=color.red)
g2=gcurve(graph=g_v2, color=color.red)
g3=gcurve(graph=gr1, color=color.red)
g4=gcurve(graph=gr2, color=color.red)
g5=gcurve(graph=gr3, color=color.red)
g6=gcurve(graph=gr4, color=color.red)

gg = graph(title = "KE, U, and KE + U", xtitle = "time (s)", ytitle = "")
gg2 = graph(title = "KE, U, and KE + U as functions of displacement", xtitle = "Total displacement of the system", ytitle = "")
Kinetic=gcurve(graph = gg, color = color.red)
Potential=gcurve(graph = gg, color = color.cyan)
KplusU=gcurve(graph =gg, color = color.yellow)
Kinetic2=gcurve(graph = gg2, color = color.red)
Potential2=gcurve(graph = gg2, color = color.cyan)
KplusU2=gcurve(graph =gg2, color = color.yellow)


while True:
    rate(1e10)
    t += dt
    
    s1.F = -G * s1.mass * s2.mass * (s1.pos - s2.pos) / ((mag(s1.pos - s2.pos))**3) #Force on s1 by s2
    s2.F = -G * s1.mass * s2.mass * (s2.pos - s1.pos) / ((mag(s2.pos - s1.pos))**3) #Force on s2 by s1
    
    s1.p += s1.F * dt
    s1.v = s1.p / s1.mass
    s2.p += s2.F * dt
    s2.v = s2.p / s2.mass
    
    s1.pos += (s1.p / s1.mass) * dt
    s2.pos += (s2.p / s2.mass) * dt
    
    Fg_rad1 = μ2 * ((-G * s2.mass * ((mag(s1.pos - s2.pos))**3))**2) * dot((s1.pos - s2.pos), (s1.pos - s2.pos)) * (-s1.v / mag(s1.v))
    Fg_rad2 = μ2 * ((-G * s1.mass * ((mag(s2.pos - s1.pos))**3))**2) * dot((s2.pos - s1.pos), (s2.pos - s1.pos)) * (-s2.v / mag(s2.v))
    E1_rad += dot(Fg_rad1, s1.v) * dt
    E2_rad += dot(Fg_rad2, s2.v) * dt
    
    rad1_integrand = ((-G * s2.mass * ((mag(s1.pos - s2.pos))**3))**2) * dot((s1.pos - s2.pos), (s1.pos - s2.pos)) * (-s1.v / mag(s1.v))
    rad2_integrand = ((-G * s1.mass * ((mag(s2.pos - s1.pos))**3))**2) * dot((s2.pos - s1.pos), (s2.pos - s1.pos)) * (-s2.v / mag(s2.v))
    rad1 += dot(rad1_integrand, s1.v) * dt
    rad2 += dot(rad2_integrand, s2.v) * dt
    
    rad_sum += rad1 + rad2
    
    Fnet = s1.F + s2.F + Fg_rad1 + Fg_rad2
    
    W1 += dot(s1.F, s1.v) * dt #Work is iterative and integrative. Use +=, the recursive expression
    W2 += dot(s2.F, s2.v) * dt
    
    KE1 = (1 / 2) * s1.mass * dot(s1.v, s1.v) #These values are RELATIVE and functions are not ITERATIVE.
    KE2 = (1 / 2) * s2.mass * dot(s2.v, s2.v) # it is =  but not +=
    U1 = -G * s1.mass * s2.mass / (mag(s1.pos - s2.pos))
    U2 = -G * s1.mass * s2.mass / (mag(s2.pos - s1.pos))
    
    KE_system = KE1 + KE2
    W_system = W1 + W2
    U_system = U1 + U2
    E_rad = E1_rad + E2_rad
    
    ΔΚΕ_system = KE_system- (KE1_initial + KE2_initial)
    ΔU_system = (U_system - (U1_initial + U2_initial)) / 2
    
    g1.plot(t, mag(s1.p ) + mag(s2.p))
    g2.plot(t, W_system)
    g3.plot(t, KE_system)
    g4.plot(t, U_system)
    g5.plot(t, ΔΚΕ_system + ΔU_system)
    g6.plot(t, E_rad)
    
    Kinetic.plot(t, KE_system)
    Potential.plot(t, U_system)
    KplusU.plot(t, KE_system + U_system - E_rad)
    
    Kinetic2.plot(mag(s1.pos - vec(-1.1e11, 0, 0)) + mag(s2.pos - vec(1.5e11, 0, 0)), KE_system)
    Potential2.plot(mag(s1.pos - vec(-1.1e11, 0, 0)) + mag(s2.pos - vec(1.5e11, 0, 0)), U_system)
    KplusU2.plot(mag(s1.pos - vec(-1.1e11, 0, 0)) + mag(s2.pos - vec(1.5e11, 0, 0)), KE_system + U_system - E_rad)
    
    if t > time:
        break
    
#Riemann sum prediction
#Right endpoint rule approximation using kinematics formula
W_Rn = []
a = 0
b = time
n = 1e5
Δt = (b - a) / n
for i in range(1, int(n)):
    Rn = Δt * ((dot(s1.F, vec(0, 0, 0))) + (dot(s1.F, s1.F) / s1.mass) * (a + Δt * i))
    W_Rn.append(Rn)

a = 0
b = time
n = 1e5
Δt = (b - a) / n
for i in range(1, int(n)):
    Rn = Δt * ((dot(s2.F, vec(0, 1e1, 0))) + (dot(s2.F, s2.F) / s2.mass) * (a + Δt * i))
    W_Rn.append(Rn)
    
#Right endpoint rule approximation using kinematics formula
W_Mn = []
a = 0
b = time
n = 1e5
Δt = (b - a) / n
for i in range(1, int(n)):
    Mn = Δt * ((dot(s1.F, vec(0, 0, 0))) + (dot(s1.F, s1.F) / s1.mass) * (a + Δt * i + a + Δt * (i-1)) / 2)
    W_Mn.append(Mn)

a = 0
b = time
n = 1e5
Δt = (b - a) / n
for i in range(1, int(n)):
    Mn = Δt * ((dot(s1.F, vec(0, 0, 0))) + (dot(s1.F, s1.F) / s1.mass) * (a + Δt * i + a + Δt * (i-1)) / 2)
    W_Mn.append(Mn)

#Trapezoidal rule
W_Tn = []
a = 0
b = time
n = 1e5
Δt = (b - a) / n
for i in range(1, int(n)):
    Tn = (Δt / 2) * ((dot(s1.F, vec(0, 0, 0))) + (dot(s1.F, s1.F) / s1.mass) * (a + Δt * i) + (dot(s1.F, vec(0, 0, 0))) + (dot(s1.F, s1.F) / s1.mass) * (a + Δt * (i-1)))
    W_Tn.append(Tn)

a = 0
b = time
n = 1e5
Δt = (b - a) / n
for i in range(1, int(n)):
    Tn = (Δt / 2) * ((dot(s1.F, vec(0, 0, 0))) + (dot(s1.F, s1.F) / s1.mass) * (a + Δt * i) + (dot(s1.F, vec(0, 0, 0))) + (dot(s1.F, s1.F) / s1.mass) * (a + Δt * (i-1)))
    W_Tn.append(Tn)
    
    
print("Work done in the system by the planets = ", W_system)
print("The potential energy change or -W = ", ΔU_system)
print("Change in kinetic energy = ", ΔΚΕ_system)
print("Energy lost by gravitational radiation", ΔΚΕ_system - W_system)
print("Energy radiated (prediction by assuming u = 2e29)", E_rad)
print("True value of u the coefficient", (ΔΚΕ_system - W_system) / rad_sum)
print("Right-hand Riemann sum prediction of total work", sum(W_Rn))
print("Mid-point Riemann sum prediction of total work", sum(W_Mn))
print("Trapezoidal Riemann sum prediction of total work", sum(W_Tn))
print("Simpson's Rule Riemann sum prediction of total work", (sum(W_Tn) / 3) + (sum(W_Mn)*2 / 3))
