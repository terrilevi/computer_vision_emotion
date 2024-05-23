import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Haz un dibujito")

# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
#bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")

realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    #background_color=bg_color,
    update_streamlit=realtime_update,
    height=150,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)

# Add a Predict button
if st.button("Predict"):
    if canvas_result.image_data is not None:
        st.write("Imagen procesada")
        st.image(canvas_result.image_data)
        #aqui irá el modelo 
    else:
        st.write("No hay imagen")


