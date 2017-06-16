#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from main import Ui_MainWindow
import json
from modelos import *
from simulacion import Ui_Form

class Main(QtGui.QMainWindow):
    """docstring for Main"""
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnIniciarSimulacion.clicked.connect(self.obtener_config)
        self.ui.btnDefecto.clicked.connect(self.config_defecto)

    def obtener_config(self):

        cantAnios = self.ui.inputCantAnios.text()
        mesesAnios = self.ui.inputMesesAnio.text()
        diasAnios = self.ui.cantDiasAnios.text()
        horasDias = self.ui.cantHorasDia.text()
        cantDiasProduccion = self.ui.cantDiasProduccion.text()
        cantEmpleados = self.ui.inputCantEmpleados.text()
        tiempoAtencion1 = self.ui.inputTiempoAtencion1.text()
        tiempoAtencion2 = self.ui.inputTiempoAtencion2.text()
        
        sim = Simulacion(default=True)
        sim.cantAnios = cantAnios
        sim.cantAnios = mesesAnios
        sim.cantAnios = diasAnios
        sim.cantAnios = horasDias
        sim.cantAnios = cantDiasProduccion
        sim.cantAnios = cantEmpleados
        sim.cantAnios = tiempoAtencion1
        sim.cantAnios = tiempoAtencion2
        Form = Simulacion()
        Form.show()
        sys.exit(app.exec_())
    	

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
