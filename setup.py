"""
setup.py – Configuración del paquete `proyecto`.

Permite instalar el paquete localmente con: pip install .
Incluye metadatos, dependencias y detección automática de submódulos.

Desarrollado por Valentina Bailón Cano · Máster Data Science & IA – EVOLVE
"""

from setuptools import setup, find_packages

setup(
    name='proyecto',  # Nombre del paquete real
    version='0.1.0',
    packages=find_packages(),  # Encuentra todos los subpaquetes (como "proyecto/")
    install_requires=[
        'nltk',
        'langdetect',
        'matplotlib'
    ],
    author='Valentina Bailón Cano',
    description='Librería educativa para limpieza, análisis y visualización de texto',
    url='https://github.com/valentinabailoncano-code/MASTER-EVOLVE-MODULO-2',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
# Este archivo setup.py permite instalar el paquete localmente
# con el comando `pip install .` en la raíz del proyecto.
# Incluye metadatos, dependencias y detecta automáticamente los submódulos.
