# ===============================
# limpieza.py - Funciones de limpieza de texto
# ===============================
# Contiene una única función que normaliza el texto:
# - Convierte a minúsculas
# - Elimina símbolos y signos de puntuación
# - Elimina espacios innecesarios

import re

# Función para limpiar texto antes del análisis
# Elimina signos de puntuación y convierte todo a minúsculas

def limpiar_texto(texto):
    """
    Limpia el texto eliminando puntuación y convirtiendo todo a minúsculas.
    """
    texto = texto.lower()  # Pasar a minúsculas
    texto = re.sub(r'[^\w\s]', '', texto)  # Eliminar signos de puntuación
    texto = re.sub(r'\s+', ' ', texto).strip()  # Quitar espacios extra
    return texto
