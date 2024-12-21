from vpython import *
#Web VPython 3.2
from vpython import *
#Axis indicator
#Opacity and visibility
op=0.7
visibility=True
indicator1=arrow(pos=vec(0,0,0), axis=vec(100,0,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.red)
indicator2=arrow(pos=vec(0,0,0), axis=vec(0,100,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.cyan)
indicator3=arrow(pos=vec(0,0,0), axis=vec(0,0,100), shaftwidth=0.1, visible=visibility, opacity=op, color=color.green)

#camera position and axis (axis is the object of interest with DIRECTION, and position is the observer's position)
scene.camera.pos=vec(2,0,2)
scene.center=vec(2,0,0)

#Two objects as spheres at the origin
particle_1=sphere(pos=vec(0,0,0), radius=0.2, color=color.blue, make_trail=True)
particle_2=sphere(pos=vec(0,0,0), radius=0.2, color=color.orange, make_trail=True)

#Determine the angles at which the particles move
theta1=pi/3 #60 degree
theta2=pi/4 #45 degree

#Here, the speed or the magnitude of the velocity |v| is...
v1=8
v2=10
#Where the unit vectors of them are...
# v^=(cos(theta), sin(theta), 0) on the xy plane
#Thus the velocity vector is v=|v|*v^
velocity1=vec(v1*cos(theta1), v1*sin(theta1), 0)
velocity2=vec(v2*cos(theta2), v2*sin(theta2), 0)

#Update the position and velocity with the momentum principle using a loop iteration
# dp=F*dt and thus m*dv=F*dt
# Where g=Fg/m..."negative" acceleration
t=0
dt=0.01
g=-10

gr1=graph(title="x-component of velocity", xtitle="t", ytitle="Vx")
gr2=graph(title="y-component of velocity", xtitle="t", ytitle="Vy", ymin=-20)
g1=gcurve(graph=gr1, color=color.red)
g2=gcurve(graph=gr2, color=color.cyan)

for t in range(0, 200):
    rate(45)
    t+=1
    #Normal positional updates on the xy plane
    particle_1.pos=particle_1.pos+velocity1*dt
    particle_2.pos=particle_2.pos+velocity2*dt
    
    #Only for one object, gravitational force...velocity in terms of y-axis is influenced
    velocity1.y=velocity1.y+g*dt
    
    g1.plot(t, velocity1.x)
    g2.plot(t, velocity1.y)
    
   

    
