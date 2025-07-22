"""
limpieza.py – Funciones para preprocesar texto antes del análisis.

Este módulo contiene funciones básicas para preparar el texto:
- Conversión a minúsculas
- Eliminación de signos de puntuación
- Normalización de espacios

Desarrollado por Valentina Bailón Cano · Máster Data Science & IA – EVOLVE
"""

import re


def limpiar_texto(texto: str) -> str:
    """
    Limpia el texto eliminando puntuación, espacios innecesarios
    y convirtiendo todo a minúsculas.

    Args:
        texto (str): Texto original a limpiar.

    Returns:
        str: Texto procesado y limpio.
    
    Ejemplo:
        >>> limpiar_texto("¡Hola, Mundo!   Esto es una PRUEBA.")
        'hola mundo esto es una prueba'
    """
    texto = texto.lower()                              # Convertir a minúsculas
    texto = re.sub(r'[^\w\s]', '', texto)              # Eliminar signos de puntuación
    texto = re.sub(r'\s+', ' ', texto).strip()         # Normalizar espacios en blanco
    return texto
