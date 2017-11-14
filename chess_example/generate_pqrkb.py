import math
import sys
sys.path.append('../../')
from figure import Figure

print "import successful"

body = open("outlines/Queen.md")
diameters = []
for each in body:
    if each != "":
        diameters.append(float(each))
print diameters

print "Still good"
height_step = 1
angle_step = 0.25
mirror = 8
width = 1.2

fig = Figure()

for an in range(mirror/2):
    base = diameters[0]
    p1=(base*math.cos(6.3/mirror*an),base*math.sin(6.3/mirror*an),0)
    p2=(-base*math.cos(6.3/mirror*an),-base*math.sin(6.3/mirror*an),0)
    fig.line(p1, p2, width=width)

for i in range(len(diameters)-1):
    for an in range(mirror):
        h1 = diameters[i]
        h2 = diameters[i+1]
        p1=(h1*math.cos(angle_step*i+6.3/mirror*an),
            h1*math.sin(angle_step*i+6.3/mirror*an),
            height_step*i)
        p2=(h2*math.cos(angle_step*(i+1)+6.3/mirror*an),
            h2*math.sin(angle_step*(i+1)+6.3/mirror*an),
            height_step*(i+1))
        fig.line(p1,p2, width=width)
        p1 = (-p1[0], p1[1], p1[2])
        p2 = (-p2[0], p2[1], p2[2])
        fig.line(p1, p2, width=width)

fig.generate_stl()
