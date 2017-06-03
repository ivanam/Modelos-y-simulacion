


### TP6 MyS Simulacion de Inventarios ###


  - [Consigna](#consigna)
  - [Requerimientos](#requerimientos)
  - [Instalacion](#instalacion)
  - [Iniciar la Aplicacion](#iniciar-la-aplicacion)
  

## Consigna ##
Manufactura Mantel provee varios tipos de auto-partes a las más importantes empresas automotrices y que trabajan con el sistema de producción JIT (just-in-
time). La compañía ha firmado un nuevo contrato para producir bombas de agua. La capacidad de producción planeada para bombas de agua es de 100 unidades por turno. Debido a las fluctuaciones en la línea de ensamble de los clientes, la demanda histórica diaria presenta una distribución Normal de media 110 unidades con un desvió estándar de 20 unidades. Para mantener un inventario suficiente que cumpla con los requerimientos JIT de los clientes el gerente de Mantel está considerando una nueva política, la de producir durante un segundo turno si el inventario cae a 50 o menos unidades (60 y 70) El costo de mantener el stock es de 20$ por unidad por día. Para la planificación anual del presupuesto los gerentes de proceso necesitan saber cuántos turnos adicionales serán necesarios en promedio en un año para 50, 60 y 70 o menos unidades inventario. Como también tener el presupuesto promedio anual del mantenimiento de stock.


Simular 30 anios con 250 dias habiles cada uno, calcule:
  - Cuántos turnos adicionales serán necesarios en promedio en un año para 50, 60 y 70 o menos unidades inventario.
  - Calcule promedios como estimador puntual e I.C (99%). Grafique histogramas representativos. (Reporte).
  - Realice un gráfico (box plot o cajas y bigotes) para comparar el presupuesto anual de inventario para los 3 valores definidos para incluir turno adicional. Analizar la posibilidad de realizar un análisis de la variancia (ANOVA) para concluir si existe diferencia significativa para los tres niveles de 50, 60 o 70 unidades de inventario límites para incluir un segundo turno.


## Requerimientos ##
  - numpy
  - scipy
  - matplotlib
  - jupyter
  
## Instalacion ##
    $sudo pip install -r requirements.txt

## Iniciar la aplicacion ##
    $jupyter notebook tp6.ipynb 


