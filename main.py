import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
tab1, tab2 = st.tabs(["Haz un  dibujito", "Sube una imágen"])

with tab1:
    import streamlit as st
    st.header("Haz un dibujito")

    # Specify canvas parameters in application
    drawing_mode = st.selectbox(
        "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
    )

    stroke_width = st.slider("Ancho del trazo: ", 1, 25, 3)
    if drawing_mode == 'point':
        point_display_radius = st.slider("Tamaño del punto: ", 1, 25, 3)
    stroke_color = st.color_picker("Color: ")
    #bg_color = st.color_picker("Background color hex: ", "#eee")

    realtime_update = st.checkbox("Actualizar en tiempo real", True)

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
    if st.button("Predecir dibujo"):
        if canvas_result.image_data is not None:
            st.write("Imagen procesada")
            st.image(canvas_result.image_data)
            #aqui irá el modelo 
        else:
            st.write("No hay imagen")

with tab2:
    import streamlit as st
    st.header("O...sube una imágen")
    source_img = st.file_uploader(
    "Escoge una imágen...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

    if st.button("Predecir imagen"):
        if source_img is not None:
            st.write("Imagen procesada")
            st.image(source_img)
            #aqui irá el modelo 
        else:
            st.write("No hay imagen")


