#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from forms.main import Ui_MainWindow
import json
from modelos import *
from forms import simulacion
from dialogs import simulacion

class Main(QtGui.QMainWindow):
    """docstring for Main"""
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnIniciarSimulacion.clicked.connect(self.obtener_config)
        self.ui.btnDefecto.clicked.connect(self.config_defecto)

    def obtener_config(self):

        cantAnios = int(self.ui.inputCantAnios.text())
        mesesAnios = int(self.ui.inputMesesAnio.text())
        diasAnios = int(self.ui.cantDiasAnios.text())
        horasDias = int(self.ui.cantHorasDia.text())
        cantDiasProduccion = int(self.ui.cantDiasProduccion.text())
        cantEmpleados = int(self.ui.inputCantEmpleados.text())
        tiempoAtencion1 = int(self.ui.inputTiempoAtencion1.text())
        tiempoAtencion2 = int(self.ui.inputTiempoAtencion2.text())
        
        sim = Simulacion(default=True)
        sim.cant_anios = cantAnios
        sim.meses_anio = mesesAnios
        sim.dias_mes = diasAnios
        sim.horas_trabajo = horasDias
        sim.dias_produccion = cantDiasProduccion
        #sim.cantAnios = cantEmpleados
        sim.set_tiempos_atencion(tiempoAtencion1, tiempoAtencion2) 
        if sim.estado == 'configurado':
            res = sim.iniciar()
            d = simulacion.form_simulacion(res)
            d.exec_()
        print "Error en la configuracion"

    def config_defecto(self):

        with open('config.json') as data_file:    
            config = json.load(data_file)
        self.ui.inputCantAnios.setText(str(config['cant_anios']))
        self.ui.inputMesesAnio.setText(str(config['meses_anio']))
        self.ui.cantDiasAnios.setText(str(config['dias_mes']))
        self.ui.cantHorasDia.setText(str(config['empleados']['horas_trabajo']))
        self.ui.cantDiasProduccion.setText(str(config['dias_produccion']))
        self.ui.inputCantEmpleados.setText(str(config['empleados']['cantidad']))
        self.ui.inputTiempoAtencion1.setText(str(config['productos'][0]['parametros']['lam']))
        self.ui.inputTiempoAtencion2.setText(str(config['productos'][1]['parametros']['lam']))

        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
