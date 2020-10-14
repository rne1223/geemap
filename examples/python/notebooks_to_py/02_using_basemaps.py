# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
# geemap.show_youtube('6J5ZCIUPXfI')
import geemap


# %%
Map = geemap.Map(center=[40, -100], zoom=4)

## Add a base map
# Map.add_basemap()

## Add a 'Hybrid' base map
# Map.add_basemap('HYBRID')

## To find all the basemaps available
Map.basemap_demo()
Map

# %%
naip_url = 'https://services.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer?'
Map.add_wms_layer(url=naip_url, layers='0', name='NAIP Imagery', format='image/png', shown=True)


# %%
url = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}'
Map.add_tile_layer(url, name='Google Map', attribution='Google')


# %%
m = geemap.Map()
m.basemap_demo()
m


