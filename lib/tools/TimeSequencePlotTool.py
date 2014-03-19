
from lib.PipeTool import PipeTool
from lib.plots.TimeSequencePlot import TimeSequencePlot
import numpy as np

class TimeSequencePlotTool(PipeTool):

    def __init__(self, DESCRIPTION):
        PipeTool.__init__(self, DESCRIPTION)
        
    def streamStart(self):
        self.timeSeq = None
        self.expSeq = None

    def processLine(self, line):
        if self.timeSeq == None:
            self.timeSeq = [float(x) for x in line.split(' ')]
            self.expSeq = None
        elif self.expSeq == None:
            self.expSeq = [float(x) for x in line.split(' ')]
    
    def streamEnd(self):
        plot = TimeSequencePlot(np.array(self.timeSeq), np.array(self.expSeq))
        plot(self.args.out)
        
