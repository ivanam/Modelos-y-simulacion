# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulacion.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(721, 572)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.lvlEventoDemandaAcumulada = QtGui.QLabel(self.groupBox_2)
        self.lvlEventoDemandaAcumulada.setText(_fromUtf8(""))
        self.lvlEventoDemandaAcumulada.setObjectName(_fromUtf8("lvlEventoDemandaAcumulada"))
        self.gridLayout_3.addWidget(self.lvlEventoDemandaAcumulada, 0, 2, 1, 1)
        self.lblEventoDemandaDiaria = QtGui.QLabel(self.groupBox_2)
        self.lblEventoDemandaDiaria.setText(_fromUtf8(""))
        self.lblEventoDemandaDiaria.setObjectName(_fromUtf8("lblEventoDemandaDiaria"))
        self.gridLayout_3.addWidget(self.lblEventoDemandaDiaria, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.lblDemandaDiaria = QtGui.QLabel(self.groupBox_2)
        self.lblDemandaDiaria.setObjectName(_fromUtf8("lblDemandaDiaria"))
        self.gridLayout_3.addWidget(self.lblDemandaDiaria, 1, 1, 1, 1)
        self.lblDemandaAcumulada = QtGui.QLabel(self.groupBox_2)
        self.lblDemandaAcumulada.setObjectName(_fromUtf8("lblDemandaAcumulada"))
        self.gridLayout_3.addWidget(self.lblDemandaAcumulada, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lblEventoSockAutoparte1 = QtGui.QLabel(self.groupBox)
        self.lblEventoSockAutoparte1.setObjectName(_fromUtf8("lblEventoSockAutoparte1"))
        self.gridLayout_2.addWidget(self.lblEventoSockAutoparte1, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.lblStockAutoparte2 = QtGui.QLabel(self.groupBox)
        self.lblStockAutoparte2.setObjectName(_fromUtf8("lblStockAutoparte2"))
        self.gridLayout_2.addWidget(self.lblStockAutoparte2, 1, 1, 1, 1)
        self.lblStockAutoparte1 = QtGui.QLabel(self.groupBox)
        self.lblStockAutoparte1.setObjectName(_fromUtf8("lblStockAutoparte1"))
        self.gridLayout_2.addWidget(self.lblStockAutoparte1, 0, 1, 1, 1)
        self.lblEventoAutoparte2l = QtGui.QLabel(self.groupBox)
        self.lblEventoAutoparte2l.setObjectName(_fromUtf8("lblEventoAutoparte2l"))
        self.gridLayout_2.addWidget(self.lblEventoAutoparte2l, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.lblAtencionDemandas = QtGui.QLabel(self.groupBox_3)
        self.lblAtencionDemandas.setObjectName(_fromUtf8("lblAtencionDemandas"))
        self.gridLayout_5.addWidget(self.lblAtencionDemandas, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.btnPararSim = QtGui.QPushButton(Form)
        self.btnPararSim.setObjectName(_fromUtf8("btnPararSim"))
        self.gridLayout_4.addWidget(self.btnPararSimz, 4, 0, 1, 1)
        self.btnContinuarSim = QtGui.QPushButton(Form)
        self.btnContinuarSim.setObjectName(_fromUtf8("btnContinuarSim"))
        self.gridLayout_4.addWidget(self.btnContinuarSim, 5, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_15 = QtGui.QLabel(Form)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout.addWidget(self.label_15)
        self.lblDiaMesAnio = QtGui.QLabel(Form)
        self.lblDiaMesAnio.setObjectName(_fromUtf8("lblDiaMesAnio"))
        self.horizontalLayout.addWidget(self.lblDiaMesAnio)
        self.lblDiaMesAnioFinal = QtGui.QLabel(Form)
        self.lblDiaMesAnioFinal.setObjectName(_fromUtf8("lblDiaMesAnioFinal"))
        self.horizontalLayout.addWidget(self.lblDiaMesAnioFinal)
        self.gridLayout_4.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.btnFinalizarSim = QtGui.QPushButton(Form)
        self.btnFinalizarSim.setObjectName(_fromUtf8("btnFinalizarSim"))
        self.gridLayout_4.addWidget(self.btnFinalizarSim, 6, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_4)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.lblTotalDemandas = QtGui.QLabel(self.groupBox_4)
        self.lblTotalDemandas.setObjectName(_fromUtf8("lblTotalDemandas"))
        self.gridLayout_7.addWidget(self.lblTotalDemandas, 5, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_7.addWidget(self.label_9, 3, 0, 1, 1)
        self.lblTotalDias = QtGui.QLabel(self.groupBox_4)
        self.lblTotalDias.setObjectName(_fromUtf8("lblTotalDias"))
        self.gridLayout_7.addWidget(self.lblTotalDias, 0, 1, 1, 1)
        self.btnInformeEstadistico = QtGui.QPushButton(self.groupBox_4)
        self.btnInformeEstadistico.setObjectName(_fromUtf8("btnInformeEstadistico"))
        self.gridLayout_7.addWidget(self.btnInformeEstadistico, 6, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_7.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_7.addWidget(self.label_11, 5, 0, 1, 1)
        self.lblCantDemorasStock = QtGui.QLabel(self.groupBox_4)
        self.lblCantDemorasStock.setObjectName(_fromUtf8("lblCantDemorasStock"))
        self.gridLayout_7.addWidget(self.lblCantDemorasStock, 4, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_7.addWidget(self.label_10, 4, 0, 1, 1)
        self.lblCantDemorasEmp = QtGui.QLabel(self.groupBox_4)
        self.lblCantDemorasEmp.setObjectName(_fromUtf8("lblCantDemorasEmp"))
        self.gridLayout_7.addWidget(self.lblCantDemorasEmp, 3, 1, 1, 1)
        self.lblAcumuladoPorDia = QtGui.QLabel(self.groupBox_4)
        self.lblAcumuladoPorDia.setObjectName(_fromUtf8("lblAcumuladoPorDia"))
        self.gridLayout_7.addWidget(self.lblAcumuladoPorDia, 2, 1, 1, 1)
        self.lblTotalAcumulado = QtGui.QLabel(self.groupBox_4)
        self.lblTotalAcumulado.setObjectName(_fromUtf8("lblTotalAcumulado"))
        self.gridLayout_7.addWidget(self.lblTotalAcumulado, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox_2.setTitle(_translate("Form", "Demanda", None))
        self.label_3.setText(_translate("Form", "Acumulada", None))
        self.label_4.setText(_translate("Form", "Diaria", None))
        self.lblDemandaDiaria.setText(_translate("Form", "20", None))
        self.lblDemandaAcumulada.setText(_translate("Form", "100", None))
        self.groupBox.setTitle(_translate("Form", "Deposito", None))
        self.lblEventoSockAutoparte1.setText(_translate("Form", "+ 160 ", None))
        self.label_2.setText(_translate("Form", "autoparte 2", None))
        self.lblStockAutoparte2.setText(_translate("Form", "1500", None))
        self.lblStockAutoparte1.setText(_translate("Form", "2000", None))
        self.lblEventoAutoparte2l.setText(_translate("Form", "+ 110", None))
        self.label.setText(_translate("Form", "autoparte 1", None))
        self.groupBox_3.setTitle(_translate("Form", "Empleados", None))
        self.lblAtencionDemandas.setText(_translate("Form", "2000", None))
        self.label_8.setText(_translate("Form", "Demandas Atendidas", None))
        self.btnPararSim.setText(_translate("Form", "Parar", None))
        self.btnContinuarSim.setText(_translate("Form", "Continuar", None))
        self.label_15.setText(_translate("Form", "Dia", None))
        self.lblDiaMesAnio.setText(_translate("Form", "1 / 2 / 1 ", None))
        self.lblDiaMesAnioFinal.setText(_translate("Form", "30 - 12 - 5", None))
        self.btnFinalizarSim.setText(_translate("Form", "Finalizar", None))
        self.groupBox_4.setTitle(_translate("Form", "Promedios Generales", None))
        self.lblTotalDemandas.setText(_translate("Form", "0", None))
        self.label_9.setText(_translate("Form", "Demandas demoradas por empleados", None))
        self.lblTotalDias.setText(_translate("Form", "0", None))
        self.btnInformeEstadistico.setText(_translate("Form", "Ver Informe Detallado", None))
        self.label_7.setText(_translate("Form", "Total Acumulado", None))
        self.label_5.setText(_translate("Form", "Total de dias", None))
        self.label_6.setText(_translate("Form", "Acum por dia", None))
        self.label_11.setText(_translate("Form", "Total de demandas", None))
        self.lblCantDemorasStock.setText(_translate("Form", "0", None))
        self.label_10.setText(_translate("Form", "Demandas demoradas por stock", None))
        self.lblCantDemorasEmp.setText(_translate("Form", "0", None))
        self.lblAcumuladoPorDia.setText(_translate("Form", "0", None))
        self.lblTotalAcumulado.setText(_translate("Form", "0", None))

