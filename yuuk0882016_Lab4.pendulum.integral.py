from vpython import *
from scipy import integrate
from numpy import sin, sqrt, pi
import numpy as np

dt = 0.001
t = 0
g = 9.8
ω = 0
θ = radians(float(input("Angle in degrees [choose from 2, 5, 10, 45, 65, 90]: ")))
#As the calculation starts at the negative y-axis, pi is at 90 degrees and 0 is at 270 degrees.

string = cylinder(pos = vec(0, 0, 0), axis = vec(0, -float(input("The length of the string [choose from 0.9, 1.2, 1.5]: ")), 0),
                  radius = 0.01, color = color.cyan, ks = 40)

L = mag(string.axis - string.pos)

bob = sphere(pos = string.axis, radius = 0.1, mass = float(input("Mass [choose from 0.555, 0.750, 0.950, 1.5]: ")),
             color = color.red, velocity = vec(0, 0, 0 ), force = vec(0, 0, 0))

#Integration of the divergent integral with vertical asymptotes
antideriv =[]
def integrand(x, a, b):
    return a / sqrt(a - (b * sin(x))**2)

a = 1
b = sin(θ/2)

I = integrate.quad(integrand, 0, pi / 2, args=(a, b))
print("Integral result = ", I)
print("Anser to be used =", I[0])

T = 4 * sqrt(L / g) * I[0] # !!Presise approximation for both large angles and small angles
T2 = 2 * pi * sqrt(L / g) #theoretical small-angle approximation of time interval
time = []
angular_velocity = []
Δt = []

gr = graph(title = "Angular displacement", xtitle = "time (s)", ytitle = "Angular displacement")
gr2 = graph(title = "Angular velocity", xtitle = "time (s)", ytitle = "Angular velocity")
g1 = gcurve(graph = gr)
g2 = gcurve(graph = gr2)

while True:
    rate(1/dt) #real time execution 1/dt
    
    t += dt
    
    a = (-g / L * sin(θ)) #approximation such that θ<<1 and sin(θ) ~ θ
    
    ω += a * dt #angular velocity update
    
    θ += ω * dt #angular position update
    
    bob.pos = vec(L * sin(θ), -L * cos(θ), 0) #position update
    string.axis = bob.pos
    
    angular_velocity.append(ω)
    
    if ω >= 3.5459: #approx. maximum angular velocity(frequency) calculated (mass = 0.555, L = 0.9)
                    # !!VALUE OF INTEREST ONLY CHANGES, OTHER VALUES REMAIN AS THE 'MINIMUM'!!
                        # for 2 degs, .115180
                        # for 5 degs, .287873
                        # for 10 deg, .5751993329344561
                        # for 45 deg, 2.52558
                        # for 65 deg, 3.54600
                        # for 90 deg, 4.66667
        time.append(t) #experimental time at which the angular velocity (frequency) is maximum
        print(t)
    
    if t > 25: #Make sure to set for 25 sec
        break
    
    g1.plot(t, θ * 180 / pi)
    g2.plot(t, ω)
print("The maximum angular velocity = ", max(angular_velocity))

# Initialize a list to store the first value of each interval to eliminate the some overlaps
time_revised = []

# This "for" loop only transfers time intervals that are different enough and exclude similar values
for i in range(len(time)):
    # If it's the first value or the current value is not immediately following the previous one
    if i == 0 or time[i] - time[i-1] > 0.01:
        time_revised.append(time[i]) #making a new list
print("Time invterval revised", time_revised)
print(" ")
print(" ")

for i in range(len(time_revised)): #Here, by taking arithmetric difference between 2 numbers next to each other
                                           #, delta t = duration of one time interval is produced by this iterative execution
    Δt.append(time_revised[-i] - time_revised[-i-1]) #Iterative function starting from position [-1] or the last element in the list
del Δt[0] #Removes the first element in this list, which is not a correct answer. #Removes the first element in this list, which is not a correct answer.
    
data_size_N = len(Δt)
mean = sum(Δt) / data_size_N
Σ_list = []
for i in range(0, data_size_N):
    Σ_list.append((Δt[i] - mean)**2)
variance = sum(Σ_list) / (data_size_N - 1)
deviation = sqrt(variance)

#Answers in lists rounded to 4 decimal places.
print("The theoretical small-angle approximation of pendulum period = ", T2)
print("The theoretical value of pendulum period = ", T)
print("Δt experimental values: ", np.round(np.array(Δt), 4))
print("Time between each interval:", np.round(np.array(time_revised), 4))

print("Mean value of Δt = ", mean)
print("Variance = ", variance)
print("Standard deviation = ", deviation)
