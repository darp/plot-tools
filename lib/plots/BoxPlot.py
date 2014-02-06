from lib.plots.AbstractPlot import AbstractPlot
import pylab

class BoxPlotExample( AbstractPlot ):

    def __init__( self ):
        params = dict()
        params['xlim'] = [0,4]
        params['ylim'] = [1,1000]
        params['ylog'] = True
        params['grid_linewidth'] = 1.5
        params['xlabel'] = 'xlabel'
        params['ylabel'] = 'ylabel'
        AbstractPlot.__init__( self, params )

    def registerPlottingFunctions( self ):
        functions = list()
        functions.append( self.__plot_boxplot1 )
        return functions

    def __plot_boxplot1( self ):
        data = self.__fake_boxplot_data()
        label = 'My Boxes'
        xlabels = ['a','b','c']
        self._plot_boxplot(data, label, xlabels )

    def __fake_boxplot_data( self ):
        spread = pylab.rand(50) * 100
        center = pylab.ones(25) * 50
        flier_high = pylab.rand(10) * 100 + 100
        flier_low = pylab.rand(10) * -100
        data = pylab.concatenate( (spread, center, flier_high, flier_low), 0 )

        spread = pylab.rand(50) * 100
        center = pylab.ones(25) * 40
        flier_high = pylab.rand(10) * 100 + 100
        flier_low = pylab.rand(10) * -100
        d2 = pylab.concatenate( (spread, center, flier_high, flier_low), 0 )
        data.shape = (-1, 1)
        d2.shape = (-1, 1)
        data = [ data, d2, d2[::2,0] ]

        return data
