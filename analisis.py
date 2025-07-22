# ===============================
# analisis.py - Funciones de análisis de texto
# ===============================
# Este archivo incluye funciones para analizar texto limpio:
# - contar_palabras: número total de palabras
# - frecuencia_palabras: cuántas veces aparece cada palabra
# - eliminar_stopwords: elimina palabras vacías como "el", "de", "y" (usando nltk)
# - detectar_idioma: intenta detectar automáticamente el idioma del texto

from collections import Counter
from langdetect import detect
import nltk
from nltk.corpus import stopwords

# Forzar descarga de 'stopwords' si no están (para Streamlit Cloud)
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def detectar_idioma(texto):
    """
    Detecta el idioma de un texto usando langdetect.
    """
    return detect(texto)

def eliminar_stopwords(texto, idioma):
    """
    Elimina las stopwords según el idioma detectado.
    """
    if idioma not in stopwords.fileids():
        idioma = 'english'  # fallback seguro
    stop_words = set(stopwords.words(idioma))
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra not in stop_words]
    return " ".join(palabras_filtradas)

def contar_palabras(texto):
    """
    Cuenta el número de palabras significativas en el texto.
    """
    return len(texto.split())

def frecuencia_palabras(texto):
    """
    Devuelve la frecuencia de cada palabra en un texto como diccionario.
    """
    palabras = texto.split()
    return dict(Counter(palabras))
