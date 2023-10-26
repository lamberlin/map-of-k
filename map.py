import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import branca

site_data = pd.read_csv(r"./segments_site_k_values.csv")

min_k = site_data['k1'].min()
max_k = site_data['k1'].max()
colormap = branca.colormap.linear.RdBu_11.scale(min_k, max_k)

topo_tile_url = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}"
m = folium.Map(location=[15.7835, -90.2308], zoom_start=6, tiles=topo_tile_url, attr='Esri')

plot_dir = "./segments_site_plots/"

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
        popup=folium.Popup(popup_content, max_width=310) 
    ).add_to(m)

colormap.caption = "k Value"
colormap.add_to(m)

folium_static(m)

st.title("Growth Curve Map of Plantation Across Guatemala")
st.subheader("Created by Lambert Lin, Ja Yoon Kim")

