# %%
import geemap
import json
import os
import requests

from geemap import geojson_to_ee, ee_to_geojson
from ipyleaflet import GeoJSON, Marker, MarkerCluster

Map = geemap.Map()
Map

# %%
file_path = os.path.abspath('../../data/us-cities.json')

if not os.path.exists(file_path):
    url = 'https://github.com/giswqs/geemap/raw/master/examples/data/us-cities.json'
    r = requests.get(url)
    with open(file_path, 'w') as f:
        f.write(r.content.decode("utf-8"))        

with open(file_path) as f:
    json_data = json.load(f)

# %%
maker_cluster = MarkerCluster(
    markers=[Marker(location=feature['geometry']['coordinates'][::-1]) for feature in json_data['features']],
    name='Markers')

# %%
Map.add_layer(maker_cluster)

# %%
ee_fc = geojson_to_ee(json_data)
Map.addLayer(ee_fc, {}, "US Cities EE")
