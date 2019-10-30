from vpython import *
sizes=[0.06,0.04]
ms = [0.2,0.12]
L,k=0.5,15
scene = canvas(width=400,height=400,center=vec(0.275,0,0),align='left',background=vec(0.5,0.5,0))
dt = 0.001
time = 0

balls =[]
for i in range(2):
    ball = sphere(pos=vec(0.55*i,0,0),radius=sizes[i],color=color.red)
    ball.v = vec(0,0,0)
    balls.append(ball)
    

spring = helix(pos = balls[0].pos,radius= 0.02,thickness =0.01)
spring.axis = balls[1].pos-spring.pos
spring.k=k
while True:
    rate(1000)
    balls[0].v += (dt*spring.k*(mag(spring.axis)-L)*vec(1,0,0))/ms[0]
    balls[0].pos += balls[0].v*dt
    balls[1].v += (dt*spring.k*(L-mag(spring.axis))*vec(1,0,0))/ms[1]
    balls[1].pos += balls[1].v*dt
    spring.pos = balls[0].pos
    spring.axis=balls[1].pos-spring.pos
    time = time+dt
    if balls[0].pos.x <0.00000000000000000000000000001 :
        print(time)
        time = 0
