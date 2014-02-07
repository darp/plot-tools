
from lib.tools.ScatterPlotTool import ScatterPlotTool
from lib.plots.Histogram3D import Histogram3D

class HistogramTool3D(ScatterPlotTool):
    
    def __init__(self, description):
        ScatterPlotTool.__init__(self, description)
        
    def streamEnd(self):
        
        plot = Histogram3D(self.X, self.Y)
        plot(self.args.out)
        