from vpython import *
#Web Vpython 3.2

from vpython import *

dt = 0.001
t = 0
g = 9.8
θ = 1 * pi / 180 #angle in radians. As the calculation starts at the negative y-axis, pi is at 90 degrees and 0 is at 270 degrees.
ω = 0

string = cylinder(pos = vec(0, 0, 0), axis = vec(0, -5, 0), radius = 0.05, color = color.cyan)

L = mag(string.axis - string.pos)

bob = sphere(pos = string.axis, radius = 0.5, mass = 0.5, color = color.red, velocity = vec(0, 0, 0 ),
              force = vec(0, 0, 0))
              
T = 2 * pi * sqrt(L / g) #theoretical small-angle approximation of time interval
time = []
angular_velocity = []
Δt = []

gr = graph(title = "Angular displacement", xtitle = "time (s)", ytitle = "Angular displacement")
gr2 = graph(title = "Angular velocity", xtitle = "time (s)", ytitle = "Angular velocity")
g1 = gcurve(graph = gr)
g2 = gcurve(graph = gr2)

while True:
    rate(1e10) #real time execution 1/dt
    
    t += dt
    
    a = (-g / L * sin(θ)) #approximation such that θ<<1 and sin(θ) ~ θ
    
    ω += a * dt #angular velocity update
    
    θ += ω * dt #angular position update
    
    bob.pos = vec(L * sin(θ), -L * cos(θ), 0) #position update
    string.axis = bob.pos
    
    angular_velocity.append(ω)
    
    if ω >= 0.0244343: #maximum angular velocity(frequency) calculated (mass = 0.5, L = 5)
                        # for 5 degs, .122134
                        # for 10 deg, .244036
                        # for 20 deg, .486215
                        # for 30 deg, .724693
                        # for 50 deg, .1.18333
                        # for 70 deg, 1.60601
                        # for 90 deg, 1.9799
        time.append(t) #experimental time at which the angular velocity (frequency) is maximum
        print(t)
    
    if t > 25: #Make sure to set for 25 sec
        break
    
    g1.plot(t, θ * 180 / pi)
    g2.plot(t, ω)

# Initialize a list to store the first value of each interval to eliminate the small overlaps
time_revised = []

# This "for" loop only transfers time intervals that are different enough and exclude similar values
for i in range(len(time)):
    # If it's the first value or the current value is not immediately following the previous one
    if i == 0 or time[i] - time[i-1] > 0.01:
        time_revised.append(time[i]) #making a new list
print("Time invterval revised", time_revised)

for i in range(len(time_revised)): #Here, by taking arithmetric difference between 2 numbers next to each other
                                           #, delta t = duration of one time interval is produced by this iterative execution
    Δt.append(time_revised[-i] - time_revised[-i-1]) #Iterative function starting from position [-1] or the last element in the list
del Δt[0] #Removes the first element in this list, which is not a correct answer. #Removes the first element in this list, which is not a correct answer.
    
data_size_N = int(len(Δt))
mean = sum(Δt) / data_size_N
variance = sum((i - mean)**2 / data_size_N for i in range(data_size_N))
deviation = sqrt(variance)

print("The maximum angular velocity = ", max(angular_velocity))
print("The theoretical small-angle approximation of pendulum period", T)
print("Δt experimental values: ", Δt)
print("Time between each interval", time_revised)
print("Variance", variance)
print("Standard deviation", deviation)
