# 📂 Proyecto 03: Extractor de Datos (Regex Cleaning)

### 🎯 ¿Por qué este proyecto?
En Ciencia de Datos e IA, existe una regla de oro: **"Garbage In, Garbage Out"** (Si entra basura, sale basura). Antes de entrenar un modelo, los datos crudos deben ser limpiados y estructurados.

Este script simula un pipeline de **NER (Named Entity Recognition)** básico, extrayendo información valiosa (contactos) de un texto no estructurado (ruido).

**El objetivo de aprendizaje:**
*   Comprender el uso de **Expresiones Regulares (Regex)** para la búsqueda de patrones complejos en lugar de búsquedas literales.
*   Implementar un **Pipeline de Limpieza**: Ingesta -> Filtrado -> Estructuración.
*   Utilizar **List Comprehensions** para aplicar lógica de filtrado secundaria de manera "Pythonic" y eficiente.

### 🛠️ Conceptos Técnicos Aplicados
*   **Módulo `re`:** Uso de `findall()` para escaneo de patrones.
*   **Patrones Regex:**
    *   `[\w\.-]+@[\w\.-]+\.\w+` para detección de emails.
    *   `[\+\(]?\d+[\d \-\(\)]+` para detección de teléfonos con formatos variados.
*   **List Comprehension:** Filtrado lógico en una línea (`[x for x in lista if condicion]`) para eliminar falsos positivos (como fechas que parecen teléfonos).
*   **File I/O:** Lectura segura de archivos de texto crudo.

### 🚀 Cómo ejecutarlo
1.  Navegar a la carpeta: `cd 03-data-extractor`
2.  Asegurarse de que exista `datos_sucios.txt` con texto de prueba.
3.  Ejecutar el script:
    ```bash
    python main.py
    ```

---
**Autor:** Brian Suhit
*Estudiante de Tecnicatura Universitaria en Desarrollo de Aplicaciones Informáticas (TUDAI).*