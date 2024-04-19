ETL(extraccion, transformacion y carga de los datos) Google y Yelp

En esta parte del proyecto se enfocó en realizar una extraccion, transformacion y carga de los datos (ETL) utilizando dos fuentes principales: Google y Yelp. Nuestro objetivo fue extraer la data de ambas bases y poder juntar en un solo lugar todos los datos extraidos, con un filtrado leve por anticipacion.


en los siguientes tableros se puede visualizar los nombres de los archivos, sus fuentes pertinentes y por ultimo un tablero de cada archivo con una explicacion del contenido de cada columna del mismo



Archivos

| Nombres del Archivo               | Fuente de datos                         |
|-----------------------------------|-----------------------------------------|
| business_cs.parquet.gz            | contiene los negocios de Yelp           |
| checkin.parquet.gz                | contiene las entradas y salidas de Yelp |
| geo_cs.csv                        | contiene ubicaciones de ambas fuentes   |
| review_cs.parquet.gz              | contiene las reseñas de la fuente Yelp  |
| review_sites_google_cs.parquet.gz | contiene las reseñas de la fuente Google|
| sites_google_cs.parquet.gz        | contiene los negocios de Google         |
| tip_cs.parquet.gz                 | contiene las propinas de la fuente Yelp |
| user_cs.parquet.gz                | contiene los usuarios de la fuente Yelp |



Archivo: business_cs.parquet.gz

| Columnas                          | Datos                                   |
|-----------------------------------|-----------------------------------------|
| business_id                       | Identificador del negocio               |
| name                              | contiene los name de los negocios       |
| address                           | contiene ubicaciones de ambas fuentes   |
| city                              | contiene la ciudad del negocio          |
| postal_code                       | contiene el codigo postal de la address |
| latitude                          | contiene la latitud de cada negocio     |
| longitude                         | contiene la longitud de cada negocio    |
| stars                             | contiene la calificacion del negocio    |
| review_count                      | contiene la cantidad de reseñas         |
| is_open                           | contiene si esta cerrado o abierto      |
| attributes                        | contiene los atributos de ese local     |
| categories                        | contiene la categoria del negocio       |
| hours                             | contiene los horarios de cada local     |
| state_name                        | contiene el nombre del estado           |
| state_code                        | contiene el nombre de la ciudad         |



Archivo: checkin.parquet.gz

| Columnas                          | Datos                                   |
|-----------------------------------|-----------------------------------------|
| business_id                       | Identificador del negocio               |
| date                              | tiempo de apertura y cierre             |



Archivo: geo_cs.csv

| Columnas                          | Datos                                   |
|-----------------------------------|-----------------------------------------|
| site_id                           | Identificador del negocio de Google/Yelp|
| latitude                          | contiene la latitud de cada negocio     |
| longitude                         | contiene la longitud de cada negocio    |
| state                             | contiene el nombre del estado           |
| city                              | contiene el nombre de la ciudad         |
| county                            | contiene el nombre del condado          |
| is_urban                          | contiene la ubicacion es o no urbana    |



Archivo: review_cs.parquet.gz

| Columnas                          | Datos                                   |
|-----------------------------------|-----------------------------------------|
| review_id                         | Identificador de la reseña              |
| user_id                           | Identificador de cada usuario           |
| business_id                       | Identificador del negocio de Yelp       |
| stars                             | contiene las estrellas de la reseña     |
| useful                            | contiene si la reseña es util           |
| funny                             | contiene si la reseña es graciosa       |
| cool                              | contiene si la reseña es interesante    |
| text                              | contiene lel texto de la reseña         |
| date                              | contiene la fecha de la reseña          |



Archivo: review_sites_google_cs.parquet.gz

| Columnas                          | Datos                                   |
|-----------------------------------|-----------------------------------------|
| name                              | nombre del negocio                      |
| gmap_id                           | Identificador de cada negocio           |
| latitude                          | contiene la latitud de cada negocio     |
| longitude                         | contiene la longitud de cada negocio    |
| category                          | contiene la categoria del negocio       |
| avg_rating                        | contiene el promedio de estrellas       |
| num_of_reviews                    | contiene el numero de reseñas           |
| state                             | contiene si esta abierto o cerrado      |
| city                              | contiene el ciudad del negocio          |
| state_us                          | contiene la abreviación del estado      |
| horario                           | contiene los horarios del local         |
| user_id                           | Identificador del usuario               |
| time                              | contiene la fecha de la reseña          |
| rating                            | contiene la calificacion de la reseña   |
| text                              | contiene el texto de la reseña          |
| resp                              | contiene si el negocio respondio        |
| business_name                     | contiene el nombre del negocio          |
| State_review                      | contiene el estado de la reseña         |



Archivo: sites_google_cs.parquet.gz

| Columnas                          | Datos                                   |
|-----------------------------------|-----------------------------------------|
| name                              | nombre del negocio                      |
| gmap_id                           | Identificador de cada negocio           |
| latitude                          | contiene la latitud de cada negocio     |
| longitude                         | contiene la longitud de cada negocio    |
| category                          | contiene la categoria del negocio       |
| avg_rating                        | contiene el promedio de estrellas       |
| num_of_reviews                    | contiene el numero de reseñas           |
| state                             | contiene si esta abierto o cerrado      |
| city                              | contiene el ciudad del negocio          |
| state_us                          | contiene la abreviación del estado      |
| horario                           | contiene los horarios del local         |



Archivo: tip_cs.parquet.gz

| Columnas                          | Datos                                   |
|-----------------------------------|-----------------------------------------|
| business_id                       | Identificador de cada negocio           |
| user_id                           | Identificador de cada usuario           |
| text                              | contiene el texto de cada reseña        |
| date                              | contiene la fecha de cada reseña        |
| compliment_count                  | contiene cuantas veces gusto la reseña  |




Archivo: user_cs.parquet.gz

| Columnas                          | Datos                                                      |
|-----------------------------------|------------------------------------------------------------|
| user_id                           | Identificador de cada usuario                              |
| name                              | nombre del negocio                                         |
| review_count                      | contiene el numero de reseñas                              |
| yelping_since                     | contiene la fecha de cada reseña                           |
| useful                            | contiene si la reseña es util                              |
| funny                             | contiene si la reseña es graciosa                          |
| cool                              | contiene si la reseña es interesante                       |
| elite                             | contiene los años que el usuario fue elite                 |
| friends                           | contiene los id de usuarios que son amigos de ese usuario  |
| fans                              | contiene la cantidad de fans                               |
| average_stars                     | contiene el promedio de estrellas                          |
| compliment_hot                    | total de cumplidos 'hot' recibidos por el usuario          |
| compliment_more                   | total de cumplidos varios recibidos por el usuario         |
| compliment_profile                | total de cumplidos por el perfil recibidos por el usuario  |
| compliment_cute                   | total de cumplidos 'cute' recibidos por el usuario         |
| compliment_list                   | total de  listas de cumplidos recibidos por el usuario     |
| compliment_note                   | total de cumplidos como notas recibidos por el usuario     |
| compliment_plain                  | total de cumplidos planos recibidos por el usuario         |
| compliment_cool                   | total de cumplidos 'cool' recibidos por el usuario         |
| compliment_funny                  | total de cumplidos 'funny' recibidos por el usuario        |
| compliment_writer                 | numero de cumplidos escritos recibidos por el usuario      |
| compliment_photos                 | número de cumplidos en foto recibidos por el usuario       |















