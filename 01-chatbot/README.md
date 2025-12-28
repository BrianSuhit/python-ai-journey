## 📂 Proyecto 01: Chatbot "Rule-Based" (Lógica Determinística)

### 🎯 ¿Por qué este proyecto?
En la era de los LLMs (ChatGPT, Gemini), es fácil olvidar cómo funcionan los sistemas base. Este proyecto simula un **Asistente Virtual Clásico** basado en reglas.

**El objetivo de aprendizaje:**
*   Entender el **Flujo de Diálogo** (Input/Output loop).
*   Implementar **Reconocimiento de Intención** (Intent Recognition) básico mediante búsqueda de palabras clave, sin usar Machine Learning.
*   Dominar el control de flujo (`While Loops`, `Conditionals`) y manipulación de Strings.

### 🛠️ Conceptos Técnicos Aplicados
*   **Bucle Infinito (`while True`):** Para mantener la sesión del bot activa "escuchando" constantemente.
*   **Normalización de Datos:** Uso de `.lower()` para procesar inputs sin importar mayúsculas/minúsculas.
*   **Lógica de Inclusión (`in`):** Detección de keywords dentro de frases complejas (el precursor del NLP moderno).
*   **Control de Flujo:** Uso estructurado de `if/elif/else` para priorizar comandos (ej: "salir" tiene prioridad sobre "contacto").

### 🚀 Cómo ejecutarlo
1.  Clonar el repositorio.
2.  Navegar a la carpeta: `cd 01-chatbot`
3.  Ejecutar el script:
    ```bash
    python main.py
    ```

---
**Autor:** Brian Suhit  
*Estudiante de Tecnicatura Universitaria en Desarrollo de Aplicaciones Informáticas (TUDAI).*