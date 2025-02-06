import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target  # Agregar la columna objetivo

fig, ax = plt.subplots(1,1)
df.plot(kind='scatter', x='sepal length (cm)', y='petal length (cm)', title='Sepal vs Petal',ax=ax)
estadisticas=df.describe().reset_index()


# Título de la aplicación
st.title("Mi primera aplicación con Streamlit 🚀")

# Agregar un texto
st.write("¡Bienvenido a tu primera aplicación interactiva en Python!")
st.pyplot(fig)
if st.button("Mostrar grafico"):
    st.pyplot(fig)
    st.dataframe(estadisticas)
   # st.write(f"Hola, {nombre}! 🎉 Bienvenido a Streamlit.")
   