# %%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx


# %%
#  Gauges II USGS stream gauge dataset:
# Download here:
# https://water.usgs.gov/GIS/metadata/usgswrd/XML
# /gagesII_Sept2011.xml#stdorder

# Reading it using geopandas
file = os.path.join('../../data', 'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)

# Zoom  in and just look at AZ
gages.columns
gages.STATE.unique()
gages_AZ = gages[gages['STATE'] == 'AZ']

# %%
# adding HUC boundaries
# https://www.usgs.gov/core-science-systems/ngp
# /national-hydrography/access-national-hydrography-products
# https://viewer.nationalmap.gov/basic/?basemap=b1&
# category=nhd&title=NHD%20View

# Example reading in a geodataframe
# Watershed boundaries for the lower colorado
file = os.path.join('../../data', 'WBD_15_HU2_GDB.gdb')
fiona.listlayers(file)
HUC6 = gpd.read_file(file, layer="WBDHU6")

# %%
# importing boundary of states close to arizona
# https://catalog.data.gov/dataset/usgs-national-boundary-dataset-nbd
# -for-arizona-20171220-state-or-territory-filegdb-10-14ecfe
file = os.path.join('../../data', 'GOVTUNIT_Arizona_State_GDB.gdb')
fiona.listlayers(file)
statebound = gpd.read_file(file, layer="GU_StateOrTerritory")

# plotting boundary
fig, ax = plt.subplots(figsize=(5, 5))
# statebound.plot(ax=ax)
# ax.set_title("statebound")
statebound.boundary.plot(ax=ax, color=None,
                         edgecolor='black', linewidth=1.5)
plt.show()


# %%
# Add some point
# STream gauge:  34.44833333, -111.7891667
point_list = np.array([[-111.7891667, 34.44833333]])

# make these into spatial features
point_geom = [Point(xy) for xy in point_list]
point_geom

# mape a dataframe of the site
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC6.crs)

# %%
# reprojecting to basemap standard
points_project = point_df.to_crs(epsg=3857)
gages_AZ = gages_AZ.to_crs(epsg=3857)
HUC6_project = HUC6.to_crs(epsg=3857)
statebounds = statebound.to_crs(epsg=3857)

# %%
# combination map of all 5 layers
fig, ax = plt.subplots(figsize=(8, 8))
HUC6_project.boundary.plot(ax=ax, color=None, label='HUC boundaries',
                           edgecolor='grey', linewidth=1.1)
gages_AZ.plot(column='DRAIN_SQKM', categorical=False, label='gages',
              legend=True, markersize=25, cmap='brg',
              ax=ax)
points_project.plot(ax=ax, color='c', marker='*', label='site-gage',
                    markersize=345)
statebounds.boundary.plot(ax=ax, color=None, label='stateline',
                          edgecolor='black', linewidth=1.5)
ctx.add_basemap(ax, source=ctx.providers.Stamen.TonerLite)
plt.ylim(3.65*(10**6), 4.5*(10**6))
plt.xlim(-1.28*(10**7), -1.21*(10**7))
ax.legend()

# %%
