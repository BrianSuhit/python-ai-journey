# 📂 Proyecto 04: Clasificador Visual KNN (Machine Learning Manual)

### 🎯 ¿Por qué este proyecto?
Este es el "Jefe Final" ( de momento ) de mis proyectos de lógica Vanilla. Finalizando con un proyecto/practica de **Algoritmos Predictivos**.

Implemente el algoritmo **K-Nearest Neighbors (K-Vecinos Más Cercanos)** desde cero, sin usar librerías de IA como Scikit-Learn. El objetivo era entender matemáticamente cómo una computadora "ve" similitudes entre datos.

**El objetivo de aprendizaje:**
*   Comprender que para una IA, la "similitud" es simplemente **Distancia Geométrica** en un espacio vectorial.
*   Implementar la **Distancia Euclidiana** (Teorema de Pitágoras) para medir cercanía entre puntos.
*   Visualizar datos (Data Visualization) para entender la separabilidad de las clases antes de programar.

### 🛠️ Conceptos Técnicos Aplicados
*   **Pandas:** Carga y estructuración del dataset (`Data_Frame`).
*   **Matplotlib / Seaborn:** Visualización de datos en un Scatter Plot para identificar clústeres visualmente.
*   **Matemática Pura:** Implementación manual de la fórmula de distancia: `√(x2-x1)² + (y2-y1)²`.
*   **Algoritmo KNN:**
    1.  Calcular distancia entre el punto nuevo y TODOS los puntos existentes.
    2.  Ordenar las distancias de menor a mayor.
    3.  Tomar los **K** primeros vecinos (K=3).
    4.  Realizar una votación por mayoría simple para clasificar.

### 🚀 Cómo ejecutarlo
1.  Navegar a la carpeta: `cd 04-knn-visual`
2.  Ejecutar el script:
    ```bash
    python main.py
    ```
3.  Ingresar valores de prueba (Ej: Peso 4, Altura 20 para un gato).
4.  Observar el gráfico y luego la clasificación en la terminal.

---
**Autor:** Brian Suhit  
*Estudiante de Tecnicatura Universitaria en Desarrollo de Aplicaciones Informáticas (TUDAI).*