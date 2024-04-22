# Streamlit
</div>
<center>

![Image](../assets/streamlit.png)
</center>
</div>

Streamlit es una biblioteca de Python que permite crear aplicaciones web interactivas de manera rápida y sencilla. Es muy utilizada para la visualización de datos y la creación de dashboards.

## Resumen del Código

El código proporciona una plataforma interactiva para el análisis de reseñas de la tienda Walgreens en las plataformas Google y Yelp, así como la visualización de datos y recomendaciones basadas en Machine Learning.

### Funcionalidades Principales

1. **Análisis de Sentimientos de Reseñas:**
   - Utiliza NLTK para el análisis de sentimientos de las reseñas de Walgreens en Google y Yelp.
   - Categoriza las reseñas como positivas, neutrales o negativas.
   - Realiza un análisis de tópicos utilizando LDA (Latent Dirichlet Allocation) para identificar los temas principales en las reseñas.

2. **Dashboard Interactivo:**
   - Presenta un dashboard interactivo con pestañas para la navegación: "Home", "Dashboard" y "Modelos".
   - En la pestaña "Dashboard", muestra visualizaciones de datos utilizando Tableau sobre las reseñas de Walgreens en Google y Yelp.

3. **Recomendación de Tiendas:**
   - Ofrece una función para recomendar las mejores ubicaciones de tiendas de Walgreens basadas en la ubicación y las reseñas positivas de los clientes.

4. **Análisis de Competidores:**
   - Permite comparar las reseñas de Walgreens con las de competidores directos como 7-Eleven, Circle K, etc.
   - Proporciona un análisis de sentimiento y probabilidad de ocurrencia de temas en las reseñas de los competidores.

5. **Análisis de Reseñas por Tienda:**
   - Permite buscar una tienda de Walgreens por su gmap_id y analizar las reseñas asociadas.
   - Realiza un análisis de sentimientos y un análisis de tópicos en las reseñas de la tienda seleccionada.

### Tecnologías Utilizadas

- Python: Utilizado como el lenguaje principal de programación.
- Bibliotecas como Streamlit, Folium, NLTK, Pandas, y Scikit-learn para el procesamiento de datos, visualizaciones y análisis de sentimientos.
- Integración de Tableau para la visualización de datos interactiva.

Este código proporciona una plataforma completa para el análisis de reseñas de clientes de Walgreens, con la capacidad de obtener información útil para mejorar la experiencia del cliente y la toma de decisiones comerciales.
