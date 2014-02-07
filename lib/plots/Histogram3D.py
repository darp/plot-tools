from lib.plots.MultiPlot import MultiPlot

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import *

class Histogram3D(MultiPlot):

    def __init__(self, X, Y):
         
        MultiPlot.__init__(self, X, Y)
    
    def _initializeFigure(self):
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig)
    
    def _finishPlot(self):
        
        plt.show()
    
    def _multi_plot(self):

        X = self.X.pop()
        Y = self.Y.pop()
        
        hist, xedges, yedges = np.histogram2d(X, Y, bins=10)
        elements = (len(xedges) - 1) * (len(yedges) - 1)
        xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1])

        xpos = xpos.flatten()
        ypos = ypos.flatten()
        zpos = np.zeros(elements)
        dx = 0.5 * np.ones_like(zpos)
        dy = dx.copy()
        dz = hist.flatten()
               
        self.ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
 