"""
main.py – Script de demostración de procesamiento de texto.

Este archivo ejecuta paso a paso el flujo de análisis de texto:
- Limpieza
- Eliminación de stopwords
- Detección de idioma
- Conteo de palabras
- Visualización de frecuencias

Desarrollado por Valentina Bailón Cano · Máster Data Science & IA – EVOLVE
"""

from proyecto.analisis import (
    limpiar_texto,
    contar_palabras,
    frecuencia_palabras,
    eliminar_stopwords,
    detectar_idioma
)
import matplotlib.pyplot as plt


def ejecutar_demostracion():
    # Texto de entrada original
    texto = "¡Hola Mundo! Esto es un ejemplo con ejemplo y texto."

    # 1. Detectar idioma
    idioma_detectado = detectar_idioma(texto)
    print(f"🌍 Idioma detectado: {idioma_detectado}")

    # 2. Limpiar texto: quitar signos, pasar a minúsculas, normalizar
    texto_limpio = limpiar_texto(texto)
    print(f"🧹 Texto limpio: {texto_limpio}")

    # 3. Eliminar stopwords del idioma detectado
    texto_filtrado = eliminar_stopwords(texto_limpio, idioma=idioma_detectado)
    print(f"🚫 Texto sin stopwords: {texto_filtrado}")

    # 4. Contar palabras
    total_palabras = contar_palabras(texto_filtrado)
    print(f"🔢 Cantidad de palabras: {total_palabras}")

    # 5. Calcular frecuencia de palabras
    frecuencias = frecuencia_palabras(texto_filtrado)
    print(f"📊 Frecuencia de palabras: {frecuencias}")

    # 6. Visualizar frecuencias con gráfico de barras
    visualizar_frecuencias(frecuencias)


def visualizar_frecuencias(frecuencias):
    """Genera un gráfico de barras con las frecuencias de palabras."""
    palabras = list(frecuencias.keys())
    conteos = list(frecuencias.values())

    plt.figure(figsize=(10, 5))
    plt.bar(palabras, conteos, color='skyblue')
    plt.title('Frecuencia de palabras (sin stopwords)')
    plt.xlabel('Palabras')
    plt.ylabel('Cantidad')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    ejecutar_demostracion()
# Este bloque asegura que el script se ejecute solo si es el archivo principal
# y no cuando se importe como módulo en otro script.
# Esto permite reutilizar las funciones de análisis en otros contextos sin ejecutar la demostración automáticamente.