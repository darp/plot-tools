
from lib.plots.AbstractPlot import AbstractPlot

class SequencePlot(AbstractPlot):

    def __init__( self, vals, ymax=None, xmax=None ):
        self.vals = vals
        params = self.__initParams(ymax, xmax)
        AbstractPlot.__init__(self, params)

    def __initParams( self, ymax, xmax ):
        params = dict()
        if xmax == None:
            xmax = len(self.vals)
        params['xlim'] = [0,xmax]
        if ymax == None:
            ymax = max(abs(self.vals))+10
        ymin = min(0, min(self.vals))
        params['ylim'] = [-ymin,ymax]
        params['xlabel'] = 'n'
        params['ylabel'] = 'h(n)'
        params['legend_location'] = 2
        return params

    def registerPlottingFunctions( self ):
        functions = list()
        functions.append(self.__plotSequence)
        return functions
    
    def __plotSequence( self ):
        x = range(len(self.vals))
        y = self.vals
        self._plot_vlines(x, y, '') 
