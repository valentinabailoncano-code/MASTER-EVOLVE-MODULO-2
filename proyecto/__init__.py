"""
__init__.py – Punto de entrada del paquete `proyecto`.

Permite importar directamente las funciones clave para
el procesamiento y análisis de texto.

Desarrollado por Valentina Bailón Cano · Máster Data Science & IA – EVOLVE
"""

# Funciones de limpieza
from .limpieza import limpiar_texto

# Funciones de análisis
from .analisis import (
    contar_palabras,
    frecuencia_palabras,
    eliminar_stopwords,
    detectar_idioma
)
__version__ = "0.1"

