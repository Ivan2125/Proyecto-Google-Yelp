<div align="center">
<img src='./assets/WAG_Signature_logo_RGB.png' width=60%>
  <h1>Estudio de presencia en plataformas Google Maps y Yelp</h1>
<img src='./assets/g1-logo.png' width=10%>
</div>


## Contenido

- [Propuesta](#propuesta)
- [Objetivos](#objetivos)
- [Infraestructura Técnológica](#infraestructura-técnológica)
- [Despliegue](#despliegue)
- [Herramientas](#herramientas)

## Propuesta

En un mundo donde 
- 1 billón de personas utilizan Google Maps cada mes  
- 2.5 millones de aplicaciones integran sus servicios
- 287 millones de reseñas y recomendaciones de usuarios acumuladas en Yelp 

Podemos decir que nos encontramos ante una revolución digital que transforma cómo interactuamos con los espacios y negocios a nuestro alrededor. Para una marca líder como Walgreens, con una presencia significativa tanto en el espacio físico como en el digital, estas plataformas ofrecen una oportunidad única para gestionar su presencia en línea, interactuar con los clientes y mejorar la experiencia del consumidor.

Este proyecto busca presentar cómo Walgreens puede capitalizar este potencial. 


## Objetivos

- Detectar 3 oportunidades de negocios y mejoras derivadas del estudio de las reseñas de nuestro cliente y de la competencia mediante un [análisis exploratorio de datos](02-eda-etl). 
- Visualizar, dimensionar y calificar la presencia de Walgreens en plataformas Google Maps y Yelp a través de un [tablero interactivo](09-dashboard)
- Generar [modelos de recomendación](03-ml-model) para el cliente a partir de las reseñas de la competencia, mediante criterios de geolocalización y percepción del servicio. 


## Infraestructura tecnológica

Este proyecto utiliza una combinación de tecnologías para crear una infraestructura robusta y escalable. Puedes encontrar el detalle de cada herramienta en su carpeta respectiva. 

- [Cloud](04-cloud) contiene la configuración y los scripts para implementar los recursos de la nube, como servidores virtuales, redes y almacenamiento. Utilizamos Google Cloud Platform como proveedor de nube
- [Mage](05-mage) contiene los archivos de configuración y los scripts para implementar y administrar las aplicaciones del proyecto. Utilizamos Mage para orquestar la implementación y gestión de las aplicaciones
- [Terraform](08-terraform) contiene los archivos de configuración de Terraform para definir y provisionar la infraestructura de manera declarativa. Terraform nos permite automatizar la creación y gestión de la infraestructura, lo que facilita la implementación y el mantenimiento del proyecto.

## Despliegue 

Para facilitar el acceso del cliente a los productos, los hemos desplegado en [Streamlit](https://app-test-kqpydgyxdbfoqjsnqxxdoi.streamlit.app). Esta aplicación permite a los usuarios interactuar con el dashboard de Tableau y los modelos de recomendación de una manera fácil e intuitiva. Puedes encontrar el detalle del despliegue [aquí](07-streamlit)  

## Herramientas

![Python](https://img.shields.io/badge/-Python-7fdbca?style=flat&logo=python)
![GitHub](https://img.shields.io/badge/-GitHub-7fdbca?style=flat&logo=github)
![Jupyter](https://img.shields.io/badge/-Jupyter-7fdbca?style=flat&logo=jupyter)
![Pandas](https://img.shields.io/badge/-Pandas-7fdbca?style=flat&logo=pandas)
![Geopandas](https://img.shields.io/badge/-Geopandas-7fdbca?style=flat&logo=Geopandas)
![Terraform](https://img.shields.io/badge/-Terraform-7fdbca?style=flat&logo=Terraform)
![Mage](https://img.shields.io/badge/-Mage-7fdbca?style=flat&logo=Mage)
![Numpy](https://img.shields.io/badge/-Numpy-7fdbca?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-7fdbca?style=flat&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/-Seaborn-7fdbca?style=flat&logo=seaborn)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-7fdbca?style=flat&logo=scikitlearn)
![NLTK](https://img.shields.io/badge/-NLTK-7fdbca?style=flat&logo=NLTK)
![Gensim](https://img.shields.io/badge/-Gensim-7fdbca?style=flat&logo=Gensim)
![Folium](https://img.shields.io/badge/-Folium-7fdbca?style=flat&logo=Folium)
![GoogleCloudPlatform](https://img.shields.io/badge/-GoogleCloudPlatform-7fdbca?style=flat&logo=google-cloud-platform)
![GoogleCloudStorage](https://img.shields.io/badge/-GoogleCloudStorage-7fdbca?style=flat&logo=GoogleCloudStorage)
![GoogleBigQuery](https://img.shields.io/badge/-GoogleBigQuery-7fdbca?style=flat&logo=GoogleBigQuery)
![Tableau](https://img.shields.io/badge/-Tableau-7fdbca?style=flat&logo=tableau)
![Streamlit](https://img.shields.io/badge/-Streamlit-7fdbca?style=flat&logo=streamlit)






