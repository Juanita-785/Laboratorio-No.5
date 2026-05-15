# Laboratorio-No.5
## Juanita Gómez y Shara Cetina

## Descripción
<p align="justify">
Este proyecto contiene el código y la información necesarios para comprender la variabilidad de la frecuencia cardíaca (HRV) e identificar cambios en el balance autonómico. Además, incluye el análisis de señales ECG mediante técnicas como el HRV en el dominio del tiempo (media y SDNN) y el diagrama de Poincaré, así como la implementación de filtros IIR a partir de la obtención de su ecuación en diferencias.

## Propósito
<p align="justify">


## Metodología 
<p align="justify">
La metodología de esta práctica se estructuró en tres fases principales: adquisición de datos, pre-procesamiento de la señal y análisis de la variabilidad de la frecuencia cardíaca (HRV).
  
<p align="justify">  
En la fase de adquisición, se registró la señal electrocardiográfica (ECG) de un sujeto durante un periodo total de 4 minutos. Para cumplir con el requerimiento de emplear una tasa apropiada para este tipo de señal, se estableció una frecuencia de muestreo de 800 Hz, lo que permitió capturar con precisión los picos R y asegurar una resolución temporal adecuada para el análisis posterior. El protocolo se dividió en dos condiciones experimentales: los primeros 2 minutos en reposo absoluto (inmovilidad y silencio) y los 2 minutos restantes en una tarea de lectura en voz alta.
  
<p align="justify">
Durante el pre-procesamiento, la señal fue tratada en el entorno Spyder (Python) mediante un filtro IIR diseñado específicamente para eliminar el ruido e interferencias. Se obtuvo la ecuación en diferencias del filtro y se aplicó a la señal grabada asumiendo condiciones iniciales en cero. Tras el filtrado, se procedió a la detección de los picos R en cada segmento para calcular los intervalos R-R, generando así una nueva serie temporal para cada una de las dos condiciones de 2 minutos.

<p align="justify">
Finalmente, se realizó el análisis de la HRV comparando los parámetros básicos en el dominio del tiempo, tales como la media de los intervalos R-R y la desviación estándar (SDNN). Complementariamente, se aplicó el método no lineal del diagrama de Poincaré (o gráfico de Lorenz), analizando la dispersión de la nube de puntos en cada caso. A partir de este diagrama, se calcularon el Índice Vagal Cardíaco (CVI) y el Índice Simpático Cardíaco (CSI), permitiendo evaluar de forma independiente y cuantitativa los cambios en el balance autonómico del sujeto generados por la realizacíón de la lectura en voz alta.
  
## Definiciones
<p align="justify">

  
<p align="justify">
  
### 3. Variabilidad de la frecuencia cardíaca (HRV) obtenida a partir de la señal electrocardiográfica (ECG)
La Variabilidad de la Frecuencia Cardíaca (HRV) se define como la variación en el tiempo (medida en milisegundos) que transcurre entre latidos cardíacos consecutivos, conocidos como intervalos R-R. En un individuo sano, el ritmo cardíaco no es perfectamente regular; por el contrario, el tiempo entre dos latidos varía latido a latido debido a la influencia constante de mecanismos reguladores.

<p align="justify">
Desde una perspectiva técnica, la HRV se obtiene a partir de la señal de electrocardiografía (ECG) mediante la identificación de cada una de las ondas R para calcular el tiempo exacto entre picos R adyacentes. Esta serie de intervalos R-R resultantes conforma lo que se denomina el tacograma, que es la base para todos los análisis posteriores en los dominios del tiempo, la frecuencia y los métodos no lineales.

<p align="justify">
Fisiológicamente, la HRV es un indicador fundamental de la función autonómica cardíaca, ya que refleja la interacción dinámica y el equilibrio entre las ramas simpática y parasimpática (vagal) del sistema nervioso autónomo sobre el nodo sinusal. Mientras que el sistema simpático tiende a reducir esta variabilidad en situaciones de estrés o actividad, el predominio del sistema parasimpático en reposo aumenta la variabilidad, lo que generalmente se asocia con un mejor estado de salud y un factor protector para el corazón.
  
### 4. Diagrama de Poincaré como herramienta de análisis de la serie R-R. 

### Diagramas de flujo



## Resultados


## Conclusión
