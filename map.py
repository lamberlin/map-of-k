import folium
import pandas as pd
import branca

# Load your data
site_data = pd.read_csv(r"./segments_site_k_values.csv")

# Create a colormap for the k values
min_k = site_data['k1'].min()
max_k = site_data['k1'].max()
colormap = branca.colormap.linear.RdBu_11.scale(min_k, max_k)

# Create a base map centered around Guatemala
m = folium.Map(location=[15.7835, -90.2308], zoom_start=6, tiles='Stamen Terrain', min_zoom=2, max_zoom=16)

# Add your sites to the map
for _, row in site_data.iterrows():
    color = colormap(row['k1'])
    folium.CircleMarker(
        location=[row['Y'], row['X']],
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=f"Site: {row['codigoparc']}<br>Species: {row['Especie']}<br>k: {row['k1']}",
    ).add_to(m)

# Add the color map legend to the map
colormap.caption = "k Value"
colormap.add_to(m)

# Display the map
m
