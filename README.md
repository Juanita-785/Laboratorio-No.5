# Laboratorio-No.5  " Variabilidad de la frecuencia cardíaca (HRV) y balance autonómico "
## Juanita Gómez y Shara Cetina

## Descripción
<p align="justify">
Este proyecto contiene el código y la información necesarios para comprender la variabilidad de la frecuencia cardíaca (HRV) e identificar cambios en el balance autonómico. Además, incluye el análisis de señales ECG mediante técnicas como el HRV en el dominio del tiempo (media y SDNN) y el diagrama de Poincaré, así como la implementación de filtros IIR a partir de la obtención de su ecuación en diferencias.

## Propósito
<p align="justify">
El propósito de este laboratorio es que el estudiante aplique técnicas de análisis de la variabilidad cardíaca y comprenda la importancia del cálculo de parámetros en el dominio del tiempo dentro del procesamiento de señales, específicamente en señales electrocardiográficas (ECG). Se busca que el estudiante entienda el análisis de la variabilidad cardíaca como una herramienta que permite evaluar la actividad del sistema nervioso autónomo, en particular las respuestas simpática y parasimpática asociadas a actividades que implican verbalización.

Asimismo, mediante el cálculo de parámetros como la media y la desviación estándar, junto con el análisis de señales biológicas, se pretende que el estudiante evalúe el impacto de estos procedimientos en la identificación de cambios en la actividad simpática y parasimpática presentes en señales ECG, y reconozca su relevancia en aplicaciones propias de la ingeniería biomédica. Además, se busca que el estudiante relacione estos parámetros con características fisiológicas y con la calidad de la señal, permitiendo interpretar diferencias entre actividades que implican verbalización y aquellas que no.

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
### 1. Actividad simpática y parasimpática del sistema nervioso autónomo
<p align="justify">
El sistema nervioso autónomo es el encargado de regular las funciones involuntarias del organismo y mantener la homeostasis cardiovascular mediante la interacción entre el sistema nervioso simpático y el parasimpático. El control de la actividad cardíaca se logra a través del equilibrio entre estas dos divisiones principales.

<p align="justify">
El sistema nervioso simpático actúa como un mecanismo de respuesta ante situaciones de estrés o emergencia y se asocia con la respuesta de “lucha o huida”. Las terminaciones simpáticas liberan noradrenalina, mientras que la médula suprarrenal secreta adrenalina al torrente sanguíneo. Estas sustancias interactúan principalmente con los receptores adrenérgicos del corazón, produciendo un aumento de la frecuencia cardíaca (cronotropismo positivo) y de la fuerza de contracción (inotropismo positivo).

<p align="justify">
Por otra parte, el sistema nervioso parasimpático está relacionado con la conservación de energía, el descanso y la recuperación posterior a situaciones de estrés. Su principal neurotransmisor es la acetilcolina (ACh). En el corazón, la ACh se une a receptores colinérgicos muscarínicos ubicados en las células marcapasos, generando una disminución de la frecuencia cardíaca (cronotropismo negativo).
  
### 2. Efecto de la actividad simpática y parasimpática en la frecuencia cardíaca
<p align="justify">
La activación simpática aumenta la frecuencia cardíaca debido a que acelera la despolarización diastólica espontánea en el nodo sinusal. Esto ocurre por el incremento en la entrada de calcio y otras corrientes iónicas en las células del nodo sinusal, permitiendo que el corazón alcance el umbral de disparo más rápidamente.

<p align="justify">
Por otra parte, la estimulación vagal (parasimpática) disminuye la frecuencia cardíaca. Cuando se activan los receptores colinérgicos, se produce la apertura de canales de potasio, generando una hiperpolarización de las células marcapasos y dificultando su despolarización. Como consecuencia, disminuye la descarga del nodo sinusal y se enlentece la conducción entre aurículas y ventrículos.

<p align="justify">
En un corazón sano y en estado de reposo, predomina el tono parasimpático sobre el simpático. Sin esta influencia vagal, la frecuencia intrínseca de disparo del nodo sinusal sería considerablemente mayor, aproximadamente entre 100 y 120 latidos por minuto.
  
