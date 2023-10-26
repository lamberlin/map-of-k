import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt  # <-- Make sure to import this

site_data = pd.read_csv(r"./segments_site_k_values.csv")
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
guatemala_map = world[world.name == 'Guatemala']

fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(10, 10))

# Use Stamen Terrain tiles
stamen_terrain = cimgt.Stamen('terrain-background')  # <-- Create an instance of Stamen with 'terrain' tile
ax.add_image(stamen_terrain, 6)  # <-- Add the StamenTerrain to the axis

# Plot sites with k values
sc = ax.scatter(site_data['X'], site_data['Y'], c=site_data['k1'], 
                s=50, edgecolor='k', cmap='RdBu', transform=ccrs.PlateCarree())

# Add colorbar
cbar = plt.colorbar(sc, ax=ax, orientation='horizontal', fraction=0.046, pad=0.1)
cbar.set_label('k Value')

plt.title('Distribution of k values in Sites across Guatemala')
plt.show()
