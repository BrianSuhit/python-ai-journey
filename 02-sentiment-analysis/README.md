# 📂 Proyecto 02: Analizador de Sentimientos (Scoring Logic)

### 🎯 ¿Por qué este proyecto?
Este script representa el siguiente escalón en la ingeniería de IA: pasar de la **Lógica Booleana** (Chatbot) a la **Aritmética de Pesos** (Scoring).

Es una introducción práctica al **NLP (Procesamiento de Lenguaje Natural)**. Antes de los modelos Transformers (como GPT), el análisis de sentimientos se hacía mediante sistemas expertos basados en diccionarios de pesos ("Bag of Words" con scoring).

**El objetivo de aprendizaje:**
*   Entender el concepto de **Tokenización** (romper frases en datos procesables).
*   Implementar una **Base de Conocimiento** usando Diccionarios (`Key: Value`).
*   Aplicar la lógica de **Suma Ponderada** (Weighted Sum), que es el principio matemático básico de cómo una neurona artificial procesa información.

### 🛠️ Conceptos Técnicos Aplicados
*   **Diccionarios (`{}`):** Uso de estructuras clave-valor para asignar "pesos emocionales" a las palabras.
*   **Normalización y Tokenización:** Uso de `.lower()` y `.split()` para transformar lenguaje humano en una lista de tokens procesables por la máquina.
*   **Algoritmo de Acumulación:** Un bucle `for` que recorre los tokens, busca sus valores en el diccionario y actualiza una variable de estado (`score_total`).
*   **Lógica Difusa (Fuzzy Logic) Básica:** El sistema no solo dice "Bien" o "Mal", calcula un espectro numérico donde el 0 representa la neutralidad o el conflicto (amor + odio = 0).

### 🚀 Cómo ejecutarlo
1.  Navegar a la carpeta: `cd 02-sentiment-analysis`
2.  Ejecutar el script:
    ```bash
    python main.py
    ```
3.  Ingresar una frase cuando el sistema lo pida (ej: *"Hoy es un día excelente"*).

---
**Autor:** Brian Suhit  
*Estudiante de Tecnicatura Universitaria en Desarrollo de Aplicaciones Informáticas (TUDAI).*

