import pandas as pd
import cv2
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import ultralytics
from ultralytics import YOLO

#Importando MODELO
model = YOLO('best.pt')
model2 = YOLO('last.pt')

tab1, tab2 = st.tabs(["Haz un  dibujito ✍️", "Sube una imágen ⬆️"])

with tab1:
    import streamlit as st


    st.header("Haz un dibujito")

    # Especifica los parametros canvas de la aplicacion canvas
    drawing_mode = st.selectbox(
        "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
    )

    stroke_width = st.slider("Ancho del trazo: ", 1, 25, 3)
    if drawing_mode == 'point':
        point_display_radius = st.slider("Tamaño del punto: ", 1, 25, 3)
    stroke_color = st.color_picker("Color: ")
    #FFFDFD - Color blanco del fondo on default, necesario
    bg_color = st.color_picker("Background color hex: ", "#FFFDFD")

    realtime_update = st.checkbox("Actualizar en tiempo real", True)

    modelos_disponibles = {'Modelo 1 (best.pt)': model, 'Modelo 2 (last.pt)': model2}
    option = st.selectbox("Escoja modelo: ", list(modelos_disponibles.keys()))

    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        update_streamlit=realtime_update,
        height=150,
        drawing_mode=drawing_mode,
        point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
        key="canvas",
    )
    

    # Boton predecir:

    if st.button("Predecir dibujo"):
        if canvas_result.image_data is not None:
            # Convertir la imagen a formato RGB
            image = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA')
            image = image.convert('RGB')
            
            # Obtener el modelo seleccionado
            selected_model = modelos_disponibles[option]
            
            # Realizar predicción en el dibujo
            results = selected_model(image)
            
            # Mostrar los resultados de la predicción
            im = results[0].plot()
            st.image(im)
        else:
            st.write("No hay imagen")

with tab2:

    import streamlit as st

    st.header("Sube una imágen")
    source_img = st.file_uploader(
    "Escoge una imágen...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
    
    modelos_subidos = {'Modelo 1 (best.pt)': model, 'Modelo 2 (last.pt)': model2}
    option = st.selectbox("Escoger modelo: ", list(modelos_subidos.keys()))


    if st.button("Predecir imagen"):
        if source_img is not None:

            # Convertir la imagen a formato RGB
            image = Image.open(source_img)
            image = image.convert('RGB')

            modelo_seleccionado = modelos_subidos[option]

            # Realizar predicción en la imagen subida
            results = modelo_seleccionado(image)
            
            # Mostrar los resultados de la predicción
            im = results[0].plot()
            st.image(im)

        else:
            st.write("No hay imagen")
