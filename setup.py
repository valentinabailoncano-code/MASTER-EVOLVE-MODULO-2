# ===============================
# setup.py - Configuración del paquete
# ===============================
# Este archivo permite instalar la librería como paquete
# usando el comando: pip install .
# Incluye metadatos y dependencias necesarias.

from setuptools import setup, find_packages

setup(
    name='mi_libreria_texto',  # Nombre del paquete
    version='0.1.0',  # Versión inicial
    packages=find_packages(),  # Detecta todos los subpaquetes automáticamente
    install_requires=[],  # Dependencias externas (añadidas por requirements.txt)
    author='Valentina Bailón Cano',  # Tu nombre
    description='Librería para limpiar y analizar texto con visualización de frecuencias.',
    url='https://github.com/valentinabailoncano-code/mi_libreria_texto',  # URL del repo en GitHub
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
