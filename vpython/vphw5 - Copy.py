from vpython import*
G = 6.673E-11
mass= {'earth':5.97E24,'moon':7.36E22,'sun':1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun':6.95E8*10}
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.84E8, 'v': 1.022E3}
theta = 5.145*pi/180.0

scene=canvas(width=800,height=800,
             background=vec(0.5,0.5,0),center=vec(earth_orbit['r'],0,0))
def G_force(m1,pos1,m2,pos2): 
    return -G * m1*m2 / mag2(pos1-pos2) * norm(pos1-pos2) 
earth = sphere(color=color.blue,radius=radius['earth'],
               pos=vec(earth_orbit['r']-cos(theta)*mass['moon']*moon_orbit['r']/(mass['earth']+mass['moon']),moon_orbit['r']*sin(theta)*mass['moon']/(mass['moon']+mass['earth']),0),
               v=-1*mass['moon']*vec(0,0,-moon_orbit['v'])/mass['earth']+vec(0,0,-earth_orbit['v']),
               m=mass['earth'])
moon = sphere(color=color.black,
              pos=vec(earth_orbit['r']+moon_orbit['r']*cos(theta)*mass['earth']/(mass['earth']+mass['moon']),-moon_orbit['r']*sin(theta)*mass['earth']/(mass['moon']+mass['earth']),0),
              v=vec(0,0,-moon_orbit['v']-earth_orbit['v']),
              radius=radius['moon'],m=mass['moon'])
sun = sphere(color=color.yellow,pos=vec(0,0,0)
             ,v=vec(0,0,0),radius=radius['sun'],
             m=mass['sun'])
am = arrow(pos=earth.pos)
iniaxis= 1E-3*(moon.pos-earth.pos).cross(moon.v-earth.v)
time=0
dt = 60*50
while True:
    rate(1000)
    time=time+dt
    moon.v+= G_force(moon.m,moon.pos,earth.m,earth.pos)*dt/moon.m +G_force(moon.m,moon.pos,sun.m,sun.pos)*dt/moon.m 
    moon.pos += moon.v*dt
    earth.v+= G_force(earth.m,earth.pos,moon.m,moon.pos)*dt/earth.m +G_force(earth.m,earth.pos,sun.m,sun.pos)*dt/earth.m
    earth.pos += earth.v*dt
    sun.v += G_force(sun.m,sun.pos,moon.m,moon.pos)*dt/sun.m +G_force(sun.m,sun.pos,earth.m,earth.pos)*dt/sun.m
    sun.pos += sun.v*dt
    am.pos=earth.pos
    am.axis = 1E-3*(moon.pos-earth.pos).cross(moon.v-earth.v)
    if mag(iniaxis-am.axis)< 1:
        print (time/60*60*24*365)
    scene.center=earth.pos
