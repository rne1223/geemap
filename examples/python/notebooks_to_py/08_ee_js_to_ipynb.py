# %%
"""
<table class="ee-notebook-buttons" align="left">
    <td><a target="_blank"  href="https://github.com/giswqs/geemap/tree/master/examples/notebooks/earthengine_js_to_ipynb.ipynb">
        <img width=32px src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" /> View source on GitHub
        </a>
    </td>
    <td><a target="_blank"  href="https://nbviewer.jupyter.org/github/giswqs/geemap/blob/master/examples/notebooks/earthengine_js_to_ipynb.ipynb"><img width=26px src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" />Notebook Viewer</a></td>
    <td><a target="_blank"  href="https://colab.research.google.com/github/giswqs/geemap/blob/master/examples/notebooks/earthengine_js_to_ipynb.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run in Google Colab</a></td>
</table>
"""

# %%
"""
## Automatic conversion from Earth Engine JavaScripts to Python scripts

### Install Earth Engine API and geemap
Install the [Earth Engine Python API](https://developers.google.com/earth-engine/python_install) and [geemap](https://github.com/giswqs/geemap). The **geemap** Python package is built upon the [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet) and [folium](https://github.com/python-visualization/folium) packages and implements several methods for interacting with Earth Engine data layers, such as `Map.addLayer()`, `Map.setCenter()`, and `Map.centerObject()`.
The following script checks if the geemap package has been installed. If not, it will install geemap, which automatically installs its [dependencies](https://github.com/giswqs/geemap#dependencies), including earthengine-api, folium, and ipyleaflet.

**Important note**: A key difference between folium and ipyleaflet is that ipyleaflet is built upon ipywidgets and allows bidirectional communication between the front-end and the backend enabling the use of the map to capture user input, while folium is meant for displaying static data only ([source](https://blog.jupyter.org/interactive-gis-in-jupyter-with-ipyleaflet-52f9657fa7a)). Note that [Google Colab](https://colab.research.google.com/) currently does not support ipyleaflet ([source](https://github.com/googlecolab/colabtools/issues/60#issuecomment-596225619)). Therefore, if you are using geemap with Google Colab, you should use [`import geemap.eefolium`](https://github.com/giswqs/geemap/blob/master/geemap/eefolium.py). If you are using geemap with [binder](https://mybinder.org/) or a local Jupyter notebook server, you can use [`import geemap`](https://github.com/giswqs/geemap/blob/master/geemap/geemap.py), which provides more functionalities for capturing user input (e.g., mouse-clicking and moving).
"""

# %%
import subprocess

try:
    import geemap
except ImportError:
    print('geemap package not installed. Installing ...')
    subprocess.check_call(["python", '-m', 'pip', 'install', 'geemap'])
"""
### Convert Earth Engine JavaScripts to Python scripts
"""

import os
from geemap.conversion import *

# Create a temporary working directory
work_dir = os.path.join(os.path.expanduser('~'), 'geemap')
# Get Earth Engine JavaScript examples. There are five examples in the geemap package folder. 
# Change js_dir to your own folder containing your Earth Engine JavaScripts, 
# such as js_dir = '/path/to/your/js/folder'
js_dir = get_js_examples(out_dir=work_dir) 

# Convert all Earth Engine JavaScripts in a folder recursively to Python scripts.
js_to_python_dir(in_dir=js_dir, out_dir=js_dir, use_qgis=True)
print("Python scripts saved at: {}".format(js_dir))

# %%
"""
### Convert Earth Engine Python scripts to Jupyter Notebooks
"""

# %%
# Convert all Earth Engine Python scripts in a folder recursively to Jupyter notebooks.
nb_template = get_nb_template()  # Get the notebook template from the package folder.
py_to_ipynb_dir(js_dir, nb_template)

# Execute all Jupyter notebooks in a folder recursively and save the output cells.
execute_notebook_dir(in_dir=js_dir)