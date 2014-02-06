from lib.plots.AbstractPlot import AbstractPlot
import numpy as np

class LinePlot(AbstractPlot):

    def __init__( self ):
        params = dict()
        params['xlim'] = [0,5]
        params['ylim'] = [0,20]
        params['xlabel'] = 'xlabel'
        params['ylabel'] = 'ylabel'
        AbstractPlot.__init__( self, params )

    def registerPlottingFunctions( self ):
        functions = list()
        functions.append( self.__plot_scatter1 )
        functions.append( self.__plot_line1 )
        functions.append( self.__plot_line2 )
        functions.append( self.__plot_text1 )
        return functions

    def __plot_text1( self ):
        x,y = 2.2,10
        text = 'text'
        self._plot_text( x, y, text )

    def __plot_scatter1( self ):
        x = np.linspace(0,10,100)
        y = x**2 + 3
        m = (y + np.random.randn(1,100)*3)[0]
        params = { 'color' : 'gray' }
        label = 'label'
        self._plot_scatter( x, m, label, params )

    def __plot_line1( self ):
        x = np.linspace(0,10,100)
        y = x**2 + 3
        self._plot_line( x, y, 'line 1' )

    def __plot_line2( self ):
        x = np.linspace(0,10,100)
        y = x**2 + 10
        params = { 'linestyle' : '--' }
        self._plot_line( x, y, 'line 2', params )