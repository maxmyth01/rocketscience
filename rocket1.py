#Max Low
#3-14-18
#rocket1.py -- first rocket orbital program safe altitude

from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.000009)
rocket = Rocket(earth, altitude=400000, velocity=1000)
earth.run(rocket)
