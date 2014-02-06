
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
        
        seq = self.lineTo2DPoints(line)
        if seq == None: return
        
        XSeq = [s[0] for s in seq]
        YSeq = [s[1] for s in seq]
        self.X.append(XSeq)
        self.Y.append(YSeq)
      
    
    def lineTo2DPoints(self, line):
        seq = [float(x) for x in line.split(' ')]
        if len(seq) % 2 != 0:
            sys.stderr.write('Warning: invalid line encountered.')
            return None
    
        return [(seq[2*i], seq[2*i+1]) for i in range(len(seq)/2)]
        
    def streamEnd(self):
        
        plot = ScatterPlot(self.X, self.Y)
        plot(self.args.out)
        
        
            
        