### 3. Variabilidad de la frecuencia cardíaca (HRV) obtenida a partir de la señal electrocardiográfica (ECG)
La Variabilidad de la Frecuencia Cardíaca (HRV) se define como la variación en el tiempo (medida en milisegundos) que transcurre entre latidos cardíacos consecutivos, conocidos como intervalos R-R. En un individuo sano, el ritmo cardíaco no es perfectamente regular; por el contrario, el tiempo entre dos latidos varía latido a latido debido a la influencia constante de mecanismos reguladores.

<p align="justify">
Desde una perspectiva técnica, la HRV se obtiene a partir de la señal de electrocardiografía (ECG) mediante la identificación de cada una de las ondas R para calcular el tiempo exacto entre picos R adyacentes. Esta serie de intervalos R-R resultantes conforma lo que se denomina el tacograma, que es la base para todos los análisis posteriores en los dominios del tiempo, la frecuencia y los métodos no lineales.

<p align="justify">
Fisiológicamente, la HRV es un indicador fundamental de la función autonómica cardíaca, ya que refleja la interacción dinámica y el equilibrio entre las ramas simpática y parasimpática (vagal) del sistema nervioso autónomo sobre el nodo sinusal. Mientras que el sistema simpático tiende a reducir esta variabilidad en situaciones de estrés o actividad, el predominio del sistema parasimpático en reposo aumenta la variabilidad, lo que generalmente se asocia con un mejor estado de salud y un factor protector para el corazón.
  
### 4. Diagrama de Poincaré como herramienta de análisis de la serie R-R.

El diagrama de Poincaré es una técnica de análisis no lineal y de visualización estándar utilizada para evaluar la dinámica de la variabilidad de la frecuencia cardíaca (HRV). Se define matemáticamente como un mapa de retorno o gráfico de dispersión bidimensional, en el cual cada intervalo R-R de la serie temporal ($RR_ n$) se grafica en el eje horizontal frente al intervalo inmediatamente subsiguiente ($RR_ n+1$) en el eje vertical.

<p align="justify">

Esta herramienta permite transformar la serie de tiempo del tacograma en una configuración geométrica (habitualmente una elipse en sujetos sanos), facilitando la detección de patrones, oscilaciones e irregularidades que no son evidentes mediante métodos lineales tradicionales. La interpretación del diagrama se basa en la cuantificación de su geometría a través de dos ejes principales:

### 1. Eje Transversal ($T$ o $SD1$): 
<p align="justify">
Es perpendicular a la línea de identidad ($RR_ n=RR_n+1$). Representa la desviación estándar del cambio instantáneo o la variabilidad latido a latido, lo cual es un indicador directo de la actividad parasimpática (vagal).

<p align="justify">
  
### 2.Eje Longitudinal ($L$ o $SD2$): 
<p align="justify">
Se ubica a lo largo de la línea de identidad. Representa la variabilidad a largo plazo y la amplitud total de las fluctuaciones de los intervalos R-R.

En el ámbito clínico y de investigación, la principal ventaja de esta herramienta es su capacidad para derivar índices independientes del balance autonómico, como el Índice Vagal Cardíaco (CVI) y el Índice Simpático Cardíaco (CSI), proporcionando una evaluación fiable incluso con registros cortos de tan solo 100 intervalos R-R. Visualmente, una elipse de mayor área indica un tono vagal elevado, mientras que una figura más alargada y estrecha sugiere un incremento en la actividad simpática.

## Diagramas de flujo

### Parte A

## Plan de Acción
<p align="center">
<img width="1024" height="768" alt="1" src="https://github.com/user-attachments/assets/f3330e97-00db-4fd7-8531-53208424089c" />
<img width="1024" height="768" alt="2" src="https://github.com/user-attachments/assets/171cd6f6-2c0c-43e8-98e6-cc95e87029a4" />
<img width="1023" height="487" alt="7" src="https://github.com/user-attachments/assets/62416fef-1705-477d-9ce1-2cd5d4f3bc90" />

### Parte B

