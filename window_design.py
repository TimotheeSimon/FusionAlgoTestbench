# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt



import serial as ser
import threading as th
import os

import rightWidget as rw
import fonts as fo


class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.setWindow()
        self.setupUi()

    def setupUi(self):
        # Panneau de configuration
        self.panneau_de_conf = QtWidgets.QGroupBox(self.central_widget)
        self.panneau_de_conf.setGeometry(QtCore.QRect(10, 0, 251, 670))
        self.panneau_de_conf.setFont(fo.title_font)
        self.panneau_de_conf.setAlignment(QtCore.Qt.AlignCenter)
        self.panneau_de_conf.setObjectName("panneau_de_conf")
        # Panneau serial communication
        self.panneau_serial_com = QtWidgets.QGroupBox(self.panneau_de_conf)
        self.panneau_serial_com.setGeometry(QtCore.QRect(10, 30, 231, 171))
        self.panneau_serial_com.setFont(fo.standard_font)
        self.panneau_serial_com.setTitle("")
        self.panneau_serial_com.setAlignment(QtCore.Qt.AlignCenter)
        self.panneau_serial_com.setObjectName("panneau_serial_com")
        # Liste port COM
        self.list_port_com = QtWidgets.QComboBox(self.panneau_serial_com)
        self.list_port_com.setGeometry(QtCore.QRect(10, 30, 211, 22))
        self.list_port_com.setObjectName("list_port_com")
        t = th.Thread(None, self.findCOMPorts)
        t.start()
        # Label port COM
        self.label_port_com = QtWidgets.QLabel(self.panneau_serial_com)
        self.label_port_com.setGeometry(QtCore.QRect(0, 10, 231, 20))
        self.label_port_com.setAlignment(QtCore.Qt.AlignCenter)
        self.label_port_com.setObjectName("label_port_com")
        # Liste vitesse de communication
        self.list_speed_com = QtWidgets.QComboBox(self.panneau_serial_com)
        self.list_speed_com.setGeometry(QtCore.QRect(10, 80, 211, 22))
        self.list_speed_com.setObjectName("list_speed_com")
        self.list_speed_com.addItems(['9600','14400','19200','28800','38400','57600','115200'])
        # Label vitesse de communication
        self.label_speed_com = QtWidgets.QLabel(self.panneau_serial_com)
        self.label_speed_com.setGeometry(QtCore.QRect(0, 60, 231, 20))
        self.label_speed_com.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speed_com.setObjectName("label_speed_com")
        # Bouton démarrer communication
        self.btn_start_com = QtWidgets.QPushButton(self.panneau_serial_com)
        self.btn_start_com.setGeometry(QtCore.QRect(30, 120, 171, 31))
        self.btn_start_com.setAutoRepeatDelay(304)
        self.btn_start_com.setAutoDefault(False)
        self.btn_start_com.setDefault(False)
        self.btn_start_com.setFlat(False)
        self.btn_start_com.setObjectName("btn_start_com")
        self.btn_start_com.clicked.connect(self.startSerialCallback)
        # Bouton stopper communication
        self.btn_stop_com = QtWidgets.QPushButton(self.panneau_serial_com)
        self.btn_stop_com.setGeometry(QtCore.QRect(30, 120, 171, 31))
        self.btn_stop_com.setAutoRepeatDelay(304)
        self.btn_stop_com.setAutoDefault(False)
        self.btn_stop_com.setDefault(False)
        self.btn_stop_com.setFlat(False)
        self.btn_stop_com.setObjectName("btn_stop_com")
        self.btn_stop_com.clicked.connect(self.stopSerialCallback)
        self.btn_stop_com.setVisible(False)
        # Widget plot
        self.widget_right = QtWidgets.QWidget(self.central_widget)
        self.widget_right.setGeometry(QtCore.QRect(269, 9, 771, 641))
        self.widget_right.setObjectName("widget_right")
        layout = QtGui.QVBoxLayout()
        self.widget_right.setLayout(layout)
        




        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def setWindow(self):
        # Main window
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setEnabled(True)
        self.MainWindow.resize(1050, 700)
        self.MainWindow.setMaximumSize(QtCore.QSize(1050, 750))
        # Central Widget
        self.central_widget = QtWidgets.QWidget(self.MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.MainWindow.setCentralWidget(self.central_widget)
        self.central_widget.setAutoFillBackground(True)
        p = self.central_widget.palette()
        p.setColor(self.central_widget.backgroundRole(), Qt.white)
        self.central_widget.setPalette(p)
        # Menu bar
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 21))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        # Status bar
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "IMU data visualisation"))
        self.panneau_de_conf.setTitle(_translate("MainWindow", "Panneau de configuration"))
        self.label_port_com.setText(_translate("MainWindow", "Port série"))
        self.label_speed_com.setText(_translate("MainWindow", "Vitesse de communication"))
        self.btn_start_com.setText(_translate("MainWindow", "Démarrer la communication"))
        self.btn_stop_com.setText(_translate("MainWindow", "Stopper la communication"))

    def findCOMPorts(self):
        self.statusbar.showMessage( "Looking for COM ports ..." )
        COMs = os.popen("python -m serial.tools.list_ports -q").read().split()
        self.list_port_com.addItems(COMs)
        self.statusbar.showMessage( "Ready to start" )

    def startSerialCallback(self):
          
        try:
            self.statusbar.showMessage( "Starting serial communication ..." )
            self.serial = ser.Serial(self.list_port_com.currentText(), int(self.list_speed_com.currentText()), timeout=1)
            self.statusbar.showMessage( "Success!" )
            rw.RightWidget(self.serial, self.widget_right) 
            self.btn_start_com.setVisible(False)
            self.btn_stop_com.setVisible(True)
        except:
            self.statusbar.showMessage( "Failed to open serial communication" )

        
    def stopSerialCallback(self):
        self.serial.close()
        self.statusbar.showMessage( "Closed serial communication" )
        self.btn_stop_com.setVisible(False)
        self.btn_start_com.setVisible(True)
        





