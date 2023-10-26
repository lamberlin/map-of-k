#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# streamlit_app.py

import streamlit as st
import pandas as pd
import pydeck as pdk

# Load data
site_data = pd.read_csv("./segments_site_k_values.csv")

# Create map with pydeck
view_state = pdk.ViewState(latitude=15.7835, longitude=-90.2308, zoom=5)
layer = pdk.Layer(
    "ScatterplotLayer",
    data=site_data,
    get_position=["X", "Y"],
    get_color="k1 * 255",
    get_radius=50000,
    pickable=True,
    radius_min_pixels=10,
    radius_max_pixels=50
)

tooltip = {
    "html": "<b>Site:</b> {codigoparc}<br><b>Species:</b> {Especie}<br><b>k:</b> {k1}",
    "style": {"backgroundColor": "steelblue", "color": "white"}
}

r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip)

# Streamlit app
st.title('Distribution of k values in Sites across Guatemala')
st.pydeck_chart(r)

