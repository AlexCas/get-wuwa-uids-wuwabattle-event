# Setup
Para ejecutar el script simplemente en una terminar con python ejecutar py get-uuids.py

# Justificacion
Wuthering Waves realizo un [concurso](https://x.com/Wuthering_Waves/status/1799026649679433798) donde publicas un video y agregas tu id de jugador. Supuestamente regalarian 2k de la moneda premium al hacerlo. Lo que me hizo preguntarme como harian para poder regalar eso?

Evidentemente no pondran a un sujeto a registrar id por id en cada video. Tomando en cuenta que la entrada es por YT Shorts, X y Tiktok es demasiada informacion. Asi que asumi que usarian algun metodo/bot para obtener los ids.

Me di a la tarea de hacer un script para tiktok unicamente y ver si me era posible obtener los UID de los jugadores.

# Resultados

Me apoye de la [API no Oficial de Tiktok](https://github.com/davidteather/TikTok-Api) sin embargo, para el caso de uso que requeria contaba con ciertas limitaciones al momento de traer los videos relacionados al hashtag asi que me di a la tarea de modificar las funciones del modulo. Dichas modificaciones se encuentran en la raiz de este proyecto.

Al realizar dichas modificaciones logre obtener la informacion cruda del video de tiktok y con expresiones regulares obtener el uid del jugador que lo habia posteado.

TODO

-Guardar la coleccion de uids en un archivo json/csv