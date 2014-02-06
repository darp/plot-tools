
from lib.PipeTool import PipeTool
from lib.plots.ScatterPlot import ScatterPlot
import sys

class ScatterPlotTool(PipeTool):

    def __init__(self, DESCRIPTION):
        PipeTool.__init__(self, DESCRIPTION)
        
    def streamStart(self):
        self.X = []
        self.Y = []

    def processLine(self, line):
        
        seq = [float(x) for x in line.split(' ')]
        if len(seq) != 2:
            sys.stderr.write('Warning: invalid line encountered.')
            return
        
        self.X.append(seq[0])
        self.Y.append(seq[1])
    
    def streamEnd(self):
        
        plot = ScatterPlot(self.X, self.Y)
        plot(self.args.out)
        
        
            
        
