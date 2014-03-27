
from lib.PipeTool import PipeTool
from lib.plots.SequencePlot import SequencePlot
import numpy as np

class SequencePlotTool(PipeTool):

    def __init__(self, DESCRIPTION):
        PipeTool.__init__(self, DESCRIPTION)

        self.argParser.add_argument('-y', '--y_max', nargs='?', type=int,
                                    default=None,
                                    help = 'max value of y axis')
        self.argParser.add_argument('-x', '--x_max', nargs='?', type=int,
                                    default=None,
                                    help = 'max value of x axis')
        
    def streamStart(self):
        self.vals = None

    def processLine(self, line):
        if self.vals == None:
            self.vals = [float(x) for x in line.split(' ')]
    
    def streamEnd(self):
        plot = SequencePlot(np.array(self.vals), self.args.y_max,
                self.args.x_max)
        plot(self.args.out)
