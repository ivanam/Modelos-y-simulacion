"""
This is a demo of creating a pdf file with several pages,
as well as adding metadata and annotations to pdf files.
"""

import datetime
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from modelos import *
# Create the PdfPages object to which we will save the pages:
# The with statement makes sure that the PdfPages object is closed properly at
# the end of the block, even if an Exception occurs.

class GeneradorPdf:

    def __init__(self, estadisticas = None):
        self.promedios = estadisticas.get('promedios_totales')

    def getPdf(self):
        assert self.promedios
        with PdfPages('simulacion.pdf') as pdf:

            """plt.figure(figsize=(3, 3))
            plt.hist([1,2,3,2,2,4,2,1,2])
            plt.title('Demandas Instatisfechas')
            pdf.savefig()  # saves the current figure into a pdf page
            plt.close()"""
            p = self.promedios
            labels = 'Demandas Satisfechas', 'Demandas Insatisfechas'

            demoras_empl = p.get('cant_demandas_sin_atender_por_demoras_empl')
            demoras_stock = p.get('cant_demandas_sin_atender_por_falta_stock')
            demandas_insatisfechas = demoras_empl + demoras_stock
            total_demandas = p.get('promedio_total_demandas')
            demandas_satisfechas = total_demandas -demandas_insatisfechas
            
            plt.title('Analisis de Demandas')
            texto = "Total de demandas: %d \n Insatisfechas %d \n Satisfechas %d"%(total_demandas,demandas_insatisfechas, demandas_satisfechas)
            sizes = [demandas_satisfechas, demandas_insatisfechas]
            explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()  
            plt.text( -0.01,0.9, texto)
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=100)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            pdf.savefig()  # saves the current figure into a pdf page
            plt.close()

            plt.title('Demandas Insatisfechas')
            texto = "Total de demandas insatisfechas: %d \n Por Empleados %d \n Por Stock %d"%(demandas_insatisfechas, demoras_empl, demoras_stock)
            labels = 'Demoras Por Empleados', 'Demoras Por Stock'
            sizes = [demoras_empl,demoras_stock]
            explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.text( -0.01,0.9, texto)
            pdf.savefig()  # saves the current figure into a pdf page
            plt.close()

            plt.rc('text', usetex=False)
            plt.figure(figsize=(3, 3))
            x = np.arange(0, 5, 0.1)
            plt.title('Page Two')
            pdf.savefig()
            plt.close()

            d = pdf.infodict()
            d['Title'] = 'Simulacion MyS2017'
            d['Author'] = u'Nicoc'
            d['Subject'] = 'Simulacion de fabrica de autopartes'
            d['Keywords'] = 'PdfPages multipage keywords author title subject'
            d['CreationDate'] = datetime.datetime(2009, 11, 13)
            d['ModDate'] = datetime.datetime.today()


if __name__ == '__main__':
    result = Simulacion(default=True).iniciar()
    estadisticas = Estadisticas().getEstadisticas(result)
    g = GeneradorPdf(estadisticas).getPdf()
