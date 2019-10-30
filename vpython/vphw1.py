from vpython import *
g=vec(0,-9.8,0)              
size = 0.25         
height = 5.0       

scene = canvas(width=800, height=800, center = vec(0,height/2,0), background=vec(0.5,0.5,0)) #設定畫面
floor = box(length=30, height=0.01, width=10, color=color.blue)                         #畫地板
ball = sphere(radius = size, color=color.red,make_trail=True,trail_radius=0.05)                                           #畫球

ball.pos = vec(-15, height, 0)        
ball.v = vec(6, 8 , 0)               

a1=arrow(color=color.green,shaftwidth=0.05)
i=0
path=0
dt = 0.001                              
while ball.pos.y > size:               
    rate(1000)                      

    ball.v +=  g*dt
    ball.pos += ball.v*dt
    a1.pos=ball.pos
    a1.axis=ball.v*0.25
    i = i+1
    vmode= (ball.v.x**2+ball.v.y**2+ball.v.z**2)**0.5
    path = path + dt*vmode
time = i/1000
print (time)
print (path)
paths=text(text="length:"+str(path)+"  time:" +str(time),pos=vec(0,5,0))
paths.visible=True

