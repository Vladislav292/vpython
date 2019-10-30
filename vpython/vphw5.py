from vpython import*
G = 6.673E-11
mass= {'earth':5.97E24,'moon':7.36E22,'sun':1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun':6.95E8*10}
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.84E8, 'v': 1.022E3}
theta = 5.145*pi/180.0

scene=canvas(width=800,height=800,background=vec(0.5,0.5,0),center=vec(earth_orbit['r'],0,0))
def G_force(m1,pos1,m2,pos2): 
    return -G * m1*m2 / mag2(pos1-pos2) * norm(pos1-pos2) 
class as_obj(sphere): 
    def kinetic_energy(self): 
        return 0.5 * self.m * mag2(self.v)
earth = as_obj(color=color.blue,radius=radius['earth'],pos=vec(earth_orbit['r'],0,0),v=-1*mass['moon']*vec(0,0,-moon_orbit['v'])/mass['earth'],m=mass['earth'])
moon = as_obj(color=color.black,pos=vec(earth_orbit['r']+moon_orbit['r']*cos(theta),-moon_orbit['r']*sin(theta),0),v=vec(0,0,-moon_orbit['v']),radius=radius['moon'],m=mass['moon'])
am = arrow(pos=earth.pos)

dt = 60*30
while True:
    rate(10000)
    moon.v+= G_force(moon.m,moon.pos,earth.m,earth.pos)*dt/moon.m
    moon.pos += moon.v*dt
    earth.v+= G_force(earth.m,earth.pos,moon.m,moon.pos)*dt/earth.m 
    earth.pos += earth.v*dt
    am.pos=earth.pos
    am.axis = 1E-3*(moon.pos-earth.pos).cross(moon.v)
