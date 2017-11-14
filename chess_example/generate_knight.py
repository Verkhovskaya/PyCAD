import math
import sys
sys.path.append('../../')
from figure import Figure

print "import successful"

body = open("outlines/Knight.md")
params = []
for each in body:
    if each != "":
        each = map(lambda x: float(x), each.split(' '))
        params.append(each)

diameters = []
i = 0
for each in params:
    this_line = []
    ave_len = (each[0]+each[2])/2
    len1 = (ave_len+each[0])/2
    len3 = (ave_len+each[2])/2
    if i < 5:
        width1 = each[1]/1.4
        width2 = each[1]
        width3 = width1
    else:
        if i < 9:
            width1 = each[1]/2
            width2 = each[1]/1.2
            width3 = each[1]
        else:
            width1 = each[1]/1.4
            width2 = each[1]
            width3 = width1

    this_line.append((each[0], 0))
    this_line.append((each[0], 2))
    this_line.append((len1, width1))
    this_line.append((ave_len, width2))
    this_line.append((len3, width3))
    this_line.append((each[2], 2))
    if i < 10:
        this_line.append((each[2], 0))
    else:
        this_line.append((each[2], 2))
    diameters.append(this_line)
    i+=1



for each in diameters:
    print each

print "Still good"
height_step = 3
angle_step = 0.25
mirror = 8
width = 1.2

fig = Figure()

for i in range(len(diameters)-3):
    for j in range(len(diameters[0])-1):
        (x10,y10,z10) = (diameters[i][j][0],diameters[i][j][1],i*height_step-20)
        (x11,y11,z11) = (diameters[i][j+1][0],diameters[i][j+1][1],i*height_step-20)
        (x20,y20,z20) = (diameters[i+1][j+1][0],diameters[i+1][j+1][1],(i+1)*height_step-20)
        (x21,y21,z21) = (diameters[i+1][j][0],diameters[i+1][j][1],(i+1)*height_step-20)
        (x15,y15,z15) = ((max(x10,x11)+x20)/2,(max(y10,y11)+y20)/2,(max(z10,z11)+z20)/2)
        fig.line((x10, y10, z10), (x15, y15, z15), width=width)
        fig.line((x15, y15, z15), (x20, y20, z20), width=width)
        fig.line((x10, -y10, z10), (x15, -y15, z15), width=width)
        fig.line((x15, -y15, z15), (x20, -y20, z20), width=width)
        fig.line((x11, y11, z11), (x15, y15, z15), width=width)
        fig.line((x15, y15, z15), (x21, y21, z21), width=width)
        fig.line((x11, -y11, z11), (x15, -y15, z15), width=width)
        fig.line((x15, -y15, z15), (x21, -y21, z21), width=width)
i = len(diameters)-3
heights = [0,.1,.2,.3,.8]
for j in range(1,len(diameters[0])-3):
    (x1,y1,z1) = (diameters[i][j][0],diameters[i][j][1],i*height_step-20)
    (x2,y2,z2) = (diameters[i][j+1][0],diameters[i][j+1][1],i*height_step-20)
    (x3,y3,z3) = ((x1+x2)/2, 0, z1+height_step*height_step*heights[j])
    fig.line((x1,y1,z1),(x3,y3,z3), width=width)
    fig.line((x2,y2,z2),(x3,y3,z3), width=width)
    fig.line((x1,-y1,z1),(x3,-y3,z3), width=width)
    fig.line((x2,-y2,z2),(x3,-y3,z3), width=width)

print
bottom = []
for i in diameters[0]:
    bottom.append(i)
for i in range(1,len(bottom)-1):
    a = bottom[i]
    b = bottom[i+1]
    fig.line((a[0],a[1],-20),(b[0],b[1],-20), width=width)
    fig.line((a[0],-a[1],-20),(b[0],-b[1],-20), width=width)
    b = bottom[len(bottom)-1-i]
    fig.line((a[0],-a[1],-20),(b[0],b[1],-20), width=width)

eartip1 = (1,-3,8)
fig.line((-1.0, -2, 4),eartip1,width=width)
fig.line((3, -4, 4),eartip1,width=width)

eartip2 = (1,3,8)
fig.line((-1.0, 2, 4),eartip2,width=width)
fig.line((3, 4, 4),eartip2,width=width)

fig.generate_stl()
