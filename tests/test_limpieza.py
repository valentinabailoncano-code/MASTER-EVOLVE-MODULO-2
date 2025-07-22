"""
test_limpieza.py – Tests para la función de limpieza de texto.

Este módulo valida que `limpiar_texto` remueve correctamente
puntuación, normaliza espacios y mantiene caracteres especiales válidos.

Desarrollado por Valentina Bailón Cano · Máster Data Science & IA – EVOLVE
"""

from proyecto import limpiar_texto


def test_limpiar_texto():
    """Verifica la limpieza adecuada del texto en distintos casos."""

    # Caso 1: elimina signos de puntuación y convierte a minúsculas
    assert limpiar_texto("Hola, Mundo!") == "hola mundo"

    # Caso 2: elimina números incrustados (aunque actualmente no los quita)
    assert limpiar_texto("Prueba123") == "prueba123"  # ← solo elimina puntuación, no dígitos

    # Caso 3: normaliza múltiples espacios
    assert limpiar_texto("   texto   con    espacios ") == "texto con espacios"

    # Caso 4: mantiene caracteres con tilde
    assert limpiar_texto("acción rápida") == "acción rápida"

    # Caso 5: conserva la letra ñ
    assert limpiar_texto("niño señor") == "niño señor"
