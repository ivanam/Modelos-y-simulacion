


### TPFinal MyS Fabrica Automotriz ###


  - [Consigna](#consigna)
  - [Requerimientos](#requerimientos)
  - [Instalacion](#instalacion)
  - [Iniciar la Aplicacion](#iniciar-la-aplicacion)
  

## Consigna ##
En una fábrica automotriz se desea incrementar la producción, para ello se acelerará el armado de los vehículos sustituyendo una de las máquinas que intervienen en el proceso. Se sabe que este incremento vendrá acompañado de una mayor demanda de autopartes para el ensamble de los vehículos, es por ello que se desean determinar los cambios necesarios antes de realizar la sustitución mencionada.
 
Actualmente en la misma fábrica, se manufacturan dos autopartes de gran importancia en el proceso de ensamble definitivo de los automóviles. Estas, se producen a un valor fijo de ​ 110 autopartes/dia para la autoparte 1 y ​ 160 autopartes/dia para la autoparte 2, durante los primeros quince días de cada mes y luego se suspende su producción hasta el mes siguiente. En el periodo de producción, las autopartes se acumulan en un depósito hasta ser requeridas por el sector de ensamble.
Por otra parte, la producción de automóviles es constante y ambas autopartes son extraídas para cada auto, a un valor que sigue una distribución ​ Poisson ​ ​ con​ media μ = 70 por dia.
 
Suele suceder que las autopartes se agotan antes de que transcurran los quince días hasta llegar a fin de mes, pero la producción no se reinicia automáticamente. Como consecuencia, los pedidos se acumulan y cuando se inicia la producción, estos se satisfacen por orden de llegada para luego volver a acumular autopartes para el siguiente mes.
 
Mientras tanto, en el depósito dos operadores atienden los requerimientos de autopartes y su velocidad para procesar cada pedido sigue una distribución ​ Exponencial ​ con media ​ 8 min. para la autoparte 1 y 12 min. para la autoparte 2.

Objetivos de la Simulacion

  - Objetivo de la simulación es analizar la cantidad necesaria de produccion por dia de autopartes, a medida que la variable demanda de autopartes aumenta. Suponemos que la tasa de producción por día de autopartes no puede superar al número indicado, se deberá tener en cuenta cuantos días más al mes se deben emplear para satisfacer la demanda. 
  - Otro objetivo de la simulación es analizar si disminuyendo el tiempo de atención de los operadores por autopartes aumentan la produccion de vehiculos. En principio entendemos que la producción de autopartes no alcanza para satisfacer la demanda, por lo que de nada serviria analizar la productividad de los operadores. Pero luego de encontrar la tasa de producción adecuada, procedemos a analizar si variando los tiempos de atención por autopartes de los empleados aumenta la producción de vehículos por día.


## Requerimientos ##
  - numpy
  - scipy
  - matplotlib
  - pyQt4
  
## Instalacion ##
    $ sudo pip install -r requirements.txt
    $ sudo apt-get install python-qt4 libqt4-designer

## Iniciar la aplicacion con Interfaz Grafica ##
    $ python app.py
    
## Lanzar QtDesigner
    $ designer-qt4


