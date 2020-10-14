# %%
import geemap

# Initialize and display map
Map = geemap.Map()
Map.split_map()
Map


# %%
# Initialize and display map
Map = geemap.Map()
Map.split_map(left_layer='HYBRID', right_layer='ROADMAP')
Map

# %%

#  Retrieve available base maps
basemaps = geemap.ee_basemaps.keys()
print(basemaps)

# %%
for basemap in basemaps:
    print(basemap)

# %%
# Split map between NLCD 2016 (right) and 2001 (left)
Map = geemap.Map()
Map.split_map(left_layer='NLCD 2016 CONUS Land Cover', right_layer='NLCD 2001 CONUS Land Cover')
Map

# %%
import ee

# https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD
collection = ee.ImageCollection("USGS/NLCD")
print(collection.aggregate_array('system:id').getInfo())

nlcd_2001 = ee.Image('USGS/NLCD/NLCD2001').select('landcover')
nlcd_2016 = ee.Image('USGS/NLCD/NLCD2016').select('landcover')

left_layer = geemap.ee_tile_layer(nlcd_2001, {}, 'NLCD 2001')
right_layer = geemap.ee_tile_layer(nlcd_2016, {}, 'NLCD 2016')

Map = geemap.Map()
Map.split_map(left_layer, right_layer)
Map

# %%
