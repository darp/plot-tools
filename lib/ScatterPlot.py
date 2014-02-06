
from lib.PaperPlotTemplate import PaperPlotTemplate
import numpy as np

class ScatterPlot(PaperPlotTemplate):
    
    def __init__(self, X, Y):
        
        self.X = X
        self.Y = Y

        params = dict()
        # params['xlim'] = [0, max(X)]
        maxi = max(np.abs(X))+max(X)+10
        # params['ylim'] = [-maxi,maxi]
        params['legend_location'] = 2
        PaperPlotTemplate.__init__(self, params)

    def _get_plotting_functions( self ):
        functions = list()
        functions.append(self._plot_scatter1)
        return functions

    def _plot_scatter1(self):
        
        self._plot_scatter(self.X, self.Y, '')
        
