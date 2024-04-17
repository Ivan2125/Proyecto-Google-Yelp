import base64
import json
import nltk
import numpy as np
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from gensim import corpora, models
from gettext import gettext as _
from scipy.linalg import triu
from sklearn.neighbors import NearestNeighbors
from statistics import mean
from st_on_hover_tabs import on_hover_tabs
from streamlit_folium import folium_static, st_folium

# Organizar las importaciones
import folium

# Evitar la descarga de paquetes NLTK en cada ejecución
nltk_packages = ['punkt', 'wordnet']
for package in nltk_packages:
    try:
        nltk.data.find(f'tokenizers/{package}')
    except LookupError:
        nltk.download(package)




st.set_page_config(
    layout= "wide",
    page_title="Análisis de Sentimientos de Reviews de Walgreens en Google y Yelp",
    page_icon="star",
    initial_sidebar_state="expanded"
)

def get_style():
    with open('./style.css') as f:
        return f.read()

style = get_style()
st.markdown(f'<style>{style}</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Dashboard', "Modelos"], 
                         iconName=['home', 'dashboard', 'search'], default_choice=0,
                         styles = {'navtab': {'background-color':'#2E3159',
                                                  'color': '#FFFFFF',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'}},
                             key="1")
if tabs=="Home":
            # Open the image file
            
            # Open the first image file
            img1 = Image.open('images/g1-logo.png')        
            
            # Convert the image to base64
            with open("images/g1-logo.png", "rb") as img_file:
                b64_1 = base64.b64encode(img_file.read()).decode()
            
            # Open the second image file
            img2 = Image.open('images/walg-logo.png')  # Replace with the path to your second logo
            
            # Convert the image to base64
            with open("images/walg-logo.png", "rb") as img_file:  # Replace with the path to your second logo
                b64_2 = base64.b64encode(img_file.read()).decode()
            
            # Display the images
            # Display the images
            st.markdown(f'<div style="display: flex; justify-content: center; align-items: center;"><img src="data:image/png;base64,{b64_1}" style="margin-right: 10px; width: 300px; height: 300px;" /><img src="data:image/png;base64,{b64_2}" style="margin-left: 100px; width: 600px; height: 200px;" /></div>', unsafe_allow_html=True)
            
            
            st.header("Bienvenidos ⭐", divider='rainbow')
            
            intro = """
            Hola, en esta plataforma podrás gestionar y administrar de manera útil y práctica las opiniones de los clientes. Esta herramienta servirá como punto central para detectar oportunidades de negocio y mejorar procesos en todos los niveles, desde las tiendas locales hasta los directivos a nivel global."""           
                        
            a ="➡️ Analizar las reseñas de Walgreens en Google y Yelp, y obtener una visión general de los sentimientos expresados en ellas."
            b = "➡️ Ver estadísticas sobre las reseñas, como la distribución de los sentimientos y las palabras más comunes."
            c = "➡️ Explorar las reseñas en detalle, con la capacidad de filtrar por sentimiento y buscar palabras clave."
            d = "➡️ Dashboard de control que permite una visualización que facilita el monitoreo del negocio basados en las plataformas Google y Yelp."
                        
            st.markdown(f'<h3 style="text-align: left;">{intro}</h3>', unsafe_allow_html=True)
            st.markdown(f'<h3 style="text-align: left; font-size: 23px;">{a}</h3>', unsafe_allow_html=True)
            st.markdown(f'<h3 style="text-align: left; font-size: 23px;">{b}</h3>', unsafe_allow_html=True)
            st.markdown(f'<h3 style="text-align: left; font-size: 23px;">{c}</h3>', unsafe_allow_html=True)
            st.markdown(f'<h3 style="text-align: left; font-size: 23px;">{d}</h3>', unsafe_allow_html=True)
            st.divider()
            ## Nuestra información
            st.header("Desarrollado por ⚙️ ", divider='rainbow')

            personas = [
                {
                    "nombre": "Florencia Lascurain",
                    "profesion": "Project Manager & Data Scientist ",
                    "github": "https://github.com/FlorLascu",
                    "linkedin": "https://www.linkedin.com/in/florencia-lascurain-1a890938/",
                    "imagen_link":"images/Flor.png"
                },
                {
                    "nombre": "Facundo Denis",
                    "profesion": "Machine Learning Engineer",
                    "github": "https://github.com/Facundo022",
                    "linkedin": "https://www.linkedin.com/in/facundo-nicolas-denis-60933b199/",
                    "imagen_link":"images/Facu.png"
                    
                },
                {
                    "nombre": "Cristhian Huanqui",
                    "profesion": "Machine Learning Engineer",
                    "github": "https://github.com/Kipros21",
                    "linkedin": "https://www.linkedin.com/in/cristhian-huanqui-tapia-35a653185/",
                    "imagen_link":"images/Cris.png"
                },
                {
                    "nombre": "Gabriel Rojas",
                    "profesion": "Data Analyst",
                    "github": "https://github.com/ga-romu",
                    "linkedin": "https://www.linkedin.com/in/g-a-ro-mu/",
                    "imagen_link":"images/Gabi.png"
                },
                                {
                    "nombre": "	Iván Parra",
                    "profesion": "Data Engineer",
                    "github": "https://github.com/Ivan2125",
                    "linkedin": "https://www.linkedin.com/in/ivan-parra-2501/",
                    "imagen_link":"images/Ivan.png"
                }
            ]

            def get_image_b64(path):
                with open(path, "rb") as img_file:
                    return base64.b64encode(img_file.read()).decode('utf-8')
            
            column1, column2, column3, column4,column5 = st.columns(5)
            
            for idx, persona in enumerate(personas):
                with eval(f"column{idx + 1}"):
                    st.markdown(f'<h2 style="text-align: center;">{persona["nombre"]}</h2>', unsafe_allow_html=True)
                    
                    # Convert the image to base64 and display it
                    persona_image = get_image_b64(persona["imagen_link"])
                    st.markdown(f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{persona_image}" width="200"/></div>', unsafe_allow_html=True)
                    
                    st.markdown(f'<h3 style="text-align: center;">{persona["profesion"]}</h3>', unsafe_allow_html=True)
            
                    linkedin_logo = get_image_b64("images/LI-In-Bug.png")  # Convert local LinkedIn logo to base64
                    github_logo = get_image_b64("images/github-mark-white.png")  # Convert local GitHub logo to base64
            
                    # Display the logos in a div
                    st.markdown(
                        f'<div style="display: flex; justify-content: center;"><a href="{persona["linkedin"]}"><img src="data:image/png;base64,{linkedin_logo}" alt="LinkedIn" width="50"/></a><a href="{persona["github"]}"><img src="data:image/png;base64,{github_logo}" alt="GitHub" width="40"/></a></div>', 
                        unsafe_allow_html=True
                    )

elif tabs=="Dashboard":

        st.header("Dashboard \U0001F4CA", divider='rainbow',anchor=False)
        
        intro = """
        Hola,"""           
                    
        a ="➡️ Analizar las reseñas de Walgreens en Google y Yelp, y obtener una visión general de los sentimientos expresados en ellas."
                    
        st.markdown(f'<h3 style="text-align: left;">{intro}</h3>', unsafe_allow_html=True)
        st.markdown(f'<h3 style="text-align: left; font-size: 23px;">{a}</h3>', unsafe_allow_html=True)
        
        embed_code = """
        <div style='display: flex; justify-content: center; width: 100%; margin: auto'>
            <div class='tableauPlaceholder' id='viz1713209577914' style='position: relative; margin: auto'>
                <noscript>
                    <a href='#'><img alt='Principales competidores ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wa&#47;Walgreens-reviewsanalysisonGoogleYelp&#47;Tablero1&#47;1_rss.png' style='border: none' /></a>
                </noscript>
                <object class='tableauViz'  style='display:none;'>
                    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
                    <param name='embed_code_version' value='3' /> 
                    <param name='site_root' value='' />
                    <param name='name' value='Walgreens-reviewsanalysisonGoogleYelp&#47;Tablero1' />
                    <param name='tabs' value='no' />
                    <param name='toolbar' value='yes' />
                    <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wa&#47;Walgreens-reviewsanalysisonGoogleYelp&#47;Tablero1&#47;1.png' /> 
                    <param name='animate_transition' value='yes' />
                    <param name='display_static_image' value='yes' />
                    <param name='display_spinner' value='yes' />
                    <param name='display_overlay' value='yes' />
                    <param name='display_count' value='yes' />
                    <param name='language' value='es-ES' />
                </object>
            </div>
        </div>
        <script type='text/javascript'>
            var divElement = document.getElementById('viz1713209577914');
            var vizElement = divElement.getElementsByTagName('object')[0];
            if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='977px';}                     
            var scriptElement = document.createElement('script');
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
            vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
        """
        components.html(embed_code, height=2000, width=1709,)

elif tabs=="Modelos":
    
    st.header("Modelos de Machine Learning 🤖", divider='rainbow')
    st.title("Recomendación de tiendas Walgreens 🏪")

    with st.expander(_("¿Cómo usar?")):
        st.markdown(_(
        """
        Este apartado te permite encontrar la ubicación de las mejores tiendas de Walgreens basados en su ubicación y reseñas positivas.

        Ejemplo de uso:
        - Ingresa el nombre de la ciudad, ejemplo: "Los Angeles".
        - Da click en el botón "Enviar".
        - Visualiza las ubicaciones de las mejores tiendas de Walgreens.
        """
        ))
    def obtener_coordenadas(ciudad):
        try:
                    # Lee la clave de API desde el archivo config.json
            with open('secrets/creds-cris.json') as f:
                config = json.load(f)
            api_key = config["GOOGLE_API_KEY"]
            url = f"https://maps.googleapis.com/maps/api/geocode/json?address={ciudad}&key={api_key}"
            response = requests.get(url)
            data = response.json()

            if data['status'] == 'OK':
                latitud = data['results'][0]['geometry']['location']['lat']
                longitud = data['results'][0]['geometry']['location']['lng']
                return latitud, longitud
            elif data['status'] == 'ZERO_RESULTS':
                raise ValueError(f"No se encontraron resultados para la ciudad {ciudad}.")
            else:
                raise ValueError(f"No se pudieron obtener las coordenadas para la ciudad {ciudad}.")
        except requests.exceptions.RequestException as e:
            raise ValueError("Error al conectar con la API de Google Maps.")
        except KeyError as e:
            raise ValueError("Respuesta inesperada de la API de Google Maps.")

    def mostrar_mapa(ciudad, tiendas):
        latitudes = [tienda['latitude'] for tienda in tiendas]
        longitudes = [tienda['longitude'] for tienda in tiendas]
        centro_latitud = mean(latitudes)
        centro_longitud = mean(longitudes)


        folium_map = folium.Map(location=[np.mean(centro_latitud), np.mean(centro_longitud)], zoom_start=14)

        for tienda in tiendas:
            popup_text = f"Rating: {tienda['rating']}<br>Review: {tienda['review']}"
            folium.Marker(
                location=[tienda['latitude'], tienda['longitude']],
                popup=folium.Popup(popup_text, max_width=300),  # Aquí ajustamos el tamaño máximo del popup
            ).add_to(folium_map)

        folium_static(folium_map)

    def app():

            with st.form(key='my_form'):
                ciudad = st.text_input("Ingrese el nombre de la ciudad:")
                submit_button = st.form_submit_button(label='Enviar')

            if submit_button:
                st.write(f'Ciudad ingresada: {ciudad}')
            if ciudad:
                try:
                    ruta_unificado_reviews = 'data/unificado_reviews.parquet'
                    unificado_reviews = pd.read_parquet(ruta_unificado_reviews)

                    latitud, longitud = obtener_coordenadas(ciudad)

                    df_ciudad = unificado_reviews[unificado_reviews['city'] == ciudad]
                    df_walgreens = df_ciudad[(df_ciudad['business_name'] == 'Walgreens') & 
                                             (df_ciudad['rating'] >= 3) & 
                                             (df_ciudad['rating'] <= 5)]
                    if df_walgreens.empty:
                        raise ValueError(f"No se encontraron tiendas Walgreens con rating entre 3 y 5 en la ciudad {ciudad}.")
                    df_walgreens = df_walgreens.sort_values(by='rating', ascending=False)
                    df_walgreens = df_walgreens.drop_duplicates(subset='gmap_id')
                    X = df_walgreens[['latitude', 'longitude']]
                    knn_model = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
                    knn_model.fit(X)

                    # Cuando hagas la predicción, asegúrate de que los datos tengan los mismos nombres de características
                    latitud_referencia, longitud_referencia = obtener_coordenadas(ciudad)
                    distancias, indices = knn_model.kneighbors(pd.DataFrame([[latitud_referencia, longitud_referencia]], columns=['latitude', 'longitude']))

                    tiendas_recomendadas = df_walgreens.iloc[indices[0]]
                    tiendas_dict = []
                    for _, tienda in tiendas_recomendadas.iterrows():
                        tienda_info = {
                            'gmap_id': tienda['gmap_id'],
                            'longitude': tienda['longitude'],
                            'latitude': tienda['latitude'],
                            'rating': tienda['rating'],
                            'review': tienda['text']
                        }
                        tiendas_dict.append(tienda_info)

                    mostrar_mapa(ciudad, tiendas_dict)
                except Exception as e:
                    st.error(f"Error: {e}")






    if __name__ == "__main__":
        app()


    def recomendar_locacion(state_name,county):

        # Leerlos desde local
        path = 'data/recommend.parquet'
        df_recommend = pd.read_parquet(path)

        # For that State, select the available county
        selected_state = state_name
        selected_county = county

        # Filter the DataFrame for the selected state and county
        county_filtered_df = df_recommend[(df_recommend['state_name'] == selected_state) & (df_recommend['county'] == selected_county)]

        # Sort the DataFrame by 'ratio_stores' column in ascending order
        sorted_county_filtered_df = county_filtered_df.sort_values(by='ratio_stores', ascending=True)

        # Calculate the total number of stores
        sorted_county_filtered_df['Total_Number_Stores'] = sorted_county_filtered_df['total_others_stores'] + sorted_county_filtered_df['total_walgreens_stores']

        # Calculate Walgreens presence
        sorted_county_filtered_df['Walgreens_Presence_%'] = round((sorted_county_filtered_df['total_walgreens_stores'] / sorted_county_filtered_df['Total_Number_Stores']) * 100, 2)

        sorted_county_filtered_df_display = sorted_county_filtered_df.drop(['city_state_county', 'county', 'state', 'state_name','others_total_reviews', 'others_average_rating', 'total_others_stores',
            'walgreens_average_rating','walgreens_total_reviews', 'population', 'density', 'ratio_stores'],axis=1) 
        sorted_county_filtered_df_display.rename(columns={'total_walgreens_stores': 'Total_Walgreens_Stores'},inplace=True)

        new_order = [ 'city','Total_Number_Stores','Total_Walgreens_Stores','Walgreens_Presence_%']
        sorted_county_filtered_df_display = sorted_county_filtered_df_display[new_order]

        # Display the DataFrame with the new columns
        return sorted_county_filtered_df_display.head(5)
    
    st.divider()
    
    st.title("Recomendación de nuevas tiendas 📍")
    with st.expander(_("¿Cómo usar?")):
        st.markdown(_(
        """
        Este apartado te permite seleccionar la ciudad y el condado para la obtención de la presencia de Walgreens en dichos lugares.

        Ejemplo de uso:
        - Despliega el **Estado** y selecciona "Texas".
        - Ahora despliega el **Condado** y selecciona "Parker".
        - Visualiza las ciudades con total de tiendas y presencia de Walgreens.
        """
        ))
    
    def app2():
        # Leer los datos
           path = 'data/recommend.parquet'
           df_recommend = pd.read_parquet(path)
           # Crear un selector para los estados
           states = df_recommend['state_name'].unique()
           selected_state = st.selectbox("Seleccione un estado:", states)
           # Filtrar los condados para el estado seleccionado
           counties = df_recommend[df_recommend['state_name'] == selected_state]['county'].unique()
           # Crear un selector para los condados
           selected_county = st.selectbox("Seleccione un condado:", counties)
           # Llamar a la función con los valores seleccionados
           result = recomendar_locacion(selected_state, selected_county)
        # Mostrar el resultado
           st.write(result)
           

    if __name__ == "__main__":
        app2()





    # Elimina palabras irrelevantes y aplica stemming
    stopwords = set(nltk.corpus.stopwords.words('english'))
    stemmer = nltk.stem.WordNetLemmatizer()

    def preprocess(text):
        tokens = nltk.word_tokenize(text.lower())
        filtered_tokens = [t for t in tokens if t not in stopwords and t.isalpha()]
        stemmed_tokens = [stemmer.lemmatize(t) for t in filtered_tokens]
        return stemmed_tokens

    @st.cache_data()
    def review_analysis(business_name, sentiment_value):
        # Lee el conjunto de datos
        df_review = pd.read_parquet('data/reviews_unified.parquet.gz')
        df_business = pd.read_parquet('data/sitios_google.parquet.gz')

        # Fusiona los conjuntos de datos basado en gmap_id
        merged_df = df_review.merge(df_business[['gmap_id', 'business_name']], on='gmap_id', how='left')

        # Filtrado de columnas
        merged_df = merged_df[['gmap_id', 'business_name', 'rating', 'text']]  

        # Reemplazar los valores nulos por "SD" en el DataFrame df_review
        merged_df['text'] = merged_df['text'].replace('None', 'SD')

        # Asigna los valores a la nueva columna sentiment_analysis
        merged_df['sentiment_analysis'] = merged_df['rating'].apply(lambda x: 1 if x >= 4 else 0 if x == 3 else -1)

        # Filtra la data por el valor del negocio y la polaridad de la reseña
        df_filtrado_polaridad = merged_df[(merged_df['business_name'] == business_name) & (merged_df['sentiment_analysis'] == sentiment_value)]

        # Aplica la función de preprocesamiento a tus datos
        processed_reviews = [preprocess(review) for review in df_filtrado_polaridad['text']]

        # Crea un diccionario y una matriz de términos-frecuencia
        dictionary = corpora.Dictionary(processed_reviews)
        corpus = [dictionary.doc2bow(review) for review in processed_reviews]

        # Aplica LDA a tus datos
        lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

        # Get the document topics for each review
        doc_topics = [lda_model.get_document_topics(review) for review in corpus]

        # Group the reviews by topic ID
        grouped_docs = {}
        for doc_topic in doc_topics:
            for topic, prob in doc_topic:
                if topic not in grouped_docs:
                    grouped_docs[topic] = []
                grouped_docs[topic].append(prob)

        # Calculate the average probability for each topic
        avg_probs = {topic: sum(probs) / len(probs) for topic, probs in grouped_docs.items()}

        # Sort the topics by average probability
        sorted_topics = sorted(avg_probs.items(), key=lambda x: x[1], reverse=True)

        # Print the top topics
        results = []
        for i, (topic, prob) in enumerate(sorted_topics[:5]):
            results.append(f"Tema {i+1}: Con  {prob:.4f} de probabilidad de suceso")
            words = [f"<span style='background-color: #2E3159; color: #FFFFFF; padding: 0.2em; border-radius: 5px;'>{term[0]}</span>" for term in lda_model.show_topic(topic, topn=5)]
            results.append(" ".join(words))
            results.append("\n")
        return results
    
    st.divider()
    
    st.title("Análisis de reseñas competidores ⚔️")
    with st.expander(_("¿Cómo usar?")):
        st.markdown(_(
        """
        Este apartado te permite seleccionar uno de los competidores directos del Walgreens y ver sus reseñas positivas y negativas.

        Ejemplo de uso:
        - Despliega el **Negocio** y selecciona "7-Eleven".
        - Ahora selecciona el **Sentimiento**: "Positivo" o "Negativo".
        - Visualiza las reseñas con un análisis de sentimiento y probabilidad de ocurrencia.
        """
        ))
        
    def main():
         
        tab1, tab2 = st.columns(2, gap='medium')
        # Crear un selector para el nombre del negocio
        with tab1:
            business_name = st.selectbox(
                "Selecciona un negocio",
                ("Walgreens", "7-Eleven", "Casey's General Store", "Circle K")
            )
        with tab2:
            # Crear un selector para el valor de sentimiento
            sentiment_value = st.radio("Sentimiento", ["Positivo", "Negativo"],
                                           help='Positivo: busca las reseñas positivas\n\nNegativo: busca las reseñas positivas',  key='unique_key')

        # Convertir el valor de sentimiento a un número
            sentiment_value = 1 if sentiment_value == "Positivo" else -1
        with tab1:
            # Crear un botón para ejecutar el análisis de reseñas
            if st.button("Analizar reseñas"):
                results = review_analysis(business_name, sentiment_value)
                for result in results:
                    st.markdown(result, unsafe_allow_html=True)

    if __name__ == "__main__":
        main()
        
        

    def asignar_sentiment_analysis(df_review):
        def asignar_valor(stars):
            if stars >= 4:
                return 1
            elif stars == 3:
                return 0
            else:
                return -1
        df_review['sentiment_analysis'] = df_review['rating'].apply(lambda x: asignar_valor(x))
        return df_review

    def filtro_business_sentiment(df_review, gmap_id, sentiment_value):
        df_filtrado_polaridad = df_review[(df_review['gmap_id'] == gmap_id) & (df_review['sentiment_analysis'] == sentiment_value)]
        return df_filtrado_polaridad

    def model_ML_review(df_modelo_ml):
        stopwords = set(nltk.corpus.stopwords.words('english'))
        stemmer = nltk.stem.WordNetLemmatizer()
        def preprocess(text):
            tokens = nltk.word_tokenize(text.lower())
            filtered_tokens = [t for t in tokens if t not in stopwords and t.isalpha()]
            stemmed_tokens = [stemmer.lemmatize(t) for t in filtered_tokens]
            return stemmed_tokens
        processed_reviews = [preprocess(review) for review in df_modelo_ml['text']]
        dictionary = corpora.Dictionary(processed_reviews)
        corpus = [dictionary.doc2bow(review) for review in processed_reviews]
        lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)
        doc_topics = [lda_model.get_document_topics(review) for review in corpus]
        grouped_docs = {}
        for doc_topic in doc_topics:
            for topic, prob in doc_topic:
                if topic not in grouped_docs:
                    grouped_docs[topic] = []
                grouped_docs[topic].append(prob)
        avg_probs = {}
        for topic, probs in grouped_docs.items():
            avg_probs[topic] = sum(probs) / len(probs)
        sorted_topics = sorted(avg_probs.items(), key=lambda x: x[1], reverse=True)
        results = []
        for i, (topic, prob) in enumerate(sorted_topics[:5]):
            results.append(f"Tema {i+1}: Con  {prob:.4f} de probabilidad de suceso")
            words = [f"<span style='background-color: #2E3159; color: #FFFFFF; padding: 0.2em; border-radius: 5px;'>{term[0]}</span>" for term in lda_model.show_topic(topic, topn=5)]
            results.append(" ".join(words))
            results.append("\n")
        return results

    st.divider()
    st.title("Análisis de reseñas por tienda 📝")
    with st.expander(_("¿Cómo usar?")):
        st.markdown(_(
        """
        Este apartado te permite buscar una tienda de Walgreens y ver sus reseñas positivas y negativas.

        Ejemplo de uso:
        - Ingresa el **gmap_id** de la tienda, ejemplo: "0x80dca8a2029b54bd:0x808bdccd50742c41".
        - Ahora selecciona el **Sentimiento**: "Positivo" o "Negativo".
        - Visualiza las reseñas con un análisis de sentimiento y probabilidad de ocurrencia en la tienda consultada.
        """
        ))
    def review_analysis_store():

        
        tab1, tab2 = st.columns(2, gap='medium')
        # Carga el DataFrame
        df_review = pd.read_parquet("data/merged_data.parquet")

        # Solicita al usuario que ingrese el gmap_id y el valor de sentimiento
        with tab1:
            gmap_id = st.text_input("Ingrese el gmap_id:", key='unique_key1')
            
        with tab2:
            # Crear un selector para el valor de sentimiento
            sentiment_value = st.radio("Sentimiento", ["Positivo", "Negativo"],
                                           help='Positivo: busca las reseñas positivas\n\nNegativo: busca las reseñas positivas', key='unique_key2')

        # Convertir el valor de sentimiento a un número
            sentiment_value = 1 if sentiment_value == "Positivo" else -1

        if gmap_id and sentiment_value is not None:
            # Aplica las funciones al DataFrame
            df_review = asignar_sentiment_analysis(df_review)
            df_review = filtro_business_sentiment(df_review, gmap_id, sentiment_value)
            model_ML_review(df_review)
        
        with tab1:
            # Crear un botón para ejecutar el análisis de reseñas
            if st.button("Analizar reseñas", key='unique_key3'):
                if gmap_id and sentiment_value is not None: 
                    df_review = asignar_sentiment_analysis(df_review)
                    df_review = filtro_business_sentiment(df_review, gmap_id, sentiment_value)
                    results = model_ML_review(df_review)
                for result in results:
                    st.markdown(result, unsafe_allow_html=True)

    # Llama a la función cuando se ejecuta el script
    if __name__ == "__main__":
        review_analysis_store()