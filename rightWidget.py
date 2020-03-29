from PyQt5 import QtCore, QtGui, QtWidgets

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

import threading as th
import numpy as np





class RightWidget(QtWidgets.QWidget):

    def __init__(self, serial, widget_right):
        super(RightWidget, self).__init__(widget_right)
        self.widget_right = widget_right
        self.serial = serial
        self.setPlotWidget()
        self.plotData()
        
       


    def setPlotWidget(self):
        self.plot_widget_1 = pg.PlotWidget(name='plot_widget_1')
        self.plot_widget_2 = pg.PlotWidget(name='plot_widget_2')
        self.plot_widget_3 = pg.PlotWidget(name='plot_widget_3')
        self.widget_right.layout().addWidget(self.plot_widget_1)
        self.plot_widget_2 = pg.PlotWidget(name='plot_widget_2')  
        self.widget_right.layout().addWidget(self.plot_widget_2)
        self.plot_widget_3 = pg.PlotWidget(name='plot_widget_3')  
        self.widget_right.layout().addWidget(self.plot_widget_3)

        self.show()


        self.fig_1 = self.plot_widget_1.plot()
        self.fig_2 = self.plot_widget_2.plot()
        self.fig_3 = self.plot_widget_3.plot()

        self.plot_widget_1.setDownsampling(mode='peak')
        self.plot_widget_1.setClipToView(True)
        
        



    def update_plot(self):
        n = 1000
        t=0 
        self.Y = np.empty(n)
        
        while self.serial.is_open:
            try:
                data_read = self.serial.readline().decode('ascii').strip().strip('\x00')
                data_read = str(data_read).split(',')
    
                if len(data_read)==6: 
                    y=float(data_read[0])
                    print(y)
                    
                    
                    if t < n:
                        self.plot_widget_1.setRange(xRange=[0, n])
                        self.Y[t] = y
                        self.fig_1.setData(self.Y[:t])
                    else:
                        self.plot_widget_1.setRange(xRange=[t, t+n])
                        self.Y[:-1] = self.Y[1:]
                        self.Y[-1] = y
                        self.fig_1.setData(self.Y)
                        self.fig_1.setPos(t,0)
                    t += 1
                else:
                    print('ca bug')
                        
                    
            except:
                pass

    
    def plotData(self):
        t = th.Thread(target = self.update_plot)
        t.start()
