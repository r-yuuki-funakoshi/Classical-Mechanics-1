from vpython import *
#Web VPython 3.2

from vpython import *

#Definition, sin(theta)=a/d, where 2a is the path difference and d is an atomic diameter of a plane
#on which two rays diffract on two-atomic layer.
#n*lamda(wavelength)=2*d*sin(theta) theta is the angle of incident

#Here, assume d is the radius of the atoms involved in the two-layer sheet.
d=0.5

layer_atom1=sphere(pos=vec(0,0,0), radius=d, color=color.red, opacity=0.5)
layer_atom2=sphere(pos=vec(2*d,0,0), radius=d, color=color.red, opacity=0.5)
layer_atom3=sphere(pos=vec(-2*d,0,0), radius=d, color=color.red, opacity=0.5)
layer_atom4=sphere(pos=vec(0,-2*d,0), radius=d, color=color.red, opacity=0.5)
layer_atom5=sphere(pos=vec(2*d,-2*d,0), radius=d, color=color.red, opacity=0.5)
layer_atom6=sphere(pos=vec(-2*d,-2*d,0), radius=d, color=color.red, opacity=0.5)


ray_1=sphere(pos=vec(-sqrt(2),1.5,0), radius=0.05, color=color.yellow, make_trail=True)
ray_2=sphere(pos=vec(ray_1.pos.x-1/sqrt(2),ray_1.pos.y-1/sqrt(2),0), radius=0.05, color=color.yellow, make_trail=True)

v1=vec(sqrt(2),-1,0)
v2=vec(sqrt(2),-1,0)
dt=0.01
t=0

for t in range(0,300):
    rate(100)
    d=d+dt
    ray_1.pos=ray_1.pos+v1*dt
    ray_2.pos=ray_2.pos+v2*dt
    if ray_1.pos.x+ray_1.radius > layer_atom1.pos.x:
        v1=vec(sqrt(2),1,0)
    if ray_2.pos.x+ray_2.radius > layer_atom4.pos.x:
        v2=v1
  
#At the end of this program, the difference in the positions of two photon rays 
#demonstrates the path difference 2a in Bragg's Law.

   
