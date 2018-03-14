#Max Low
#3-14-18
#rocket1.py -- first rocket orbital program safe altitude

from ggrocket import Rocket, Planet
from ggame import *

data = {}
data['thrust'] =0

def thrust():
    return data['thrust']

earth = Planet(radius=1737400 , planetmass=73500000000000000000000 , viewscale=0.000009, color=0x00FFFF)

rocket = Rocket(earth, altitude=100000, velocity=1632, timezoom=3, thrust = thrust())



def upThrust(event):
    data['thrust']  += 1
    
def downThrust(event):
    data['thrust']  -= 1

App.listenKeyEvent('keydown','t', upThrust)
App.listenKeyEvent('keydown','g', downThrust)
earth.run(rocket)
