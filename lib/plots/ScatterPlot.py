
from lib.plots.AbstractPlot import AbstractPlot

class ScatterPlot(AbstractPlot):
    
    def __init__(self, X, Y):
        
        self.X = X
        self.Y = Y

        params = dict()
        params['xlim'] = [min(X), max(X)]
        params['ylim'] = [min(Y), max(Y)]
        params['legend_location'] = 2
        AbstractPlot.__init__(self, params)

    def registerPlottingFunctions( self ):
        functions = list()
        functions.append(self._plot_scatter1)
        return functions

    def _plot_scatter1(self):
        
        self._plot_scatter(self.X, self.Y, '')
        
