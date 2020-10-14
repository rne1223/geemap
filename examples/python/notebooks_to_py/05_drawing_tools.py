# %%
import ee
import geemap


# %%
Map = geemap.Map()
Map

# %%
# Add Earth Engine dataset
image = ee.Image('USGS/SRTMGL1_003')

# Set visualization parameters.
vis_params = {
  'min': 0,
  'max': 4000,
  'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}

# Add Earth Engine DEM to map
Map.addLayer(image, vis_params, 'SRTM DEM')

# %%
# Add the "US States" as a vector layer
states = ee.FeatureCollection("TIGER/2018/States")
Map.addLayer(states, {}, 'US States')

# %%
# Displays all vector layers drawn by hand
Map.draw_features

# %%
# Displays the last vector layers were hand drawn
Map.draw_last_feature

# %%
# Create a collection from the drawn shapes
roi = ee.FeatureCollection(Map.draw_features)
# Filter and create a new vector layer that intersects the drawn shapes
selected_states = states.filterBounds(roi)
# Add a new layer with the of the intersecting shapes
Map.addLayer(selected_states, {}, "Selected states")

# %%
clipped_image = image.clip(selected_states)
Map.addLayer(clipped_image, vis_params, 'Clipped image')