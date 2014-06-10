
from lib.PipeTool import PipeTool
import pylab

class HistTool(PipeTool):
    
    def __init__(self, DESCRIPTION):
        PipeTool.__init__(self, DESCRIPTION)

    
    def processLine(self, line):
        vals = [float(x) for x in line.split(' ')]
        pylab.hist(vals, 100)
        pylab.show()
