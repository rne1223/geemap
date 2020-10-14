# %%
import ee
import geemap
"""
## Create an interactive map
"""
Map = geemap.Map(center=(40, -100), zoom=4)
Map.add_basemap('HYBRID')
Map

# %%
"""
## Add Earth Engine Python script
"""
# Add Earth Engine datasets
dem = ee.Image('USGS/SRTMGL1_003')
landcover = ee.Image("ESA/GLOBCOVER_L4_200901_200912_V2_3").select('landcover')
landsat7 = ee.Image('LE7_TOA_5YEAR/1999_2003')
states = ee.FeatureCollection("TIGER/2018/States")

# Set visualization parameters.
vis_dem_params = {
  'min': 0,
  'max': 4000,
  'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}

vis_lansat7_params = {
   'bands': ['B4', 'B3', 'B2'], 
   'min': 20, 
   'max': 200 
   }

# Add Earth Engine layers to Map
Map.addLayer(landcover, {}, 'Land cover')
Map.addLayer(landsat7, vis_lansat7_params, 'Landsat 7')
Map.addLayer(dem, vis_dem_params, 'STRM DEM', True, 0.5)
Map.addLayer(states, {}, "US States")