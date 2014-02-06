from lib.plots.AbstractPlot import AbstractPlot
import numpy as np


class BarPlot(AbstractPlot):

    def __init__( self ):
        params = dict()
        params['xlim'] = [0,5]
        params['ylim'] = [0,50]
        params['xlabel'] = 'xlabel'
        params['ylabel'] = 'ylabel'
        params['legend_location'] = 2
        AbstractPlot.__init__( self, params )

    def registerPlottingFunctions( self ):
        functions = list()
        functions.append( self.__plot_line1 )
        functions.append( self.__plot_bars1 )
        return functions
    
    def __plot_bars1( self ):
        bars = np.array([10,20,30,25,40])
        text = 'Bar Plot'
        xlabels = ['a','b','c','d','e']
        self._plot_bars( bars, text, xlabels ) 

    def __plot_line1( self ):
        x = [0,1,2,3,4,5,6]
        y = np.ones(len(x))*4
        params = { 'color' : 'red' }
        label = 'Threshold'
        self._plot_line( x, y, label, params )