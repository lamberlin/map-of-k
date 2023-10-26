import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

site_data = pd.read_csv(r"./segments_site_k_values.csv")

fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(10, 10))

# Add Stamen terrain background
ax.add_image(cfeature.STAMEN_TERRAIN, 6)  # '6' is the zoom level; you can adjust it as needed

# Plot sites with k values
sc = ax.scatter(site_data['X'], site_data['Y'], c=site_data['k1'], 
                s=50, edgecolor='k', cmap='RdBu', transform=ccrs.PlateCarree())

# Add colorbar
cbar = plt.colorbar(sc, ax=ax, orientation='horizontal', fraction=0.046, pad=0.1)
cbar.set_label('k Value')

plt.title('Distribution of k values in Sites across Guatemala')
plt.show()
