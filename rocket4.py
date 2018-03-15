#Max Low
#3-15-18
#rocket4.py -- 2 stage rocket simulation

from ggrocket import Rocket, Planet
from math import radans, sqrt, log
from gggmath import InputButton, Timer, Labol, Slider

earth = Planet(planetmass=0)

Stage1Started = False
Stage2Started = False
PayloadLaunched = False
StartTime = None
BurnTime = 0

me1 = 25600
mp1 = 395700
Ftotal1 = 6.444E6
tburn = 180

me2 = 3900
mp2 = 92670
Ftotal2 = 8.01E5
tburn2 = 372

mep = 13150

vmax1 = Ftotal1*tburn/mp1*log((me1+mp1+me2+mp2+mep)/(me1+me2+mp2+mep))
vmax2 = Ftotal2*tburn/mp2*log((me2+mp2+mep)/(me2+mep))

print("predicted final staged rocket velocity (Rocket Equation), vmax:", vmax1+vmax2, "m/s")

def GetThrust():
    global StartTime
    global BurnTime
    global Stage1Started
    global Stage2Started
    global PayloadLaunched
    if Stage1Started:
        tburn = tburn1
        Ftotal = Ftotal1
    elif Stage2Started:
        tburn = tburn2
        Ftotal = Ftotal2
    if Stage1Started or Stage2Started:
        BurnTime = rocket.shiptime - StartTime
        if BurnTime >= tburn:
            if Stage1Started:
                Stage1Started = False
                Stage2Started = True
                StartTime = rocket.shiptime
        