#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.uic import *

class Myform(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("gui.ui",self)

    def operar(self):
        numero=self.sender().text()
        #objectName()[-1]
        display=self.ui.txbDisplay
        display.setText(display.text()+numero)

    def calcular(self):
        display=self.ui.txbDisplay
        calculo=str(display.text())
        display.setText(str(eval(calculo)))
        

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    #plastique
    
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
    myapp = Myform()
    myapp.show()
    sys.exit(app.exec_())
