# 🧹 MASTER-EVOLVE-MODULO-2
![Streamlit](https://img.shields.io/badge/Streamlit-App%20Activa-brightgreen?logo=streamlit)
![Pytest](https://img.shields.io/badge/Tests-Pasando-blue?logo=pytest)
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

Librería Python desarrollada por **Valentina Bailón Cano** en el marco del Máster en Data Science & IA de **Evolve**.

Ofrece funciones de procesamiento y análisis léxico de texto con:
- Limpieza avanzada
- Detección automática de idioma
- Eliminación de stopwords multilingües
- Visualización de frecuencias

---

## 🚀 Funcionalidades principales

- 🔤 **Limpieza del texto**  
  Convierte a minúsculas, elimina símbolos y espacios innecesarios.

- 🌍 **Detección automática del idioma**  
  Identifica si el texto está en español, inglés, etc.

- 🧹 **Eliminación de stopwords**  
  Elimina palabras vacías como “el”, “de”, “and”, etc. según el idioma detectado.

- 🧮 **Conteo de palabras**  
  Calcula el número total de palabras significativas.

- 📊 **Frecuencia de palabras**  
  Calcula cuántas veces aparece cada palabra y las visualiza en un gráfico de barras o dispersión.

---

## 🧪 Ejemplo de uso

```python
from proyecto import (
    limpiar_texto,
    detectar_idioma,
    eliminar_stopwords,
    contar_palabras,
    frecuencia_palabras
)

texto = "¡Hola Mundo! Esto es un ejemplo de texto."

idioma = detectar_idioma(texto)
texto_limpio = limpiar_texto(texto)
texto_filtrado = eliminar_stopwords(texto_limpio, idioma)
conteo = contar_palabras(texto_filtrado)
frecuencias = frecuencia_palabras(texto_filtrado)

print(f"Idioma: {idioma}")
print(f"Texto limpio: {texto_limpio}")
print(f"Texto sin stopwords: {texto_filtrado}")
print(f"Número de palabras: {conteo}")
print(f"Frecuencias: {frecuencias}")
```

---

## 📁 Estructura del proyecto

```
MASTER-EVOLVE-MODULO-2/
├── proyecto/
│   ├── __init__.py
│   ├── limpieza.py
│   └── analisis.py
│   └── main.py
│
├── tests/
│   ├── test_limpieza.py
│   └── test_analisis.py
│
├── streamlit_app.py
├── requirements.txt
├── demo.ipynb
├── setup.py
└── README.md
```

---

## 🧩 Requisitos e instalación

Instala las dependencias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

O instala el paquete localmente en modo editable:

```bash
pip install -e .
```

---

## 🌐 Aplicación Web

Accede a la app online desarrollada con Streamlit:  
🔗 [Abrir en Streamlit Cloud](https://master-evolve-modulo-2.streamlit.app/)

---

## 👩‍💻 Autora

**Valentina Bailón Cano**  
Máster en Data Science & IA – Evolve  
📎 [LinkedIn](https://www.linkedin.com/in/valentina-bailon-2653b22b7/)  
🔗 [Ver repositorio en GitHub](https://github.com/valentinabailoncano-code/MASTER-EVOLVE-MODULO-2)

---
