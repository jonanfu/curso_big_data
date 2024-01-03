import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import plotly.express as px # interactive charts 
from wordcloud import WordCloud
import json

parquet_file_path = "data/df_cleaned.parquet"

# read csv from a github repo
df = pd.read_parquet(parquet_file_path)

df_date = df
# Extraer el mes de la columna 'date'
df_date['mes'] = df_date['date'].dt.strftime('%B')

# Establecer el orden de los meses
orden_meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Aplicar el orden personalizado a la columna 'mes'
df_date['mes'] = pd.Categorical(df_date['mes'], categories=orden_meses, ordered=True)

# Pivote del DataFrame
df_pivot = df_date.pivot_table(index='mes', columns='code', aggfunc='size', fill_value=0)


# Filtrar por código 400 y extraer valores de 'search'
filtered_data = df[df['code'] == 400]['payload']
search_values = filtered_data.apply(lambda x: json.loads(x)['search'].lower() if pd.notnull(x) else '').tolist()

# Eliminar duplicados y unir los valores de 'search' en una cadena
unique_text_data = ' '.join(set(search_values))

# Crear la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(unique_text_data)

# Configurar la aplicación para que ocupe toda la pantalla
st.set_page_config(page_title='Streamlit App', layout='wide')

# Layout de Streamlit con contenedor
with st.container():
    # Título
    st.title('Dashboard')


    # Crear una línea de tiempo con Plotly Express
    fig = px.line(df_pivot, x=df_pivot.index, y=df_pivot.columns, title='Registros de errores por mes')
    st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns(2)

with col1:
    fig = px.sunburst(df, path=['code', 'instance', 'path'])
    # Mostrar el Sunburst Plot
    st.plotly_chart(fig)

with col2:
    st.subheader('Errores en busquedas')
    # Mostrar la nube de palabras en Streamlit
    st.image(wordcloud.to_image())

# Tabla

st.subheader('Registro de error')
st.dataframe(df)