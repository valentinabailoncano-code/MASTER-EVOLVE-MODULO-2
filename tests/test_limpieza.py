# ===============================
# test_limpieza.py - Tests para limpieza de texto
# ===============================
# Este archivo valida que la función limpiar_texto
# funcione correctamente en diferentes escenarios.

from mi_libreria_texto import limpiar_texto

def test_limpiar_texto():
    # Elimina puntuación y pone en minúsculas
    assert limpiar_texto("Hola, Mundo!") == "hola mundo"

    # Elimina números
    assert limpiar_texto("Prueba123") == "prueba"

    # Normaliza espacios múltiples
    assert limpiar_texto("   texto   con    espacios ") == "texto con espacios"

    # Maneja tildes correctamente
    assert limpiar_texto("acción rápida") == "acción rápida"

    # No elimina letras con ñ
    assert limpiar_texto("niño señor") == "niño señor"
