# ===============================
# test_analisis.py - Tests para análisis de texto
# ===============================
# Este archivo comprueba que las funciones de análisis léxico
# devuelven los resultados correctos sobre texto limpio.

from mi_libreria_texto import contar_palabras, frecuencia_palabras

def test_contar_palabras():
    # Caso simple con dos palabras
    assert contar_palabras("hola mundo") == 2

    # Caso con palabras repetidas
    assert contar_palabras("hola hola hola") == 3

    # Frase completa
    assert contar_palabras("esto es una prueba completa") == 5

def test_frecuencia_palabras():
    # Verifica que cuente bien las repeticiones
    resultado = frecuencia_palabras("hola mundo hola")
    assert resultado == {"hola": 2, "mundo": 1}

    # Con palabras únicas
    resultado = frecuencia_palabras("uno dos tres")
    assert resultado == {"uno": 1, "dos": 1, "tres": 1}
