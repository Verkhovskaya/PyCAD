# Setup Instructions
1. Install OpenSCAD (http://www.openscad.org/index.html)
2. Download this repository and change the openscad.txt file to point at your openscad installation. This is typically /Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD
 for macs. Just "openscad" might work for Linux or Windows machines, but I've never tried it. 
3. Start a new Python file and import the library by adding

import sys

sys.path.append('../../')

from figure import Figure

fig = figure()

\# a bunch of 
fig.line((x1, y1, z1), (x2, y2, z2))

fig.generate_stl()

4. fig.generate_stl() will generate a .scad file in generated_openccad then launch the OpenSCAD GUI. To generate a 3d printable file, run build then export > STL. 
