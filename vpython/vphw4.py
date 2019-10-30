from vpython import *
g= vec(0, -9.8, 0)
NN=10
N= 6
size= 0.2
dt = 0.0005

scene= canvas(center=vec(0.8, -1, 0),background=vec(0.4, 0.6, 0.7))
balls=[]
strings=[]
suspenders=[]

for i in range(NN):
    balls.append(sphere(pos=vec(2*(size+0.001)*i,-2+0.1*g.y/1500,0),radius= size, v=vec(0,0,0),m=0.1))
    suspenders.append(sphere(radius=size/3,pos=vec(2*(size+0.001)*i,0,0)))
    strings.append(cylinder(radius=size/4,pos=suspenders[i].pos,axis= balls[i].pos-suspenders[i].pos,k=1500))
def collide(m1, m2, v1, v2, x1, x2):
     v1_prime = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
     v2_prime = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
     return (v1_prime, v2_prime)

for i in range(N):
    balls[i].pos =vec(2*(size+0.001)*i+(-2+0.1*g.y/1500)*sin(pi/6),(-2+0.1*g.y/1500)*cos(pi/6),0)
    strings[i].axis=balls[i].pos-suspenders[i].pos

while True:
    rate(2000)
    for i in range(NN):
        strings[i].axis = balls[i].pos - strings[i].pos
        stringForce = -strings[i].k*(mag(strings[i].axis)-2)*strings[i].axis.norm()
        balls[i].a = g + stringForce/balls[i].m

        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt
    for i in range(NN-1):
        if (mag(balls[i].pos - balls[i+1].pos)<= 2*size and dot(balls[i].pos - balls[i+1].pos,balls[i].v - balls[i+1].v)<=0 ):
            (balls[i].v,balls[i+1].v)=collide (balls[i].m,balls[i+1].m,balls[i].v,balls[i+1].v,balls[i].pos,balls[i+1].pos)
