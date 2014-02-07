
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
        
        self.X.append(seq[0])
        self.Y.append(seq[1])
      
    
    def lineTo2DPoints(self, line):
        seq = [float(x) for x in line.split(' ')]
        if len(seq) % 2 != 0:
            sys.stderr.write('Warning: invalid line encountered.')
            return None

        seq = [(seq[2*i], seq[2*i+1]) for i in range(len(seq)/2)]
        XSeq = [s[0] for s in seq]
        YSeq = [s[1] for s in seq]
        
        return (XSeq, YSeq)
    
        
    def streamEnd(self):
        
        plot = ScatterPlot(self.X, self.Y)
        plot(self.args.out)
        
        
