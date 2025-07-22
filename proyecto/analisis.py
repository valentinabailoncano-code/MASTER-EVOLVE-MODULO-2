"""
analisis.py – Funciones de análisis de texto limpio.

Incluye herramientas clave para procesamiento textual:
- detectar_idioma: usa langdetect para identificar idioma
- eliminar_stopwords: remueve palabras vacías usando NLTK
- contar_palabras: cuenta palabras significativas
- frecuencia_palabras: calcula la frecuencia de palabras

Desarrollado por Valentina Bailón Cano · Máster Data Science & IA – EVOLVE
"""

from collections import Counter
from langdetect import detect
from typing import Dict
import nltk
from nltk.corpus import stopwords

# Descargar las stopwords si no existen (útil para entornos cloud como Streamlit)
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


def detectar_idioma(texto: str) -> str:
    """
    Detecta el idioma principal del texto usando langdetect.

    Args:
        texto (str): Texto de entrada.

    Returns:
        str: Código del idioma detectado (ej. 'es', 'en', 'fr').
    """
    return detect(texto)


def eliminar_stopwords(texto: str, idioma: str) -> str:
    """
    Elimina las stopwords del texto según el idioma indicado.

    Si el idioma no está disponible en NLTK, se usa 'english' por defecto.

    Args:
        texto (str): Texto ya limpiado.
        idioma (str): Código del idioma (ej. 'es', 'en').

    Returns:
        str: Texto sin palabras vacías.
    """
    if idioma not in stopwords.fileids():
        idioma = 'english'  # Fallback seguro
    stop_words = set(stopwords.words(idioma))
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p not in stop_words]
    return " ".join(palabras_filtradas)


def contar_palabras(texto: str) -> int:
    """
    Cuenta el número de palabras en el texto.

    Args:
        texto (str): Texto de entrada.

    Returns:
        int: Cantidad total de palabras.
    """
    return len(texto.split())


def frecuencia_palabras(texto: str) -> Dict[str, int]:
    """
    Calcula la frecuencia de aparición de cada palabra en el texto.

    Args:
        texto (str): Texto de entrada.

    Returns:
        dict: Diccionario {palabra: frecuencia}.
    """
    palabras = texto.split()
    return dict(Counter(palabras))
