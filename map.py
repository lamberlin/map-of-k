import folium
import pandas as pd
import branca
from folium import IFrame

# Load your data
site_data = pd.read_csv(r"./segments_site_k_values.csv")

# Create a colormap for the k values
min_k = site_data['k1'].min()
max_k = site_data['k1'].max()
colormap = branca.colormap.linear.RdBu_11.scale(min_k, max_k)

# Create a base map centered around Guatemala
m = folium.Map(location=[15.7835, -90.2308], zoom_start=6, tiles='Stamen Terrain', min_zoom=2, max_zoom=16)

# Directory containing the plots
plot_dir = "./segments_site_plots/"

# Add your sites to the map
for _, row in site_data.iterrows():
    color = colormap(row['k1'])
    
    # Construct the path to the plot image for the site
    plot_path = plot_dir + f"growth_curve_{row['codigoparc']}.png"
    
    # Create a string combining the popup content and the image
    popup_content = f"""
    Site: {row['codigoparc']}<br>
    Species: {row['Especie']}<br>
    k: {row['k1']}<br>
    <img src="{plot_path}" alt="site_plot" width="300">
    """
    
    folium.CircleMarker(
        location=[row['Y'], row['X']],
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=folium.Popup(popup_content, max_width=310) # you can adjust the max_width if needed
    ).add_to(m)

# Add the color map legend to the map
colormap.caption = "k Value"
colormap.add_to(m)

# Display the map
m
