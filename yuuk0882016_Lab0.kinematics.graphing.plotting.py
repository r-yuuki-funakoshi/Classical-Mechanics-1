from vpython import *
#Web VPython 3.2

from vpython import *

#camera position and axis (axis is the object of interest with DIRECTION, and position is the observer's position)
scene.autoscale=False
scene.camera.pos=vec(4,0,20)
scene.center.pos=vec(4,0,0)
#Axis indicator
#Opacity and visibility
op=0.7
visibility=True
indicator1=arrow(pos=vec(0,0,0), axis=vec(100,0,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.red)
indicator2=arrow(pos=vec(0,0,0), axis=vec(0,100,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.cyan)
indicator3=arrow(pos=vec(0,0,0), axis=vec(0,0,100), shaftwidth=0.1, visible=visibility, opacity=op, color=color.green)



particle3=sphere(pos=vec(0,0,0), radius=0.5, color=color.cyan, make_trail=True)

theta=pi/2 #the angle theta at which the x displacemnt is the largest
v=10 #speed or |v|
velocity=vec(v*cos(theta), v*sin(theta), 0) #unit vector(direction times magnitude)
g=-10 #gravitational acceleration such that Fg/m=|g|~10

gr1=graph(title="Kinematics", xtitle="x", ytitle="y") #Kinematics
gr2=graph(title="Comparison: Vx", xtitle="t", ytitle="Vx") #Velocity components comparison
gr3=graph(title="Camparison: Vy", xtitle="t", ytitle="Vy")
gl=gcurve(graph=gr1, color=color.red)
g2=gcurve(graph=gr2, color=color.red)
g3=gcurve(graph=gr3, color=color.red)


#Here, the kinematics equation is introduced to the positional vector of y component
t=0
dt=0.001
while particle3.pos.y >= 0: #the object stops when it hits the "ground"
    rate(200)
    t+=dt
    particle3.pos.x=velocity.x*t
    particle3.pos.y=velocity.y*t+(1/2)*g*t**2 #Only y component experiences the gravitational force
    gl.plot(particle3.pos.x, particle3.pos.y) #Plotting
    g2.plot(t, velocity.x)
    g3.plot(t, velocity.y+g*t)
    
print("The final distance of the object from the origin under the influence of gravity=", particle3.pos.x)