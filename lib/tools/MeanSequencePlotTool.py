
from lib.PipeTool import PipeTool
from lib.plots.MeanSequencePlot import MeanSequencePlot
import numpy as np

class MeanSequencePlotTool(PipeTool):

    def __init__(self, DESCRIPTION):
        PipeTool.__init__(self, DESCRIPTION)
        
    def streamStart(self):
        self.mean = None
        self.standardDev = None
        

    def processLine(self, line):
        if self.mean == None:
            self.mean = [float(x) for x in line.split(' ')]
            self.standardDev = None
        elif self.standardDev == None:
            self.standardDev = [float(x) for x in line.split(' ')]
    
    def streamEnd(self):
        
        plot = MeanSequencePlot(np.array(self.mean), np.array(self.standardDev))
        plot(self.args.out)
        
