#Max Low
#3-14-18
#rocket1.py -- first rocket orbital program safe altitude

from ggrocket import Rocket, Planet

earth = Planet(radius=1737400 , planetmass=73500000000000000000000 , viewscale=0.000009)
rocket = Rocket(earth, altitude=100000, velocity=1632, timezoom=3)
earth.run(rocket)
