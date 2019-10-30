from vpython import *
L = 2
g=9.8
theta=pi/6
omega=2*pi/(3600*24)
scene = canvas(width=800,length=800,background=vec(0.5,0.5,0))
ceiling=box(color=color.blue,pos=vec(0,1,0),height = 0.01, length=0.5,width=0.5)
ball = sphere(make_trail=True,trail_radius=0.01, trail_type="points",interval=10, retain=50,radius = 0.15,pos=vec(-2*sin(theta),1-2*cos(theta),0),color=color.red,v=vec(0,0,0))
string = cylinder(pos=vec(0,1,0),axis=ball.pos-ceiling.pos,radius=0.003,k=10**5)

q=0
dt = 0.001
fivec=vec(0,0,0)
prev=vec(0,0,0)
while q<=4000:
    rate(10000)
    string.axis = ball.pos - string.pos
    coriolis = 2*omega*vec(ball.v.z*sin(radians(25))-ball.v.y*cos(radians(25)),ball.v.x*cos(radians(25)),-ball.v.x*sin(radians(25)))     #sin 25 degree
    stringForce = -string.k*(mag(string.axis)-L)*string.axis.norm()
    ball.a = vec(0,-g,0) + stringForce+coriolis
    
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    if  ball.v.y*(ball.v.y+ball.a.y*dt)<0:
        q = q+1
        fivec = ball.v
        print(q)
ang = diff_angle(fivec,vec(1,0,0))
ang = ang*180/pi
print(ang)
