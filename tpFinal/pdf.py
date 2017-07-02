import os
import datetime
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from modelos import *

class GeneradorPdf:

    def __init__(self, configuracion, estadisticas = None):
        self.promedios = estadisticas.get('promedios_totales')
        self.configuracion = configuracion # add

    def getPdf(self):
        assert self.promedios
        
        fecha = datetime.datetime.now()
        nombrePdf = "./pdf/simulacion_%d%d%d%d%d%d.pdf"%(fecha.year,fecha.month,fecha.day,fecha.hour,fecha.minute,fecha.second)

        with PdfPages(nombrePdf) as pdf:

            p = self.promedios
            labels = 'Demandas Satisfechas', 'Demandas Insatisfechas'

            demoras_empl = p.get('cant_demandas_sin_atender_por_demoras_empl')
            demoras_stock = p.get('cant_demandas_sin_atender_por_falta_stock')
            demandas_insatisfechas = demoras_empl + demoras_stock
            total_demandas = p.get('promedio_total_demandas')
            demandas_satisfechas = total_demandas -demandas_insatisfechas
            
            colors = ['white', 'red', 'lightcoral', 'gold']
            colors2 = ['darksalmon', 'tomato', 'lightcoral', 'gold']

            texto = "Total de Demandas: %d \n Insatisfechas %d \n Satisfechas %d"%(total_demandas,demandas_insatisfechas, demandas_satisfechas)
            sizes = [demandas_satisfechas, demandas_insatisfechas]
            explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.set_title('Analisis de Demandas', bbox={'facecolor':'0.9', 'pad':5})  
            plt.text( 0.7,0.8, texto)
            ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=115)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.gca().set_aspect('1')

            c = self.configuracion
            resumen = "[ Configuracion ] \nAnios Simulados: %d \nDias Simulados: %d \nMeses Simulados: %d \nHoras Prod.xDia: %d \nDias Prod.xMes: %d \nCant.Empleados: %d \nTiempo Atencion 1: %d \nTiempo Atencion 2: %d" %(c['anio'],c['dia'],c['mes'],c['horas_prod'],c['dias_prod'],2,c['t1'],c['t2']) 
            plt.text( -1.50,-1.2, resumen, horizontalalignment='left', bbox={'facecolor':'white', 'alpha':0.4, 'pad':30})
           
            pdf.savefig()  # saves the current figure into a pdf page
            plt.close()

            texto = "Total Dem. Insatis: %d \n Por Empleados %d \n Por Stock %d"%(demandas_insatisfechas, demoras_empl, demoras_stock)
            labels = 'Demoras Por Empleados', 'Demoras Por Stock'
            sizes = [demoras_empl,demoras_stock]
            explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, colors=colors2, autopct='%1.1f%%', shadow=True, startangle=112)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax1.set_title('Dem Insatisfechas', bbox={'facecolor':'0.9', 'pad':5})  
            plt.text( 0.7,0.8, texto)
            pdf.savefig()  # saves the current figure into a pdf page
            plt.close()

            # genero estadistica con param por defecto
            result_defecto = Simulacion(default=True).iniciar()
            estadisticas_defecto = Estadisticas().getEstadisticas(result_defecto)
            promedios_defecto = estadisticas_defecto.get('promedios_totales')

            demoras_empl_defecto = promedios_defecto.get('cant_demandas_sin_atender_por_demoras_empl')
            demoras_stock_defecto = promedios_defecto.get('cant_demandas_sin_atender_por_falta_stock')
            demandas_insatisfechas_defecto = demoras_empl_defecto + demoras_stock_defecto
            total_demandas_defecto = promedios_defecto.get('promedio_total_demandas')
            demandas_satisfechas_defecto = total_demandas_defecto - demandas_insatisfechas_defecto
          

            data = ((demandas_satisfechas_defecto, demandas_satisfechas), ('r', 'g'), ('Original', 'Nueva'))
            xPositions = np.arange(len(data[0]))
            barWidth = 0.70 

            _ax = plt.axes()  

            # bar(left, height, width=0.8, bottom=None, hold=None, **kwargs)
            _chartBars = plt.bar(xPositions, data[0], barWidth, color=data[1],
                                 yerr=5, align='center')  

            for bars in _chartBars:
                # text(x, y, s, fontdict=None, withdash=False, **kwargs)
                _ax.text(bars.get_x() + (bars.get_width() / 2.0), bars.get_height() + 5,
                         bars.get_height(), ha='center')  

            _ax.set_title('Produccion Comparacion', bbox={'facecolor':'0.9', 'pad':4}) 
            _ax.set_xticks(xPositions)
            _ax.set_xticklabels(data[2])

            plt.xlabel('Configuracion')
            plt.ylabel('Produccion')
            plt.grid(True)


            pdf.savefig()  # saves the current figure into a pdf page
            plt.close()


            d = pdf.infodict()
            d['Title'] = 'Simulacion MyS2017'
            d['Author'] = u'Nicoc'
            d['Subject'] = 'Simulacion de fabrica de autopartes'
            d['Keywords'] = 'PdfPages multipage keywords author title subject'
            d['CreationDate'] = datetime.datetime(2009, 11, 13)
            d['ModDate'] = datetime.datetime.today()
            
            plt.close('all')

            os.spawnv(os.P_NOWAIT, '/usr/bin/atril', ['atril', nombrePdf])


if __name__ == '__main__':
    result = Simulacion(default=True).iniciar()
    estadisticas = Estadisticas().getEstadisticas(result)
    g = GeneradorPdf(estadisticas).getPdf()
