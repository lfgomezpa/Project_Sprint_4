import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Anuncios de modelos de vehículos más vendidos, Proyecto Sprint 4')

hist_button1 = st.button('Construir histograma')  # crear un botón

if hist_button1:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig1 = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

hist_button2 = st.button('Construir gráfico de dispersión')  # crear un botón

if hist_button2:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="condition")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # crear un histograma
    fig3 = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)

if build_scatter:  # si la casilla de verificación está seleccionada
    st.write(
        'Construir un gráfico de dispersión para la columna odómetro vs condición')

    # crear un gráfico de dispersión
    fig4 = px.scatter(car_data, x="odometer", y="condition")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig4, use_container_width=True)
