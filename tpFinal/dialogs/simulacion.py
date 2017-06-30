#! /usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from forms.simulacion import Ui_Form 
from PyQt4.QtGui import *
import time
from modelos import Estadisticas
from pdf import GeneradorPdf
from estadisticas import EstadisticasPlot

class form_simulacion(QtGui.QDialog):

    DT_MS = 1000

    def __init__(self, json_simulacion):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # atributos de la gui simulacion
        self.estadisticas = None
        self.sim = json_simulacion
        self.i_anio = 0
        self.i_evento = 0
        self.timer = self.crear_timer()
        #eventos 
        self.ui.btnPararSim.clicked.connect(self.parar_simulacion)
        self.ui.btnContinuarSim.clicked.connect(self.iniciar_timer)
        self.ui.btnFinalizarSim.clicked.connect(self.finalizar_simulacion)
        self.ui.btnInformeEstadistico.clicked.connect(self.informePdf)
        
        self.ui.lblDiaMesAnioFinal.setText('Dias: '+str(self.sim.get('dias'))+' \n Meses: '+str(self.sim.get('meses'))+' \n Anios: '+str(self.sim.get('anios'))  )
        #self.ui.btnInformeEstadistico.clicked.connect(self.finalizar_simulacion)
        #acciones: inicio rapido de mostrar
        self.iniciar_timer(1)

    
    def estadisticasPlot(self):
        h = EstadisticasPlot(self.estadisticas).getPlot()
        print "GRAFICOS GENERADO"


    def informePdf(self):
        # add
        configuracion = {
            'anio': self.sim.get('anios'),
            'dia': self.sim.get('dias'),
            'mes': self.sim.get('meses'),
            'horas_prod': self.sim.get('horas_prod'),
            'dias_prod': self.sim.get('dias_prod'),
            'cant_emp': self.sim.get('cant_emp'),
            't1': self.sim.get('t1'),
            't2': self.sim.get('t2')
        }

        g = GeneradorPdf(configuracion, self.estadisticas).getPdf()
        print "PDF GENERADO"
        self.estadisticasPlot()


    def finalizar_simulacion(self):
        s = self.sim.get('simulacion')
        s = s[-1] #last
        anio = s.get('anio')
        evento = s.get('eventos')[-1]
        self.ui.lblDemandaAcumulada.setText(str(evento.get('acumulado')))
        self.ui.lblDemandaDiaria.setText(str(evento.get('demanda')))
        self.ui.lblStockAutoparte1.setText(str(evento.get('stock')[0].values()[0]))
        self.ui.lblStockAutoparte2.setText(str(evento.get('stock')[1].values()[0]))
        self.ui.lblAtencionDemandas.setText(str(evento.get('satisfecho')))
        dia = [int(s) for s in str.split(evento.get('dia')) if s.isdigit()][0]
        if dia <= self.sim.get('dias_produccion'):
            self.ui.lblEventoSockAutoparte1.setText("+ 110")
            self.ui.lblEventoAutoparte2l.setText("+ 160")
        else:
            self.ui.lblEventoSockAutoparte1.setText("+ 0")
            self.ui.lblEventoAutoparte2l.setText("+ 0")
        
        dia_mes = evento.get('dia').split('-');
        dia = 'Dia: ' + dia_mes[0] + ' \n Mes: ' + dia_mes[1] + ' \n Anio: ' + str(anio)    
        self.ui.lblDiaMesAnio.setText(dia)
        self.fin_simulacion()       

    def crear_timer(self):
        t = QtCore.QTimer()
        t.setSingleShot(True)
        t.timeout.connect(self.mostrar)
        return t

    def iniciar_timer(self, ms=None):
        print ms
        if self.timer.isActive():
            return
        if ms:
            self.timer.start(ms)
        else:
            self.timer.start(form_simulacion.DT_MS)
    
    def parar_simulacion(self):
        if self.timer.isActive():
            self.timer.stop()

    def fin_simulacion(self):
        self.timer.stop()
        self.i_evento = 0
        self.i_anio = 0
        self.mostrar_estadisticas(self.sim)

    def mostrar_estadisticas(self, sim):
        simulacion = sim.get('simulacion')
        self.ui.lblTotalDias.setText(str(len(simulacion[0].get('eventos'))-1))
        self.estadisticas = Estadisticas().getEstadisticas(sim)
        promedios_generales = self.estadisticas.get('promedios_totales')
        self.ui.lblAcumuladoPorDia.setText(str(promedios_generales.get('prom_acumulado_por_dia')))
        self.ui.lblCantDemorasEmp.setText(str(promedios_generales.get('cant_dias_demoras_empl')))
        self.ui.lblCantDemorasStock.setText(str(promedios_generales.get('cant_dias_falta_stock')))
        self.ui.lblTotalDemandas.setText(str(promedios_generales.get('promedio_total_demandas')))

    def mostrar(self):
        sim = self.sim.get('simulacion')
        try:    
            sim_anio = sim[self.i_anio]
        except:
            print "FIN simulacion"
            self.fin_simulacion()
            return 
        evento = sim_anio.get('eventos')[self.i_evento]     
        self.ui.lblDemandaAcumulada.setText(str(evento.get('acumulado')))
        self.ui.lblDemandaDiaria.setText(str(evento.get('demanda')))
        self.ui.lblStockAutoparte1.setText(str(evento.get('stock')[0].values()[0]))
        self.ui.lblStockAutoparte2.setText(str(evento.get('stock')[1].values()[0]))
        
        self.ui.lblAtencionDemandas.setText(str(evento.get('satisfecho')))
        self.i_evento += 1
        
        dia = [int(s) for s in str.split(evento.get('dia')) if s.isdigit()][0]
        if dia <= self.sim.get('dias_produccion'):
            self.ui.lblEventoSockAutoparte1.setText("+ 110")
            self.ui.lblEventoAutoparte2l.setText("+ 160")
        else:
            self.ui.lblEventoSockAutoparte1.setText("+ 0")
            self.ui.lblEventoAutoparte2l.setText("+ 0")
        
        if len(sim_anio.get('eventos')) == self.i_evento:
            self.i_evento = 0
            self.i_anio += 1
        
        dia_mes = evento.get('dia').split('-');
        dia = 'Dia: ' + dia_mes[0] + ' \n Mes: ' + dia_mes[1] + ' \n Anio: ' + str(sim_anio.get('anio'))
        self.ui.lblDiaMesAnio.setText(dia)
        self.iniciar_timer()

        
