#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from main import Ui_MainWindow
from simulacion 

class Main(QtGui.QMainWindow):
    """docstring for Main"""
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnIniciarSimulacion.clicked.connect(self.obtener_config)

    def obtener_config(self):
    	cant_anios = self.ui.inputCantAnios.text()
    	print cant_anios



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
