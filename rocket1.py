#Max Low
#3-14-18
#rocket1.py -- first rocket orbital program safe altitude

from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.000009)
rocket = Rocket(earth, altitude=50)
earth.run(rocket)
