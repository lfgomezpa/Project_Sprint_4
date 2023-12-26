import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Anuncios venta de vehículos, Proyecto Sprint 4')

hist_button1 = st.button(
    'Construir histograma - Tipo de vehículo')  # crear un botón

if hist_button1:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos del tipo de vehículo de mayor oferta en el mercado de autos')

    # crear un histograma
    fig1 = px.histogram(car_data, x="type")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

hist_button2 = st.button(
    'Construir gráfico de dispersión - Precio v.s. Año')  # crear un botón

if hist_button2:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para describir la relación del precio con el año de su modelo')
    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="model_year", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)


build_histogram = st.checkbox('Histograma - Días publicado')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Creación de un histograma para visualizar el tiempo que se tienen publicados los vehículos en días')

    # crear un histograma
    fig3 = px.histogram(car_data, x="days_listed")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)
