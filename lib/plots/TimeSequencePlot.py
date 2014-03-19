
from lib.plots.AbstractPlot import AbstractPlot
import numpy as np

class TimeSequencePlot(AbstractPlot):

    def __init__( self, timeSeq, expSeq ):
        self.timeSeq = timeSeq
        self.expSeq = expSeq
        params = dict()
        params['xlim'] = [0,len(timeSeq)]
        maxi = max(max(abs(timeSeq)),max(abs(expSeq)))+100
        params['ylim'] = [-maxi,maxi]
        params['xlabel'] = 'n'
        params['ylabel'] = 'h(n)'
        params['legend_location'] = 2
        AbstractPlot.__init__(self, params)

    def registerPlottingFunctions( self ):
        functions = list()
        functions.append(self.__plotScatterTimeSequence)
        functions.append(self.__plotExpSequence)
        functions.append(self.__plotMeanTimeSequence)
        return functions
    
    def __plotScatterTimeSequence( self ):
        x = range(len(self.timeSeq))
        y = self.timeSeq
        params = {'dotsize' : 5}
        self._plot_scatter(x, y, 'Time Sequence', params) 

    def __plotExpSequence( self ):
        x = range(len(self.expSeq))
        y = self.expSeq
        params = {'color' : 'red', 'linestyle' : '--'}
        self._plot_line(x, y, 'Expected Sequence', params) 

    def __plotMeanTimeSequence( self ):
        x = range(len(self.timeSeq))
        y = np.mean(self.timeSeq)*np.ones(len(self.timeSeq))
        params = {'color' : 'blue', 'linestyle' : '--'}
        self._plot_line(x, y, 'Mean Value', params)
