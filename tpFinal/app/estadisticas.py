import datetime
import matplotlib.pyplot as plt
from pylab import *
from modelos import Simulacion, Estadisticas
import numpy as np

class EstadisticasPlot:

    def __init__(self, estadisticas = None):
        self.promedios = estadisticas.get('promedios_totales')

    def getPlot(self):
        assert self.promedios

        p = self.promedios

        demoras_empl = p.get('cant_demandas_sin_atender_por_demoras_empl')
        demoras_stock = p.get('cant_demandas_sin_atender_por_falta_stock')
        demandas_insatisfechas = demoras_empl + demoras_stock
        total_demandas = p.get('promedio_total_demandas')
        demandas_satisfechas = total_demandas -demandas_insatisfechas
        
        plt.figure(1, figsize=(20, 10))
        plt.suptitle('Estaditicas Obtenidas', fontsize=16, bbox={'facecolor':'0.8', 'pad':8})
        colors = ['white', 'red', 'lightcoral', 'gold']
        colors2 = ['darksalmon', 'tomato', 'lightcoral', 'gold']

        plt.subplot(1,2,1) 
        ax = plt.axis('equal')
        texto = "Total de demandas: %d \n Insatisfechas %d \n Satisfechas %d"%(total_demandas,demandas_insatisfechas, demandas_satisfechas)
        plt.text( -0.01,0.9, texto)
        labels = 'Demandas Satisfechas', 'Demandas Insatisfechas'
        fracs = [demandas_satisfechas, demandas_insatisfechas]
        explode = (0, 0.1)  
        plt.title('Analisis de Demandas', bbox={'facecolor':'0.8', 'pad':5})
        plt.pie(fracs, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True,startangle=100)
        plt.gca().set_aspect('1')

        plt.subplot(1,2,2)
        ax2 = plt.axis('equal')
        texto2 = "Total de demandas insatisfechas: %d \n Por Empleados %d \n Por Stock %d"%(demandas_insatisfechas, demoras_empl, demoras_stock)
        plt.text( -0.01,0.9, texto2)
        labels2 = 'Demoras Por Empleados', 'Demoras Por Stock'
        fracs2 = [demoras_empl,demoras_stock]
        explode2 = (0, 0.1)  
        plt.title('Demandas Insatisfechas', bbox={'facecolor':'0.8', 'pad':5})
        plt.pie(fracs2, explode=explode2, labels=labels2, colors=colors2, autopct='%1.1f%%', shadow=True,startangle=100)
        plt.gca().set_aspect('1')

        plt.show()

if __name__ == '__main__':
    result = Simulacion(default=True).iniciar()
    estadisticas = Estadisticas().getEstadisticas(result)
    g = EstadisticasPlot(estadisticas).getPlot()
