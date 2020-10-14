# %%
import ee
import geemap

# %%
geemap.show_youtube('PDab8mkAFL0')

# %%


# %%
Map = geemap.Map()
Map

# %%
landsat7 = ee.Image('LE7_TOA_5YEAR/1999_2003') \
    .select([0, 1, 2, 3, 4, 6])
landsat_vis = {
    'bands': ['B4', 'B3', 'B2'], 
    'gamma': 1.4
}
Map.addLayer(landsat7, landsat_vis, "LE7_TOA_5YEAR/1999_2003")

hyperion = ee.ImageCollection('EO1/HYPERION') \
    .filter(ee.Filter.date('2016-01-01', '2017-03-01'));
hyperion_vis = {
  'min': 1000.0,
  'max': 14000.0,
  'gamma': 2.5,
}
Map.addLayer(hyperion, hyperion_vis, 'EO1/HYPERION');

# %%
Map.set_plot_options(plot_type='bar', add_marker_cluster=True)

# %%
m = geemap.Map()
m

# %%
m.plot_demo()