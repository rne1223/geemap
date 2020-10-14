# %%
import geemap
import json
import os
import requests
from geemap import geojson_to_ee, ee_to_geojson
from ipyleaflet import GeoJSON

Map = geemap.Map()
Map

# %%
file_path = os.path.abspath('../../data/us-states.json')

if not os.path.exists(file_path):
    url = 'https://github.com/giswqs/geemap/raw/master/examples/data/us-states.json'
    r = requests.get(url)
    with open(file_path, 'w') as f:
        f.write(r.content.decode("utf-8"))        

with open(file_path) as f:
    json_data = json.load(f)

# %%
json_layer = GeoJSON(data=json_data, name='US States JSON', hover_style={'fillColor': 'red', 'fillOpacity': 0.5})
Map.add_layer(json_layer)

# %%
ee_data = geojson_to_ee(json_data)
Map.addLayer(ee_data, {}, "US States EE")

# %%
json_data_2 = ee_to_geojson(ee_data)
json_layer_2 = GeoJSON(data=json_data_2, name='US States EE JSON', hover_style={'fillColor': 'red' , 'fillOpacity': 0.5})
Map.add_layer(json_layer_2)

# %%
# Read data from json file 
file_path = os.path.abspath('../../data/countries.json')

# try to download it from the web
if not os.path.exists(file_path):
    url = 'https://github.com/giswqs/geemap/raw/master/examples/data/countries.json'
    r = requests.get(url)
    with open(file_path, 'w') as f:
        f.write(r.content.decode("utf-8"))        

# Load Countries geojson data
with open(file_path) as f:
    json_data = json.load(f)

# %%
# Add a gejson layer to the map
json_layer = GeoJSON(data=json_data, 
                    name='Countries', 
                    hover_style={'fillColor': 'red' , 'fillOpacity': 0.5})

Map.add_layer(json_layer)

# %%
from ipywidgets import Text, HTML
from ipyleaflet import WidgetControl, GeoJSON 

# Cool way to modify the hover behaviour
html1 = HTML('''
    <h4>Country</h4>
    Hover over a country
''')
html1.layout.margin = '0px 20px 20px 20px'
control1 = WidgetControl(widget=html1, position='bottomright')
Map.add_control(control1)


def update_html(feature, **kwargs):
    html1.value = '''
        <h4>Country code: <b>{}</b></h4>
        Country name: {}
    '''.format(feature['id'], feature['properties']['name'])

json_layer.on_hover(update_html)