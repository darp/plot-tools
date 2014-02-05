
from lib.PipeTool import PipeTool
from lib.MeanDeviationPlot import MeanDeviationPlot
import sys
import numpy as np

class PlotMeanSequence(PipeTool):

    def __init__(self, DESCRIPTION):
        PipeTool.__init__(self, DESCRIPTION)
        
        
        self.argParser.add_argument('-o', '--out', nargs='?', type=str,
                                    default='',
                                    help = 'write output to provided file')

    def streamStart(self):
        self.mean = None
        self.standardDev = None

        if self.args.out == '':
            print 'Please supply an output file using -o.'
            sys.exit(1)  

    def processLine(self, line):
        if self.mean == None:
            self.mean = [float(x) for x in line.split(' ')]
            self.standardDev = None
        elif self.standardDev == None:
            self.standardDev = [float(x) for x in line.split(' ')]
    
    def streamEnd(self):
        
        plot = MeanDeviationPlot(np.array(self.mean), np.array(self.standardDev))
        plot(self.args.out)
    
