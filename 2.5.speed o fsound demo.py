from vpython import *
op=0.7
visibility=True
indicator1=arrow(pos=vec(0,0,0), axis=vec(100,0,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.red)
indicator2=arrow(pos=vec(0,0,0), axis=vec(0,100,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.cyan)
indicator3=arrow(pos=vec(0,0,0), axis=vec(0,0,100), shaftwidth=0.1, visible=visibility, opacity=op, color=color.green)

# defining properties of a microscale solid as cube
d = 2 #distance between adjascent nuclei
r = 0.5 #atomic radius ~~ 1 angstrom
object_mass = 1e-10

#Intralayer springs/bonds
#1st layer
spring = helix(pos = vec(0, 0, 0), axis = vec(d, 0, 0), radius = 0.25, thickness = 0.01, #This spring has its position at (0, 0, 0)
                coil = 8, k_stiffness = 40)
spring2 = helix(pos = spring.axis, axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring3 = helix(pos = vec(0, 0, d), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring4 = helix(pos = vec(d, 0, d), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring5 = helix(pos = vec(0, 0, 2*d), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring6 = helix(pos = vec(d, 0, 2*d), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring7 = helix(pos = spring.pos, axis = vec(0, 0, d), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring8 = helix(pos = spring2.pos, axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring9 = helix(pos = vec(2*d, 0, 0), axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring10 = helix(pos = spring3.pos, axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring11 = helix(pos = spring4.pos, axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring12 = helix(pos = vec(2*d, 0, d), axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)

#2nd layer
spring13 = helix(pos = vec(0, -d, 0), axis = vec(d, 0, 0), radius = 0.25, thickness = 0.01, #This spring has its position at (0, 0, 0)
                coil = 8, k_stiffness = 40)
spring14 = helix(pos = vec(d, -d, 0), axis = spring13.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring15 = helix(pos = vec(0, -d, d), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring16 = helix(pos = vec(d, -d, d), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring17 = helix(pos = vec(0, -d, 2*d), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring18 = helix(pos = vec(d, -d, 2*d), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring19 = helix(pos = spring13.pos, axis = vec(0, 0, d), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring20 = helix(pos = spring14.pos, axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring21 = helix(pos = vec(2*d, -d, 0), axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring22 = helix(pos = spring15.pos, axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring23 = helix(pos = spring16.pos, axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring24 = helix(pos = vec(2*d, -d, d), axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)

#3rd layer
spring25 = helix(pos = vec(0, -2*d, 0), axis = vec(d, 0, 0), radius = 0.25, thickness = 0.01, #This spring has its position at (0, 0, 0)
                coil = 8, k_stiffness = 40)
spring26 = helix(pos = vec(d, -2*d, 0), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring27 = helix(pos = vec(0, -2*d, d), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring28 = helix(pos = vec(d, -2*d, d), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring29 = helix(pos = vec(0, -2*d, 2*d), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring30 = helix(pos = vec(d, -2*d, 2*d), axis = spring.axis, radius = 0.25, thickness = 0.01,
                coil = 8, k_stiffness = 40)
spring31 = helix(pos = spring25.pos, axis = vec(0, 0, d), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring32 = helix(pos = spring26.pos, axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring33 = helix(pos = vec(2*d, -2*d, 0), axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring34 = helix(pos = spring27.pos, axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring35 = helix(pos = spring28.pos, axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring36 = helix(pos = vec(2*d, -2*d, d), axis = spring7.axis, radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)

#object (atom) first layer
object = sphere(pos = spring.pos, radius = r, color = color.red, velocity = vec(1, 1, 1), force = vec(0, 0, 0))
object2 = sphere(pos = spring2.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object3 = sphere(pos = spring9.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object4 = sphere(pos = spring3.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object5 = sphere(pos = spring4.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object6 = sphere(pos = spring12.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object7 = sphere(pos = spring5.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object8 = sphere(pos = spring6.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object9 = sphere(pos = vec(2*d, 0, 2*d), radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
                
#object second layer
object10 = sphere(pos = spring13.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object11 = sphere(pos = spring14.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object12 = sphere(pos = spring21.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object13 = sphere(pos = spring15.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object14 = sphere(pos = vec(-1, -1, -1), radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object15 = sphere(pos = spring24.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object16 = sphere(pos = spring17.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object17 = sphere(pos = spring18.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object18 = sphere(pos = vec(2*d, -d, 2*d), radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))

#object third layer
object19 = sphere(pos = spring25.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object20 = sphere(pos = spring26.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object21 = sphere(pos = spring33.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object22 = sphere(pos = spring27.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object23 = sphere(pos = spring28.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object24 = sphere(pos = spring36.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object25 = sphere(pos = spring29.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object26 = sphere(pos = spring30.pos, radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))
object27 = sphere(pos = vec(2*d, -2*d, 2*d), radius = r, color = color.red, velocity = vec(0, 0, 0), force = vec(0, 0, 0))

#Interlayer bonds
spring_1 = helix(pos = spring.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_2 = helix(pos = spring2.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_3 = helix(pos = spring9.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_4 = helix(pos = spring3.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_5 = helix(pos = spring4.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_6 = helix(pos = spring12.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_7 = helix(pos = spring5.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_8 = helix(pos = spring6.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_9 = helix(pos = object9.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_10 = helix(pos = spring13.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_11 = helix(pos = spring14.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_12 = helix(pos = spring21.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_13 = helix(pos = spring15.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_14 = helix(pos = spring16.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_15 = helix(pos = spring24.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_16 = helix(pos = spring17.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_17 = helix(pos = spring18.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)
spring_18 = helix(pos = object18.pos, axis = vec(0, -d, 0), radius = 0.25, thickness = 0.01, coil = 8, k_stiffness = 40)

equilibrium_pos = spring.axis - spring.pos
equilibrium_pos2 = spring2.axis - spring2.pos
equilibrium_pos3 = spring3.axis - spring3.pos
equilibrium_pos4 = spring4.axis - spring4.pos
equilibrium_pos5 = spring5.axis - spring5.pos
equilibrium_pos6 = spring6.axis - spring6.pos
equilibrium_pos7 = spring7.axis - spring7.pos
equilibrium_pos8 = spring8.axis - spring8.pos
equilibrium_pos9 = spring9.axis - spring9.pos
equilibrium_pos10 = spring10.axis - spring10.pos
equilibrium_pos11 = spring11.axis - spring11.pos
equilibrium_pos12 = spring12.axis - spring12.pos
equilibrium_pos13 = spring13.axis - spring13.pos
equilibrium_pos14 = spring14.axis - spring14.pos
equilibrium_pos15 = spring15.axis - spring15.pos
equilibrium_pos16 = spring16.axis - spring16.pos
equilibrium_pos17 = spring17.axis - spring17.pos
equilibrium_pos18 = spring18.axis - spring18.pos
equilibrium_pos19 = spring19.axis - spring19.pos
equilibrium_pos20 = spring20.axis - spring20.pos
equilibrium_pos21 = spring21.axis - spring21.pos
equilibrium_pos22 = spring22.axis - spring22.pos
equilibrium_pos23 = spring23.axis - spring23.pos
equilibrium_pos24 = spring24.axis - spring24.pos
equilibrium_pos25 = spring25.axis - spring25.pos
equilibrium_pos26 = spring26.axis - spring26.pos
equilibrium_pos27 = spring27.axis - spring27.pos
equilibrium_pos28 = spring28.axis - spring28.pos
equilibrium_pos29 = spring29.axis - spring29.pos
equilibrium_pos30 = spring30.axis - spring30.pos
equilibrium_pos31 = spring31.axis - spring31.pos
equilibrium_pos32 = spring32.axis - spring32.pos
equilibrium_pos33 = spring33.axis - spring33.pos
equilibrium_pos34 = spring34.axis - spring34.pos
equilibrium_pos35 = spring35.axis - spring35.pos
equilibrium_pos36 = spring36.axis - spring36.pos
equilibrium_pos_1 = spring_1.axis - spring_1.pos
equilibrium_pos_2 = spring_2.axis - spring_2.pos
equilibrium_pos_3 = spring_3.axis - spring_3.pos
equilibrium_pos_4 = spring_4.axis - spring_4.pos
equilibrium_pos_5 = spring_5.axis - spring_5.pos
equilibrium_pos_6 = spring_6.axis - spring_6.pos
equilibrium_pos_7 = spring_7.axis - spring_7.pos
equilibrium_pos_8 = spring_8.axis - spring_8.pos
equilibrium_pos_9 = spring_9.axis - spring_9.pos
equilibrium_pos_10 = spring_10.axis - spring_10.pos
equilibrium_pos_11 = spring_11.axis - spring_11.pos
equilibrium_pos_12 = spring_12.axis - spring_12.pos
equilibrium_pos_13 = spring_13.axis - spring_13.pos
equilibrium_pos_14 = spring_14.axis - spring_14.pos
equilibrium_pos_15 = spring_15.axis - spring_15.pos
equilibrium_pos_16 = spring_16.axis - spring_16.pos
equilibrium_pos_17 = spring_17.axis - spring_17.pos
equilibrium_pos_18 = spring_18.axis - spring_18.pos

dt = 0.001
t = 0


while True:
    rate(1/dt)
    t += 1
    #First layer atoms and forces #BE CAREFUL EACH OBJECT NUMBER IS UNIQUE 
    object.force = -spring.k_stiffness * ((mag(object.pos - spring.pos) - mag(equilibrium_pos)) * (object.pos - spring.pos) / mag(object.pos - spring.pos) #spring 1
    + (mag(object.pos - spring7.pos) - mag(equilibrium_pos7)) * (object.pos - spring7.pos) / mag(object.pos - spring7.pos)                                 #spring 7
    + (mag(object.pos - spring_1.pos) - mag(equilibrium_pos_1)) * (object.pos - spring_1.pos) / mag(object.pos - spring_1.pos))                            #spring _1
    
    object2.force = -spring.k_stiffness * ((mag(object2.pos - spring.pos) - mag(equilibrium_pos)) * (object2.pos - spring.pos) / mag(object2.pos - spring.pos)     #spring 1
    + (mag(object2.pos - spring2.pos) - mag(equilibrium_pos2)) * (object2.pos - spring2.pos) / mag(object2.pos - spring2.pos)                                      #spring 2
    + (mag(object2.pos - spring8.pos) - mag(equilibrium_pos8)) * (object2.pos - spring8.pos) / mag(object2.pos - spring8.pos)                                      #spring 8
    + (mag(object2.pos - spring_2.pos) - mag(equilibrium_pos_2)) * (object2.pos - spring_2.pos) / mag(object2.pos - spring_2.pos))                                 #spring _2
    
    object3.force = -spring.k_stiffness * ((mag(object3.pos - spring2.pos) - mag(equilibrium_pos2)) * (object3.pos - spring2.pos) / mag(object3.pos - spring2.pos) #spring 2
    + (mag(object3.pos - spring9.pos) - mag(equilibrium_pos9)) * (object3.pos - spring9.pos) / mag(object3.pos - spring9.pos)                                      #spring 9
    + (mag(object3.pos - spring_3.pos) - mag(equilibrium_pos_3)) * (object3.pos - spring_3.pos) / mag(object3.pos - spring_3.pos))                                 #spring _3
    
    object4.force = -spring.k_stiffness * ((mag(object4.pos - spring3.pos) - mag(equilibrium_pos3)) * (object4.pos - spring3.pos) / mag(object4.pos - spring3.pos) #spring 3
    + (mag(object4.pos - spring7.pos) - mag(equilibrium_pos7)) * (object4.pos - spring7.pos) / mag(object4.pos - spring7.pos)                                  #spring 7
    + (mag(object4.pos - spring10.pos) - mag(equilibrium_pos10)) * (object4.pos - spring10.pos) / mag(object4.pos - spring10.pos)                                  #spring 10
    + (mag(object4.pos - spring_4.pos) - mag(equilibrium_pos_4)) * (object4.pos - spring_4.pos) / mag(object4.pos - spring_4.pos))                             #spring _4
    
    object5.force = -spring.k_stiffness * ((mag(object5.pos - spring3.pos) - mag(equilibrium_pos)) * (object5.pos - spring3.pos) / mag(object5.pos - spring3.pos) #spring 3
    + (mag(object5.pos - spring4.pos) - mag(equilibrium_pos4)) * (object5.pos - spring4.pos) / mag(object5.pos - spring4.pos)                                  #spring 4
    + (mag(object5.pos - spring11.pos) - mag(equilibrium_pos11)) * (object5.pos - spring11.pos) / mag(object5.pos - spring11.pos)                                  #spring 11
    + (mag(object5.pos - spring8.pos) - mag(equilibrium_pos8)) * (object5.pos - spring8.pos) / mag(object5.pos - spring8.pos)                                  #spring 8
    + (mag(object5.pos - spring_5.pos) - mag(equilibrium_pos_5)) * (object5.pos - spring_5.pos) / mag(object5.pos - spring_5.pos))                             #spring _5     
    
    object6.force = -spring.k_stiffness * ((mag(object6.pos - spring4.pos) - mag(equilibrium_pos4)) * (object6.pos - spring4.pos) / mag(object6.pos - spring4.pos) #4
    + (mag(object6.pos - spring9.pos) - mag(equilibrium_pos9)) * (object6.pos - spring9.pos) / mag(object6.pos - spring9.pos) #9
    + (mag(object6.pos - spring12.pos) - mag(equilibrium_pos12)) * (object6.pos - spring12.pos) / mag(object6.pos - spring12.pos) #12
    + (mag(object6.pos - spring_6.pos) - mag(equilibrium_pos_6)) * (object6.pos - spring_6.pos) / mag(object6.pos - spring_6.pos)) #_6
    
    object7.force = -spring.k_stiffness * ((mag(object7.pos - spring5.pos) - mag(equilibrium_pos5)) * (object7.pos - spring5.pos) / mag(object7.pos - spring5.pos)  #5
    + (mag(object7.pos - spring10.pos) - mag(equilibrium_pos10)) * (object7.pos - spring10.pos) / mag(object7.pos - spring10.pos) #10
    + (mag(object7.pos - spring_7.pos) - mag(equilibrium_pos_7)) * (object7.pos - spring_7.pos) / mag(object7.pos - spring_7.pos)) #_7
    
    object8.force = -spring.k_stiffness * ((mag(object8.pos - spring5.pos) - mag(equilibrium_pos5)) * (object8.pos - spring5.pos) / mag(object8.pos - spring5.pos) #5
    + (mag(object8.pos - spring6.pos) - mag(equilibrium_pos6)) * (object8.pos - spring6.pos) / mag(object8.pos - spring6.pos)#6
    + (mag(object8.pos - spring11.pos) - mag(equilibrium_pos11)) * (object8.pos - spring11.pos) / mag(object8.pos - spring11.pos)#11
    + (mag(object8.pos - spring_8.pos) - mag(equilibrium_pos_8)) * (object8.pos - spring_8.pos) / mag(object8.pos - spring_8.pos))#_8
    
    object9.force = -spring.k_stiffness * ((mag(object9.pos - spring6.pos) - mag(equilibrium_pos6)) * (object9.pos - spring6.pos) / mag(object9.pos - spring6.pos) #6
    + (mag(object9.pos - spring12.pos) - mag(equilibrium_pos12)) * (object9.pos - spring12.pos) / mag(object9.pos - spring12.pos) #12
    + (mag(object9.pos - spring_9.pos) - mag(equilibrium_pos_9)) * (object9.pos - spring_9.pos) / mag(object9.pos - spring_9.pos))#_9
    
    #Middle layer atoms and forces
    object10.force = -spring.k_stiffness * ((mag(object10.pos - spring13.pos) - mag(equilibrium_pos13)) * (object10.pos - spring13.pos) / mag(object10.pos - spring13.pos) 
    + (mag(object10.pos - spring19.pos) - mag(equilibrium_pos19)) * (object10.pos - spring19.pos) / mag(object10.pos - spring19.pos)
    + (mag(object10.pos - spring_1.pos) - mag(equilibrium_pos_1)) * (object10.pos - spring_1.pos) / mag(object10.pos - spring_1.pos)
    + (mag(object10.pos - spring_10.pos) - mag(equilibrium_pos_10)) * (object10.pos - spring_10.pos) / mag(object10.pos - spring_10.pos))                            
    
    object11.force = -spring.k_stiffness * ((mag(object11.pos - spring13.pos) - mag(equilibrium_pos13)) * (object11.pos - spring13.pos) / mag(object11.pos - spring13.pos)     
    + (mag(object11.pos - spring14.pos) - mag(equilibrium_pos14)) * (object14.pos - spring2.pos) / mag(object14.pos - spring2.pos)                                      
    + (mag(object11.pos - spring20.pos) - mag(equilibrium_pos20)) * (object11.pos - spring20.pos) / mag(object11.pos - spring20.pos)
    + (mag(object11.pos - spring_11.pos) - mag(equilibrium_pos_11)) * (object11.pos - spring_11.pos) / mag(object11.pos - spring_11.pos)
    + (mag(object11.pos - spring_2.pos) - mag(equilibrium_pos_2)) * (object11.pos - spring_2.pos) / mag(object11.pos - spring_2.pos))                                 
    
    object12.force = -spring.k_stiffness * ((mag(object12.pos - spring21.pos) - mag(equilibrium_pos21)) * (object12.pos - spring21.pos) / mag(object12.pos - spring21.pos)
    + (mag(object12.pos - spring14.pos) - mag(equilibrium_pos14)) * (object12.pos - spring14.pos) / mag(object12.pos - spring14.pos)
    + (mag(object12.pos - spring_12.pos) - mag(equilibrium_pos_12)) * (object12.pos - spring_12.pos) / mag(object12.pos - spring_12.pos)
    + (mag(object12.pos - spring_3.pos) - mag(equilibrium_pos_3)) * (object12.pos - spring_3.pos) / mag(object12.pos - spring_3.pos))                                 
    
    object13.force = -spring.k_stiffness * ((mag(object13.pos - spring15.pos) - mag(equilibrium_pos15)) * (object13.pos - spring15.pos) / mag(object13.pos - spring15.pos) 
    + (mag(object13.pos - spring19.pos) - mag(equilibrium_pos19)) * (object13.pos - spring19.pos) / mag(object13.pos - spring19.pos)                                  
    + (mag(object13.pos - spring22.pos) - mag(equilibrium_pos22)) * (object13.pos - spring22.pos) / mag(object13.pos - spring22.pos)
    + (mag(object13.pos - spring_13.pos) - mag(equilibrium_pos_13)) * (object13.pos - spring_13.pos) / mag(object13.pos - spring_13.pos)
    + (mag(object13.pos - spring_4.pos) - mag(equilibrium_pos_4)) * (object13.pos - spring_4.pos) / mag(object13.pos - spring_4.pos))                             
    
    object14.force = -spring.k_stiffness * ((mag(object14.pos - spring15.pos) - mag(equilibrium_pos15)) * (object14.pos - spring15.pos) / mag(object14.pos - spring15.pos) 
    + (mag(object14.pos - spring16.pos) - mag(equilibrium_pos16)) * (object14.pos - spring16.pos) / mag(object14.pos - spring16.pos)                                  
    + (mag(object14.pos - spring33.pos) - mag(equilibrium_pos33)) * (object14.pos - spring33.pos) / mag(object14.pos - spring33.pos)                                  
    + (mag(object14.pos - spring20.pos) - mag(equilibrium_pos20)) * (object14.pos - spring20.pos) / mag(object14.pos - spring20.pos)
    + (mag(object14.pos - spring_14.pos) - mag(equilibrium_pos_14)) * (object14.pos - spring_14.pos) / mag(object14.pos - spring_14.pos)
    + (mag(object14.pos - spring_5.pos) - mag(equilibrium_pos_5)) * (object14.pos - spring_5.pos) / mag(object14.pos - spring_5.pos))                                 
    
    object15.force = -spring.k_stiffness * ((mag(object15.pos - spring16.pos) - mag(equilibrium_pos16)) * (object15.pos - spring16.pos) / mag(object15.pos - spring16.pos) 
    + (mag(object15.pos - spring21.pos) - mag(equilibrium_pos21)) * (object15.pos - spring21.pos) / mag(object15.pos - spring21.pos) 
    + (mag(object15.pos - spring24.pos) - mag(equilibrium_pos24)) * (object15.pos - spring24.pos) / mag(object15.pos - spring24.pos)
    + (mag(object15.pos - spring_6.pos) - mag(equilibrium_pos_6)) * (object15.pos - spring_6.pos) / mag(object15.pos - spring_6.pos)
    + (mag(object15.pos - spring_15.pos) - mag(equilibrium_pos_15)) * (object15.pos - spring_15.pos) / mag(object15.pos - spring_15.pos)) 
    
    object16.force = -spring.k_stiffness * ((mag(object16.pos - spring17.pos) - mag(equilibrium_pos17)) * (object16.pos - spring17.pos) / mag(object16.pos - spring17.pos)  
    + (mag(object16.pos - spring22.pos) - mag(equilibrium_pos22)) * (object16.pos - spring22.pos) / mag(object16.pos - spring22.pos)
    + (mag(object16.pos - spring_16.pos) - mag(equilibrium_pos_16)) * (object16.pos - spring_16.pos) / mag(object16.pos - spring_16.pos)
    + (mag(object16.pos - spring_7.pos) - mag(equilibrium_pos_7)) * (object16.pos - spring_7.pos) / mag(object16.pos - spring_7.pos)) 
    
    object17.force = -spring.k_stiffness * ((mag(object17.pos - spring17.pos) - mag(equilibrium_pos17)) * (object17.pos - spring17.pos) / mag(object17.pos - spring17.pos) 
    + (mag(object17.pos - spring18.pos) - mag(equilibrium_pos18)) * (object17.pos - spring18.pos) / mag(object17.pos - spring18.pos)
    + (mag(object17.pos - spring23.pos) - mag(equilibrium_pos23)) * (object17.pos - spring23.pos) / mag(object17.pos - spring23.pos)
    + (mag(object17.pos - spring_17.pos) - mag(equilibrium_pos_17)) * (object17.pos - spring_17.pos) / mag(object17.pos - spring_17.pos)
    + (mag(object17.pos - spring_8.pos) - mag(equilibrium_pos_8)) * (object17.pos - spring_8.pos) / mag(object17.pos - spring_8.pos))
    
    object18.force = -spring.k_stiffness * ((mag(object18.pos - spring18.pos) - mag(equilibrium_pos18)) * (object18.pos - spring18.pos) / mag(object18.pos - spring18.pos) 
    + (mag(object18.pos - spring24.pos) - mag(equilibrium_pos24)) * (object18.pos - spring24.pos) / mag(object18.pos - spring24.pos)
    + (mag(object18.pos - spring_18.pos) - mag(equilibrium_pos_18)) * (object18.pos - spring_18.pos) / mag(object18.pos - spring_18.pos)
    + (mag(object18.pos - spring_9.pos) - mag(equilibrium_pos_9)) * (object18.pos - spring_9.pos) / mag(object18.pos - spring_9.pos))
    
    #the bottom layer forces
    object19.force = -spring.k_stiffness * ((mag(object19.pos - spring25.pos) - mag(equilibrium_pos25)) * (object19.pos - spring25.pos) / mag(object19.pos - spring25.pos) 
    + (mag(object19.pos - spring31.pos) - mag(equilibrium_pos31)) * (object19.pos - spring31.pos) / mag(object19.pos - spring31.pos)                                 
    + (mag(object19.pos - spring_10.pos) - mag(equilibrium_pos_10)) * (object19.pos - spring_10.pos) / mag(object19.pos - spring_10.pos))                            
    
    object20.force = -spring.k_stiffness * ((mag(object20.pos - spring25.pos) - mag(equilibrium_pos25)) * (object20.pos - spring25.pos) / mag(object20.pos - spring25.pos)     
    + (mag(object20.pos - spring26.pos) - mag(equilibrium_pos26)) * (object20.pos - spring26.pos) / mag(object20.pos - spring26.pos)                                      
    + (mag(object20.pos - spring32.pos) - mag(equilibrium_pos32)) * (object20.pos - spring32.pos) / mag(object20.pos - spring32.pos)                                     
    + (mag(object20.pos - spring_11.pos) - mag(equilibrium_pos_11)) * (object20.pos - spring_11.pos) / mag(object20.pos - spring_11.pos))                                
    
    object21.force = -spring.k_stiffness * ((mag(object21.pos - spring26.pos) - mag(equilibrium_pos26)) * (object21.pos - spring26.pos) / mag(object21.pos - spring26.pos) 
    + (mag(object21.pos - spring33.pos) - mag(equilibrium_pos33)) * (object21.pos - spring33.pos) / mag(object21.pos - spring33.pos)                                      
    + (mag(object21.pos - spring_12.pos) - mag(equilibrium_pos_12)) * (object21.pos - spring_12.pos) / mag(object21.pos - spring_12.pos))                                 
    
    object22.force = -spring.k_stiffness * ((mag(object22.pos - spring27.pos) - mag(equilibrium_pos27)) * (object22.pos - spring27.pos) / mag(object22.pos - spring27.pos) 
    + (mag(object22.pos - spring31.pos) - mag(equilibrium_pos31)) * (object22.pos - spring31.pos) / mag(object22.pos - spring31.pos)                                  
    + (mag(object22.pos - spring34.pos) - mag(equilibrium_pos34)) * (object22.pos - spring34.pos) / mag(object22.pos - spring34.pos)                                  
    + (mag(object22.pos - spring_13.pos) - mag(equilibrium_pos_13)) * (object22.pos - spring_13.pos) / mag(object22.pos - spring_13.pos))                             
    
    object23.force = -spring.k_stiffness * ((mag(object23.pos - spring27.pos) - mag(equilibrium_pos27)) * (object23.pos - spring27.pos) / mag(object23.pos - spring27.pos) 
    + (mag(object23.pos - spring32.pos) - mag(equilibrium_pos32)) * (object23.pos - spring32.pos) / mag(object23.pos - spring32.pos)                                 
    + (mag(object23.pos - spring28.pos) - mag(equilibrium_pos28)) * (object23.pos - spring28.pos) / mag(object23.pos - spring28.pos)                                  
    + (mag(object23.pos - spring35.pos) - mag(equilibrium_pos35)) * (object23.pos - spring35.pos) / mag(object23.pos - spring35.pos)                                  
    + (mag(object23.pos - spring_14.pos) - mag(equilibrium_pos_14)) * (object23.pos - spring_14.pos) / mag(object23.pos - spring_14.pos))                             
    
    object24.force = -spring.k_stiffness * ((mag(object24.pos - spring28.pos) - mag(equilibrium_pos28)) * (object24.pos - spring28.pos) / mag(object24.pos - spring28.pos) 
    + (mag(object24.pos - spring33.pos) - mag(equilibrium_pos33)) * (object24.pos - spring33.pos) / mag(object24.pos - spring33.pos) 
    + (mag(object24.pos - spring36.pos) - mag(equilibrium_pos36)) * (object24.pos - spring36.pos) / mag(object24.pos - spring36.pos) 
    + (mag(object24.pos - spring_15.pos) - mag(equilibrium_pos_15)) * (object24.pos - spring_15.pos) / mag(object24.pos - spring_15.pos)) 
    
    object25.force = -spring.k_stiffness * ((mag(object25.pos - spring29.pos) - mag(equilibrium_pos29)) * (object25.pos - spring29.pos) / mag(object25.pos - spring29.pos)  
    + (mag(object25.pos - spring34.pos) - mag(equilibrium_pos34)) * (object25.pos - spring34.pos) / mag(object25.pos - spring34.pos) 
    + (mag(object25.pos - spring_16.pos) - mag(equilibrium_pos_16)) * (object25.pos - spring_16.pos) / mag(object25.pos - spring_16.pos)) 
    
    object26.force = -spring.k_stiffness * ((mag(object26.pos - spring29.pos) - mag(equilibrium_pos29)) * (object26.pos - spring29.pos) / mag(object26.pos - spring29.pos) 
    + (mag(object26.pos - spring30.pos) - mag(equilibrium_pos30)) * (object26.pos - spring30.pos) / mag(object26.pos - spring30.pos)
    + (mag(object26.pos - spring35.pos) - mag(equilibrium_pos35)) * (object26.pos - spring35.pos) / mag(object26.pos - spring35.pos)
    + (mag(object26.pos - spring_17.pos) - mag(equilibrium_pos_17)) * (object26.pos - spring_17.pos) / mag(object26.pos - spring_17.pos))
    
    object27.force = -spring.k_stiffness * ((mag(object27.pos - spring30.pos) - mag(equilibrium_pos30)) * (object27.pos - spring30.pos) / mag(object27.pos - spring30.pos) 
    + (mag(object27.pos - spring36.pos) - mag(equilibrium_pos36)) * (object27.pos - spring36.pos) / mag(object27.pos - spring36.pos) 
    + (mag(object27.pos - spring_18.pos) - mag(equilibrium_pos_18)) * (object27.pos - spring_18.pos) / mag(object27.pos - spring_18.pos))
    
    #Velocity updates
    object.velocity += (object.force/object_mass) * dt
    object2.velocity += (object2.force/object_mass) * dt
    object3.velocity += (object3.force/object_mass) * dt
    object4.velocity += (object4.force/object_mass) * dt
    object5.velocity += (object5.force/object_mass) * dt
    object6.velocity += (object6.force/object_mass) * dt
    object7.velocity += (object7.force/object_mass) * dt
    object8.velocity += (object8.force/object_mass) * dt
    object9.velocity += (object9.force/object_mass) * dt
    object10.velocity += (object10.force/object_mass) * dt
    object11.velocity += (object11.force/object_mass) * dt
    object12.velocity += (object12.force/object_mass) * dt
    object13.velocity += (object13.force/object_mass) * dt
    object14.velocity += (object14.force/object_mass) * dt
    object15.velocity += (object15.force/object_mass) * dt
    object16.velocity += (object16.force/object_mass) * dt
    object17.velocity += (object17.force/object_mass) * dt
    object18.velocity += (object18.force/object_mass) * dt
    object19.velocity += (object19.force/object_mass) * dt
    object20.velocity += (object20.force/object_mass) * dt
    object21.velocity += (object21.force/object_mass) * dt
    object22.velocity += (object22.force/object_mass) * dt
    object23.velocity += (object23.force/object_mass) * dt
    object24.velocity += (object24.force/object_mass) * dt
    object25.velocity += (object25.force/object_mass) * dt
    object26.velocity += (object26.force/object_mass) * dt
    object27.velocity += (object27.force/object_mass) * dt
    
    #position updates
    object.pos += object.velocity * dt
    object2.pos += object2.velocity * dt
    object3.pos += object3.velocity * dt
    object4.pos += object4.velocity * dt
    object5.pos += object5.velocity * dt
    object6.pos += object6.velocity * dt
    object7.pos += object7.velocity * dt
    object8.pos += object8.velocity * dt
    object9.pos += object9.velocity * dt
    object10.pos += object10.velocity * dt
    object11.pos += object11.velocity * dt
    object12.pos += object12.velocity * dt
    object13.pos += object13.velocity * dt
    object14.pos += object14.velocity * dt
    object15.pos += object15.velocity * dt
    object16.pos += object16.velocity * dt
    object17.pos += object17.velocity * dt
    object18.pos += object18.velocity * dt
    object19.pos += object19.velocity * dt
    object20.pos += object20.velocity * dt
    object21.pos += object21.velocity * dt
    object22.pos += object22.velocity * dt
    object23.pos += object23.velocity * dt
    object24.pos += object24.velocity * dt
    object25.pos += object25.velocity * dt
    object26.pos += object26.velocity * dt
    object27.pos += object27.velocity * dt
    
    #spring movement along with atoms
    spring.pos = object.pos
    spring.axis = object2.pos
    spring2.pos = object2.pos
    spring2.axis = object3.pos
    spring3.pos = object4.pos
    spring3.axis = object5.pos
    spring4.pos = object5.pos
    spring4.axis = object6.pos
    spring5.pos = object10.pos
    spring5.axis = object8.pos
    spring6.pos = object8.pos
    spring6.axis = object9.pos
    spring7.pos = object.pos
    spring7.axis = object4.pos
    spring8.pos = object2.pos
    spring8.axis = object5.pos
    spring9.pos = object3.pos
    spring9.axis = object6.pos
    spring10.pos = object4.pos
    spring10.axis = object7.pos
    spring11.pos = object5.pos
    spring11.axis = object8.pos
    spring12.pos = object6.pos
    spring12.axis = object9.pos
    
    
    spring13.pos = object10.pos
    spring13.axis = object11.pos
    spring14.pos = object11.pos
    spring14.axis = object12.pos
    spring15.pos = object13.pos
    spring15.axis = object14.pos
    spring16.pos = object14.pos
    spring16.axis = object15.pos
    spring17.pos = object16.pos
    spring17.axis = object17.pos
    spring18.pos = object17.pos
    spring18.axis = object18.pos
    spring19.pos = object10.pos
    spring19.axis = object13.pos
    spring20.pos = object11.pos
    spring20.axis = object14.pos
    spring21.pos = object12.pos
    spring21.axis = object15.pos
    spring22.pos = object13.pos
    spring22.axis = object16.pos
    spring23.pos = object14.pos
    spring23.axis = object17.pos
    spring24.pos = object15.pos
    spring24.axis = object18.pos
    
    spring25.pos = object19.pos
    spring25.axis = object20.pos
    spring26.pos = object20.pos
    spring26.axis = object21.pos
    spring27.pos = object22.pos
    spring27.axis = object23.pos
    spring28.pos = object23.pos
    spring28.axis = object24.pos
    spring29.pos = object25.pos
    spring29.axis = object26.pos
    spring30.pos = object26.pos
    spring30.axis = object27.pos
    spring31.pos = object27.pos
    spring31.axis = object19.pos
    spring32.pos = object20.pos
    spring32.axis = object23.pos
    spring33.pos = object21.pos
    spring33.axis = object24.pos
    spring34.pos = object22.pos
    spring34.axis = object25.pos
    spring35.pos = object23.pos
    spring35.axis = object26.pos
    spring36.pos = object24.pos
    spring36.axis = object27.pos
