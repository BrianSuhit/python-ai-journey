# 📂 Proyecto 05: Generador de Texto (Markov Chains)

### 🎯 ¿Por qué este proyecto?
Este proyecto representa el **"Habla"** de nuestra IA. Hasta ahora, hemos clasificado y limpiado datos, pero no hemos generado contenido nuevo.

Aquí desmitificamos la **IA Generativa**. Implementamos una **Cadena de Markov**, un modelo probabilístico que predice la "siguiente palabra" basándose en el estado actual. Es el antepasado lógico de los **LLMs (Large Language Models)** modernos.

**El objetivo de aprendizaje:**
*   Comprender el concepto de **Next Token Prediction** (Predicción del siguiente token), que es la base de cómo escribe ChatGPT.
*   Entender la **"Alucinación"**: Veremos cómo la máquina inventa oraciones gramaticalmente correctas pero sin sentido real, basándose pura estadística.
*   Aplicar **POO (Programación Orientada a Objetos)**: En lugar de funciones sueltas, construiremos una Clase `MarkovChain` que tenga "memoria" (entrenamiento) y "métodos" (generación).

### 🛠️ Conceptos Técnicos Aplicados
*   **POO (Clases y Objetos):** Encapsulamiento de la lógica del modelo.
*   **Estructuras de Datos Complejas:** Uso de diccionarios donde los valores son listas (`{ "palabra": ["opcion_a", "opcion_b"] }`).
*   **Probabilidad y Aleatoriedad:** Uso del módulo `random` para seleccionar la siguiente palabra basándose en la frecuencia de aparición en el texto de entrenamiento.
*   **Ingesta de Texto:** Procesamiento de corpus de texto real (libros, artículos) para "entrenar" el modelo.

### 🚀 Cómo ejecutarlo
1.  Navegar a la carpeta: `cd 05-markov-chain`
2.  Asegurarse de tener un archivo de texto para entrenar (ej: `libro.txt`) o usar el texto de prueba incluido.
3.  Ejecutar el script:
    ```bash
    python main.py
    ```

---
**Autor:** Brian Suhit  
*Estudiante de Tecnicatura Universitaria en Desarrollo de Aplicaciones Informáticas (TUDAI).*