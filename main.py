# ===============================
# main.py - Script de demostración
# ===============================
# Este archivo sirve para ejecutar manualmente la librería
# y visualizar cómo funcionan las funciones principales.

from mi_libreria_texto import (
    limpiar_texto,
    contar_palabras,
    frecuencia_palabras,
    eliminar_stopwords,
    detectar_idioma
)
import matplotlib.pyplot as plt  # Usamos matplotlib para visualizar los datos

if __name__ == "__main__":
    # Texto de entrada que contiene símbolos, mayúsculas y palabras repetidas
    texto = "¡Hola Mundo! Esto es un ejemplo con ejemplo y texto."

    # Detectamos el idioma del texto original
    idioma_detectado = detectar_idioma(texto)
    print(f"Idioma detectado: {idioma_detectado}")

    # Aplicamos limpieza: quita símbolos, convierte a minúsculas, normaliza espacios
    texto_limpio = limpiar_texto(texto)
    print(f"Texto limpio: {texto_limpio}")

    # Eliminamos stopwords basadas en el idioma detectado
    texto_filtrado = eliminar_stopwords(texto_limpio, idioma=idioma_detectado)
    print(f"Texto sin stopwords: {texto_filtrado}")

    # Contamos el número total de palabras después del filtrado
    print(f"Cantidad de palabras: {contar_palabras(texto_filtrado)}")

    # Obtenemos la frecuencia de cada palabra en el texto limpio y filtrado
    frecuencias = frecuencia_palabras(texto_filtrado)
    print(f"Frecuencia de palabras: {frecuencias}")

    # ===============================
    # Visualización: Gráfico de barras
    # ===============================
    palabras = list(frecuencias.keys())
    conteos = list(frecuencias.values())

    plt.figure(figsize=(10, 5))
    plt.bar(palabras, conteos, color='skyblue')
    plt.title('Frecuencia de palabras (sin stopwords)')
    plt.xlabel('Palabras')
    plt.ylabel('Cantidad')
    plt.tight_layout()
    plt.show()
