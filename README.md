# Laboratorio-No.5
## Juanita Gómez y Shara Cetina

## Descripción
<p align="justify">


## Propósito
<p align="justify">


## Metodología 
<p align="justify">
La metodología de esta práctica se estructuró en tres fases principales: adquisición de datos, pre-procesamiento de la señal y análisis de la variabilidad de la frecuencia cardíaca (HRV).
  
<p align="justify">  
En la fase de adquisición, se registró la señal electrocardiográfica (ECG) de un sujeto durante un periodo total de 4 minutos. Para cumplir con el requerimiento de emplear una tasa apropiada para este tipo de señal, se estableció una frecuencia de muestreo de 800 Hz, lo que permitió capturar con precisión los picos R y asegurar una resolución temporal adecuada para el análisis posterior. El protocolo se dividió en dos condiciones experimentales: los primeros 2 minutos en reposo absoluto (inmovilidad y silencio) y los 2 minutos restantes en una tarea de lectura en voz alta.
  
<p align="justify">
Durante el pre-procesamiento, la señal fue tratada en el entorno Spyder (Python) mediante un filtro IIR diseñado específicamente para eliminar el ruido e interferencias. Se obtuvo la ecuación en diferencias del filtro y se aplicó a la señal grabada asumiendo condiciones iniciales en cero. Tras el filtrado, se procedió a la detección de los picos R en cada segmento para calcular los intervalos R-R, generando así una nueva serie temporal (tacograma) para cada una de las dos condiciones de 2 minutos.

<p align="justify">
Finalmente, se realizó el análisis de la HRV comparando los parámetros básicos en el dominio del tiempo, tales como la media de los intervalos R-R y la desviación estándar (SDNN). Complementariamente, se aplicó el método no lineal del diagrama de Poincaré (o gráfico de Lorenz), analizando la dispersión de la nube de puntos en cada caso. A partir de este diagrama, se calcularon el Índice Vagal Cardíaco (CVI) y el Índice Simpático Cardíaco (CSI), permitiendo evaluar de forma independiente y cuantitativa los cambios en el balance autonómico del sujeto inducidos por la verbalización.
  
## Definiciones
<p align="justify">

  
<p align="justify">
### 3. Variabilidad de la frecuencia cardíaca (HRV) obtenida a partir de la señal electrocardiográfica (ECG)

<p align="justify">
### 4. Diagrama de Poincaré como herramienta de análisis de la serie R-R. 

### Diagramas de flujo



## Resultados


## Conclusión
