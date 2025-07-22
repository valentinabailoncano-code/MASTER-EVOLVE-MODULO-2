"""
test_analisis.py – Tests para funciones de análisis léxico.

Este módulo comprueba que las funciones de conteo y frecuencia
de palabras del paquete `proyecto` funcionan correctamente.

Desarrollado por Valentina Bailón Cano · Máster Data Science & IA – EVOLVE
"""

from proyecto import contar_palabras, frecuencia_palabras


def test_contar_palabras():
    """Verifica el conteo total de palabras en distintos escenarios."""

    # Caso 1: dos palabras simples
    assert contar_palabras("hola mundo") == 2

    # Caso 2: palabras repetidas
    assert contar_palabras("hola hola hola") == 3

    # Caso 3: frase completa
    assert contar_palabras("esto es una prueba completa") == 5


def test_frecuencia_palabras():
    """Verifica el cálculo de frecuencia de palabras."""

    # Caso 1: repeticiones
    resultado = frecuencia_palabras("hola mundo hola")
    assert resultado == {"hola": 2, "mundo": 1}

    # Caso 2: todas únicas
    resultado = frecuencia_palabras("uno dos tres")
    assert resultado == {"uno": 1, "dos": 1, "tres": 1}
