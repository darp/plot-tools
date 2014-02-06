from joerntools.shelltool.PipeTool import PipeTool
import sys

class HistogramTool3D(PipeTool):
    
    def __init__(self, description):
        PipeTool.__init__(self, description)
        

    def streamStart(self):
        self.X = []
        self.Y = []
    
    def processLine(self, line):
        seq = self.lineTo2DPoint(line)
        if seq == None: return
        
        self.X.append(seq[0])
        self.Y.append(seq[1])
        
    def lineTo2DPoint(self, line):
        seq = [float(x) for x in line.split(' ')]
        if len(seq) != 2:
            sys.stderr.write('Warning: invalid line encountered.')
            return None
        return seq
    
    def streamEnd(self):
        
        import numpy as np
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import *
           
        fig = plt.figure()
        ax = Axes3D(fig)
        
        hist, xedges, yedges = np.histogram2d(self.X, self.Y, bins=100)
        elements = (len(xedges) - 1) * (len(yedges) - 1)
        xpos, ypos = np.meshgrid(xedges[:-1]+0.25, yedges[:-1]+0.25)

        xpos = xpos.flatten()
        ypos = ypos.flatten()
        zpos = np.zeros(elements)
        dx = 0.5 * np.ones_like(zpos)
        dy = dx.copy()
        dz = hist.flatten()

        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b')
        
        # ax.set_xlim(-200000, 0)
        # ax.set_ylim(0, 200000)

        plt.show()