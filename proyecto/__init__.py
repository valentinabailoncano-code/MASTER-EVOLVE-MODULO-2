# ===============================
# __init__.py - Punto de entrada del paquete
# ===============================
# Este archivo permite importar directamente las funciones
# principales desde el paquete "mi_libreria_texto".

from .limpieza import limpiar_texto  # Limpieza del texto
from .analisis import (
    contar_palabras,  # Cuenta el número total de palabras
    frecuencia_palabras,  # Cuenta la frecuencia de cada palabra
    eliminar_stopwords,  # Elimina palabras vacías (stopwords)
    detectar_idioma  # Detecta el idioma del texto
)