### Parte C
<p align="center">
<img width="1024" height="768" alt="1" src="https://github.com/user-attachments/assets/cec40524-3426-4bfe-8315-300fce7aef69" />
<img width="1024" height="768" alt="2" src="https://github.com/user-attachments/assets/3b18c81f-2ec4-409a-81a4-0c0ddcd73075" />
<img width="1022" height="268" alt="6" src="https://github.com/user-attachments/assets/b63ae1cb-7f7d-44b5-a2a1-fa0cbf8779b5" />

## Resultados

### Tacogramas de cada segmento
<p align="center">
<img width="1600" height="1061" alt="WhatsApp Image 2026-05-14 at 21 27 14" src="https://github.com/user-attachments/assets/bf565196-e8bc-4080-ae50-6558a2f01f26" />

<p align="center">

### Picos R
#### Primer segmento
<p align="center">
<img width="1600" height="536" alt="WhatsApp Image 2026-05-14 at 21 27 15 (2)" src="https://github.com/user-attachments/assets/cd3c6298-e7ed-40dd-9130-08fd679ec026" />

#### Segundo segmento
<p align="center">
<img width="1600" height="536" alt="WhatsApp Image 2026-05-14 at 21 27 15 (3)" src="https://github.com/user-attachments/assets/1807cdd1-2211-48c3-95f1-1f4b77c5bd87" />

### Comparación de parámetros HRV
<p align="center">
<img width="994" height="648" alt="WhatsApp Image 2026-05-14 at 21 27 15 (4)" src="https://github.com/user-attachments/assets/efdbc5ad-09ae-4154-b6bd-e36de45334cc" />


<div align="center">
 
#### Datos a comparar 

| Parámetro                         | Reposo | Lectura/Actividad |
|-----------------------------------|---------|-------------------|
| Media R-R (s)                     | 0.7958  | 0.7134            |
| Desviación Estándar SDNN (s)      | 0.0573  | 0.0530            |
| Varianza (s²)                     | 0.003280| 0.002810          |
| Frecuencia Cardíaca Promedio (BPM)| 75.4    | 84.1              |

</div>

### Diagramas de Poincaré

#### Segmento 1 (Reposo) y Segmento 2 (Lectura / Actividad)
<p align="center">
<img src="https://github.com/user-attachments/assets/afdc99e7-fa18-485a-80aa-752630a321be" width="400"/>
<img src="https://github.com/user-attachments/assets/7048f30f-8737-4c8f-8680-bcd757faba14" width="400"/>
</p>


<div align="center">

#### Datos obtenidos a partir del diagrama de Poincaré

| Parámetro                         | Reposo | Lectura/Actividad |
|-----------------------------------|---------|-------------------|
| SD1 (s)                           | 0.0265  | 0.0227            |
| SD2 (s)                           | 0.0755  | 0.0716            |
| CSI (actividad simpática)         | 2.8503  | 3.1577            |
| CVI (actividad vagal)             | -2.6988 | -2.7896           |

</div>

## Conclusión
<p align="justify">
A partir de los resultados obtenidos en el laboratorio, se concluye que el paso de un estado de reposo absoluto a la actividad cognitiva y verbal (lectura en voz alta) indujo un cambio significativo y cuantificable en el balance autonómico del sujeto, caracterizado por una marcada activación de la rama simpática y un retiro de la modulación vagal. En el dominio del tiempo, esta transición se manifestó con un incremento de la frecuencia cardíaca promedio de 75.4 a 84.1 BPM, acompañado de una reducción en la variabilidad global (SDNN disminuyó de 0.0573 s a 0.0530 s), lo que refleja un ritmo cardíaco más acelerado y regular bajo estrés.

<p align="justify">
El análisis no lineal mediante el diagrama de Poincaré permitió una evaluación más profunda y sensible que los métodos tradicionales: el aumento del Índice Simpático Cardíaco (CSI) de 2.8503 a 3.1577 y la disminución del Índice Vagal Cardíaco (CVI) de -2.6988 a -2.7896 evidencian geométricamente una elipse más alargada y estrecha, producto de la reducción de la variabilidad instantánea latido a latido (SD1). Estos hallazgos validan la eficacia del método de Lorenz como una herramienta clínica robusta, capaz de capturar la compleja dinámica del sistema cardiovascular en registros cortos de solo 2 minutos, proporcionando una visualización inmediata y fiable del estado fisiológico del paciente que supera en estabilidad al análisis espectral.

