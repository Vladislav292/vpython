from vpython import *
size,m=0.05,0.2
L,k = 0.5,[15,12,17]
v = [1,2,2.2]
d=[-0.06,0,-0.1]
scene = canvas(width=400,height=400,center=vec(0.4,0.2,0),align='left',background=vec(0.5,0.5,0))
coordinate = graph(width=500,align='left')
coordinate2 = graph(width=500,align='left')
floor = box(pos = vec(0.4,0,0),length=0.8,height=0.005,width=0.8,color=color.blue)
wall = box(pos = vec(0,0.05,0),length= 0.01,height=0.1,width = 0.8)
dt = 0.001
time = 0
ske=0
sU=0
funct1 = gcurve(graph=coordinate,color=color.red,width=3)
funct2 = gcurve(graph=coordinate,color=color.blue,width=3)
functa = gcurve(graph=coordinate2,color=color.red,width=3)
functb = gcurve(graph=coordinate2,color=color.blue,width=3)

balls =[]
for i in range(3):
    ball = sphere(pos=vec(L+d[i],size,(i-1)*3*size),radius=size,color=color.red)
    ball.v = vec(v[i],0,0)
    balls.append(ball)
springs = []
for i in range(3):
    spring = helix(pos = vec(0,size,(i-1)*3*size),radius= 0.02,thickness =0.01)
    spring.axis = balls[i].pos-spring.pos
    spring.k=k[i]
    springs.append(spring)
while True:
    rate(1000)
    for i in range(3):
        balls[i].v += (dt*springs[i].k*(L-mag(springs[i].axis))*vec(1,0,0))/m
        balls[i].pos += balls[i].v*dt
        springs[i].axis=balls[i].pos-springs[i].pos
    time=time+dt
    ke = 0.5*m*(mag(balls[1].v)**2+mag(balls[2].v)**2+mag(balls[0].v)**2)
    U = 0.5*(springs[0].k*(L-mag(springs[0].axis))**2+springs[1].k*(L-mag(springs[1].axis))**2+springs[2].k*(L-mag(springs[2].axis))**2)
    ske = ske+ke
    sU = sU+U
    mke= ske/time
    mU=sU/time
    funct1.plot(pos=(time,ke))
    funct2.plot(pos=(time,U))
    functa.plot(pos=(time,mke))
    functb.plot(pos=(time,mU))
    
