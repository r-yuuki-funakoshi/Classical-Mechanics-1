from vpython import *
#Web VPython 3.2
from vpython import *
op=0.7
visibility=True
indicator1=arrow(pos=vec(0,0,0), axis=vec(100,0,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.red)
indicator2=arrow(pos=vec(0,0,0), axis=vec(0,100,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.cyan)
indicator3=arrow(pos=vec(0,0,0), axis=vec(0,0,100), shaftwidth=0.1, visible=visibility, opacity=op, color=color.green)

object = sphere(pos = vec(100, -200, 0), radius = 5, mass = 1, velocity = vec(0, 10, 0), speed = 10, color = color.blue, make_trail = True)

kissing_circle_R = 100
angular_momentum = vec(0, 0, 0)
object_momentum = object.mass * object.velocity
W = 0
dt = 1e-2
t = 0

gr1 = graph(title = "Magnitude of the speed of the object", xtitle = "time (s)", ytitle = "|v|")
gr2 = graph(title = "Angular Momentum of the object", xtitle = "time (s)", ytitle = "L = r x p")
gr3 = graph(title = "KE (orange) and Work by force (blue)", xtitle = "time (s)", ytitle = "E")
g1 = gcurve(graph = gr1, color = color.cyan)
g2 = gcurve(graph = gr2, color = color.cyan)
g3_1 = gcurve(graph = gr3, color = color.orange)
g3_2 = gcurve(graph = gr3, color = color.blue)

while True:
    rate(10 / dt)
    t += dt
    
    F_paral = vec(0, 0, 0)
    F_ortho = vec(0, 0, 0)
    
    if object.pos.y < 0 and object.pos.x > 0:
        object.pos += object.velocity * dt
        
        g1.plot(t, mag(object.velocity))
        
        g3_1.plot(t, dot(object.velocity, object.velocity))
        g3_2.plot(t, W)
        
    else:
        F_ortho = (object.mass * object.speed**2 / kissing_circle_R) * (vec(0, 0, 0) - object.pos) / mag(vec(0, 0, 0) - object.pos)
        F_paral = vec(0, 0, 0)
        F = F_paral + F_ortho
        
        object.velocity += (F / object.mass) * dt
        
        W += dot(F, object.velocity) * dt
        object_momentum += F * dt
        angular_momentum = cross((object.pos - vec(0, 0, 0)), object_momentum)
        object.pos += object.velocity * dt
        
        g1.plot(t, mag(object.velocity))
        g2.plot(t, mag(angular_momentum))
        
        g3_1.plot(t, dot(object.velocity, object.velocity))
        g3_2.plot(t, W)
        
    if object.pos.x > 300:
        break
