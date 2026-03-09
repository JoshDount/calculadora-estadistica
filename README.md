# 🖍️ Calculadora de Probabilidad (Estilo Pizarrón)

Una calculadora interactiva y visual de estadística para distribuciones poblacionales y muestrales de medias. Construida con Python utilizando **Streamlit**, **SciPy**, y **Matplotlib**.

## 📊 Características

*   **Cálculo Inmediato:** Calcula el área bajo la curva (probabilidad) a partir de los límites, la media, la desviación estándar y el tamaño de muestra.
*   **Diseño Estilo Pizarrón:** Gráficas simuladas a mano para facilitar la comprensión visual de los problemas, tal como se enseñarían en clase.
*   **Dualidad de Gráficas:** Muestra simultáneamente la distribución con los valores reales del problema (X) y la versión estandarizada (Z).
*   **Áreas Explicadas:** Divide y calcula visualmente el área izquierda y derecha en la distribución Z.

## 🚀 Cómo ejecutarlo localmente

Asegúrate de tener Python instalado y luego sigue estos pasos:

1. **Clona este repositorio o descarga los archivos:**
   ```bash
   git clone https://github.com/JoshDount/calculadora-estadistica.git
   cd calculadora-estadistica
   ```

2. **(Opcional pero recomendado) Crea y activa un entorno virtual:**
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Mac/Linux:
   source .venv/bin/activate
   ```

3. **Instala las dependencias necesarias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicia la aplicación con Streamlit:**
   ```bash
   streamlit run app.py
   ```

5. **Abre tu navegador:**
   La aplicación debería abrirse automáticamente en `http://localhost:8501`.

## 🛠️ Tecnologías utilizadas
*   **[Streamlit](https://streamlit.io/):** Para la interfaz de usuario web rápida e interactiva.
*   **[Matplotlib](https://matplotlib.org/):** Para la creación de las gráficas de campana de Gauss (usando el estilo `xkcd()` para el efecto pizarrón).
*   **[SciPy](https://scipy.org/):** Para los cálculos estadísticos precisos (`scipy.stats.norm`).
*   **[NumPy](https://numpy.org/):** Para el manejo de rangos de datos en los ejes de las gráficas.
