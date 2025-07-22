"""
streamlit_app.py – Visualización interactiva de análisis de texto

Esta aplicación web forma parte del proyecto académico MASTER-EVOLVE-MODULO-2
y permite realizar análisis textual en tiempo real:
- Limpieza
- Detección de idioma
- Eliminación de stopwords
- Conteo y visualización de frecuencias

Desarrollado por Valentina Bailón Cano · Máster en Data Science & IA – EVOLVE
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import nltk

from proyecto.limpieza import limpiar_texto
from proyecto.analisis import (
    detectar_idioma,
    eliminar_stopwords,
    contar_palabras,
    frecuencia_palabras
)

# Descargar stopwords si no existen (útil para Streamlit Cloud)
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Configuración inicial de Streamlit
st.set_page_config(page_title="MASTER-EVOLVE-MODULO-2", layout="centered")
st.title("🧹 Análisis de Texto — MASTER-EVOLVE-MODULO-2")

st.markdown("""
Esta aplicación analiza tu texto ingresado y te muestra:
- Idioma detectado
- Texto limpio
- Texto sin stopwords
- Conteo de palabras
- Visualizaciones interactivas
""")

# Entrada del usuario
texto_usuario = st.text_area("Introduce tu texto aquí:", height=200)

if texto_usuario:
    with st.spinner("Procesando texto..."):

        # 1. Detección de idioma
        idioma = detectar_idioma(texto_usuario)
        st.success(f"🌍 Idioma detectado: {idioma}")

        # 2. Limpieza del texto
        texto_limpio = limpiar_texto(texto_usuario)
        st.text_area("🔤 Texto limpio:", texto_limpio, height=100)

        # 3. Eliminación de stopwords
        texto_filtrado = eliminar_stopwords(texto_limpio, idioma)
        st.text_area("🧹 Texto sin stopwords:", texto_filtrado, height=100)

        # 4. Conteo y frecuencia
        num_palabras = contar_palabras(texto_filtrado)
        st.write(f"🧮 Número total de palabras significativas: `{num_palabras}`")

        frecuencia = frecuencia_palabras(texto_filtrado)

        if frecuencia:
            # Convertir frecuencias a DataFrame
            df_frec = pd.DataFrame(frecuencia.items(), columns=["Palabra", "Frecuencia"])
            df_frec = df_frec.sort_values(by="Frecuencia", ascending=False)

            # Gráfico de barras
            st.subheader("📊 Frecuencia de palabras (Top 10)")
            fig_bar, ax = plt.subplots(figsize=(10, 4))
            ax.bar(df_frec["Palabra"].head(10), df_frec["Frecuencia"].head(10), color="skyblue")
            ax.set_ylabel("Frecuencia")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig_bar)

            # Gráfico de dispersión
            st.subheader("🔎 Diagrama de dispersión")
            fig_scatter, ax2 = plt.subplots(figsize=(12, 5))
            ax2.scatter(df_frec["Palabra"], df_frec["Frecuencia"], color="purple")
            ax2.set_ylabel("Frecuencia")
            ax2.set_xticks(range(len(df_frec["Palabra"])))
            ax2.set_xticklabels(df_frec["Palabra"], rotation=65, ha='right', fontsize=8)
            plt.tight_layout()
            st.pyplot(fig_scatter)

            # Tabla con resultados
            st.subheader("📋 Tabla de frecuencias")
            st.dataframe(df_frec.reset_index(drop=True))

        else:
            st.info("No se encontraron palabras significativas tras la limpieza y filtrado.")
else:
    st.info("Introduce un texto para comenzar el análisis.")




