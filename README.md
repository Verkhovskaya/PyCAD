# Setup Instructions
1. Install OpenSCAD (http://www.openscad.org/index.html)
2. Download this repository and change the openscad.txt file to point at your openscad installation. This is typically /Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD
 for macs. Alternatively, add the installation to your PATH then write "openscad" to openscad.txt. 
3. Start a new Python file and import the library by adding

```python
import sys
sys.path.append(PATH_TO_FIGURE.PY)
from figure import Figure
fig = figure()
# a bunch of
# fig.line((x1, y1, z1), (x2, y2, z2))
fig.generate_stl()
```

4. This will generate a new file in /generated_openscad and launch the OpenSCAD GUI. To generate a 3D printable file, build the figure then run export > STL. 
