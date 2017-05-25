


### Django + Postgres + nginx + celery en contenedores Docker ###


  - [Consigna](#consigna)
  - [Requerimientos](#requerimientos)
  - [Instalacion](#instalacion)
  - [Iniciar la Aplicacion](#iniciar-la-aplicacion)
  

## Consigna ##

Suponga que tres amigos quieren cocinar tocino, huevos y tostadas para el desayuno de algunos visitantes del fin de semana. Ellos dividen el trabajo, con la preparación de un artículo por amigo. 
Se presenta la secuencia de las actividades con duracion en minutos representada por una distribucion uniforme, y sus tareas predecesoras.

Simular 30 expermitos de 100 corridas cada una y calcule:
  - El tiempo promedio de finalización del proyecto y el IC. Con el 99%deprobabilidad (2,57).
  - La probabilidad de criticidad de cada actividad.
  - Grafique un histograma con la distribución del tiempo de realización del proyecto con los datos de las 3000 corridas. Y otro teniendo en cuenta los promedios de los 30 experimentos.
  - Analice los resultados

## Requerimientos ##
  - numpy
  - scipy
  - matplotlib
  - jupyter
  - criticalpath

## Instalacion ##
    $sudo pip install -r requirements.txt

## Iniciar la aplicacion ##
    $jupyter notebook tp5.ipynb 


