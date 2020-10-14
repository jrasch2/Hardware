# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bmehl\OneDrive\Desktop\Research\GUIs\VCO_Control.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import nidaqmx
#system = nidaqmx.system.System.local() # finds all of the DAQS that are connected to the computer
#device_1 = system.devices['Dev1'] # we are using the first device that is connected to the DAQ for this application
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frequency_adjustment = QtWidgets.QSlider(self.centralwidget)
        self.frequency_adjustment.setGeometry(QtCore.QRect(170, 270, 271, 61))
        self.frequency_adjustment.setMaximum(10000)
        self.frequency_adjustment.setSingleStep(1)
        self.frequency_adjustment.setOrientation(QtCore.Qt.Horizontal)
        self.frequency_adjustment.setInvertedAppearance(False)
        self.frequency_adjustment.setInvertedControls(False)
        self.frequency_adjustment.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.frequency_adjustment.setTickInterval(1000)
        self.frequency_adjustment.setObjectName("frequency_adjustment")
        self.frequency_display = QtWidgets.QLCDNumber(self.centralwidget)
        self.frequency_display.setGeometry(QtCore.QRect(240, 210, 121, 51))
        self.frequency_display.display(198.99)
        self.frequency_display.setLineWidth(2)
        self.frequency_display.setObjectName("frequency_display")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(240, 360, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stop_button.setFont(font)
        self.stop_button.setObjectName("stop_button")
        self.freq_label = QtWidgets.QLabel(self.centralwidget)
        self.freq_label.setGeometry(QtCore.QRect(240, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.freq_label.setFont(font)
        self.freq_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.freq_label.setObjectName("freq_label")
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(172, 325, 16, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(198, 325, 16, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 325, 16, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(225, 325, 16, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(304, 325, 16, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(276, 325, 16, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(328, 325, 11, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(406, 325, 23, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(380, 325, 16, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(430, 325, 21, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(354, 325, 16, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.daq_port = device_1.ao_physical_chans['ao1'] # connects to the 1 analog output channel from the 1st device
        self.stop_button.clicked.connect(QtWidgets.qApp.quit) # this will terminate the window and close the program
        self.frequency_adjustment.valueChanged.connect(self.change_voltage_VCO)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.freq_label.setText(_translate("MainWindow", "VCO Frequency"))
        self.label_0.setText(_translate("MainWindow", "0"))
        self.label_1.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "2"))
        self.label_5.setText(_translate("MainWindow", "5"))
        self.label_6.setText(_translate("MainWindow", "4"))
        self.label_8.setText(_translate("MainWindow", "6"))
        self.label_9.setText(_translate("MainWindow", "9"))
        self.label_10.setText(_translate("MainWindow", "8"))
        self.label_12.setText(_translate("MainWindow", "10"))
        self.label_7.setText(_translate("MainWindow", "7"))
    def change_voltage_VCO(self):
        starting_value = 198.99
        slider_value = (self.frequency_adjustment.value()/1000)
        self.frequency_display.display(starting_value+slider_value*1.3908)
        #self.daq_port.write(slider_value)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
