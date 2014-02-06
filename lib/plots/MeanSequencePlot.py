
from lib.plots.AbstractPlot import AbstractPlot

# TODO: rename to MeanSequencePlot

class MeanSequencePlot(AbstractPlot):

    def __init__( self, means, stds ):
        self.means = means
        self.stds = stds
        params = dict()
        params['xlim'] = [0,len(means)]
        maxi = max(abs(means))+max(stds)+10
        params['ylim'] = [-maxi,maxi]
        params['xlabel'] = 'n'
        params['ylabel'] = 'h(n)'
        params['legend_location'] = 2
        AbstractPlot.__init__(self, params)

    def registerPlottingFunctions( self ):
        functions = list()
        functions.append(self.__plot_bars1)
        return functions
    
    def __plot_bars1(self):
        bars = self.means
        xlabels = map(self.__reduce_ticks, range(len(self.means)))
        text = 'Impulse Response'
        params = { 'yerr' : self.stds }
        self._plot_bars(bars, text, xlabels, params) 

    def __reduce_ticks(self, tick):
        if (tick % 10)==0:
            return str(tick)
        else:
            return ''

