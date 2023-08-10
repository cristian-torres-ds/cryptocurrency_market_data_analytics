import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if st.checkbox('Mostrar texto'):
    st.write('hola')

fields = ['country', 'points', 'price', 'variety']

df = pd.read_csv('wine_reviews.csv', usecols=fields)
df.dropna(inplace=True)

if st.checkbox('Mostrar dataframe'):
    st.dataframe(df)



if st.checkbox('Vista de datos head o tail'):
    if st.button('Motrar Head'):
        st.write(df.head())
    if st.button('Motrar Tail'):
        st.write(df.tail())




dim = st.radio('Dimension a mostrar:', ('Filas', 'Columnas'), horizontal=True)

if dim == 'Filas':
    st.write('Cantidad de filas: ', df.shape[0])
else:
    st.write('Cantidad de columnas: ', df.shape[1])




precio_limite = st.slider('Definir precio máximo', 0, 4000, 250)

fig = plt.figure(figsize=(6,4))
sns.scatterplot(x='price', y='points', data=df[df['price']<precio_limite])
st.pyplot(fig)



countries_list = df['country'].unique().tolist()
countries = st.multiselect('Seleccione país/es: ', countries_list, default=['Argentina', 'Chile', 'Spain'])

df_countries = df[df['country'].isin(countries)]
fig = plt.figure(figsize=(6,4))
sns.scatterplot(x='price', y='points', hue='country', data=df_countries[df_countries['price']<precio_limite])
st.pyplot(fig)




col1, col2 = st.columns(2)

with col1:
    df_countries = df[df['country']=='Argentina']
    fig = plt.figure()
    sns.scatterplot(x='price', y='points', data=df_countries)
    plt.title('Puntajes según precio para Argentina')
    st.pyplot(fig)

with col1:
    df_countries = df[df['country']=='Chile']
    fig = plt.figure()
    sns.scatterplot(x='price', y='points', data=df_countries)
    plt.title('Puntajes según precio para Chile')
    st.pyplot(fig)