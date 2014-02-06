'''
    Created on 2013-03-15
    
    Abstract Base Class for Plots
    
    @author: darp, fabs
'''

import pylab
import abc


from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Polygon
import numpy as np


class AbstractPlot:
    '''
        abstract class with default values for plots
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, params=dict()):
        
        self._initializePlottingParams(params)
        self._initializeFigure()
        self.__functions = self.registerPlottingFunctions()
        

    @abc.abstractmethod
    def registerPlottingFunctions( self ):
        '''
            this method has to be implemented by all subclasses. the method
            returns a list of functions which add plots to the figure.
        '''
        return

    def _initializePlottingParams(self, params):
        self._setPlottingParamsToDefault()
        
        for key, val in params.items():
            self.__params[key] = val

    def _setPlottingParamsToDefault(self):
        self.__params = { #save figure in path
                        'path' : './',
                        'figsize' : (6,6), 
                        'fontsize' : 16,
                        'xlabel' : '',
                        'ylabel' : '',
                        'grid' : True,
                        'grid_linewidth' : 1.0,
                        # axis parameters
                        'xlim' : [0,100],
                        'ylim' : [0,100],
                        'xlog' : False,
                        'ylog' : False,
                        'axisbelow' : True,
                        'ticksize' : 14,
                        # legend parameters
                        'legend_scatterpoints' : 1,
                        'legend_location' : 4 }
        
      
    def _initializeFigure(self):
        pylab.figure(figsize=self.__params['figsize'])
        self.__ax = pylab.subplot(111)
        
    def __call__(self, filename = ''):
        self._executePlotFunctions()
        self._finishPlot()
        self.showOrSavePlot(filename)
    
    def _executePlotFunctions(self):
        for function in self.__functions:
            function()
     
    def _finishPlot(self):
        
        self._setLegendParameters()
        self._setLabels()
        self._set_axis_parameter()
        
        pylab.grid( self.__params['grid'], linewidth= self.__params['grid_linewidth'] )
        pylab.tight_layout()
 

    def showOrSavePlot(self, filename):
        if filename == '':
            pylab.show()
        else:
            self._save_plot( filename )
    
    # The following are plotting functions that may come in handy
    # We might want to place this in a sep. class.
    
    def _setLegendParameters(self):
    
        if len(self.__functions) > 1:
            pylab.legend( loc = self.__params['legend_location'],
                        scatterpoints = self.__params['legend_scatterpoints'] )
            pylab.rc('legend', **{'fontsize':self.__params['fontsize']})
    
    def _setLabels(self):
        # set labels
        pylab.ylabel( self.__params['ylabel'], fontsize=self.__params['fontsize'] )
        pylab.xlabel( self.__params['xlabel'], fontsize=self.__params['fontsize'] )
    
    
    def _set_axis_parameter( self ):
        # set axis to equal length
        params = self.__params
        ax_0 = self._get_axis()
        # set axis aspect 
        pylab.xlim(params['xlim'])
        pylab.ylim(params['ylim'])
        x0,x1 = ax_0.get_xlim()
        y0,y1 = ax_0.get_ylim()
        if params['xlog'] and params['ylog']:
            delta_x = float(np.log(x1)-np.log(x0))
            delta_y = float(np.log(y1)-np.log(y0))
        else:
            delta_x = float(x1 - x0)
            delta_y = float(y1 - y0)
        ax_0.set_aspect(delta_x/delta_y)
        # set tick size
        ax_0.tick_params(axis='both', labelsize=params['ticksize'])
        # set logarithmic scale
        if params['xlog']:
            pylab.xscale('log')
            if params['grid']:
                ax_0.xaxis.grid( True, which='both' )
        if params['ylog']:
            pylab.yscale('log')
            if params['grid']:
                ax_0.yaxis.grid( True, which='both' )
        # grid below bars and boxes
        ax_0.set_axisbelow(params['axisbelow'])
    
    def _get_axis( self ):
        return self.__ax
    
    def _save_plot( self, filename ):
        path = self.__params['path']
        savepath = '{}/{}'.format(path,filename)
        pp = PdfPages( savepath )
        pp.savefig()
        pp.close()
    
    def _plot_line( self, x, y, label, params=dict() ):
        fparams = { 'color' : 'black',
                    'linestyle' : 'solid',
                    'linewidth' : 2.0 }
        fparams.update( params )
    
        pylab.plot( x, y, 
                color = fparams['color'],
                linestyle = fparams['linestyle'],
                linewidth = fparams['linewidth'],
                label = label )
    
    def _plot_scatter( self, x, y, label, params=dict() ):
        fparams = { 'dotsize' : 30,
                    'color' : 'black' }
        fparams.update( params )
        pylab.scatter( x, y, 
                s = fparams['dotsize'],
                color = fparams['color'],
                label = label )
    
    def _plot_text( self, x, y, text, params=dict() ):
        fparams = { 'fontsize' : self.__params['fontsize'] }
        fparams.update( params )
        pylab.text( x, y, text, fontsize=fparams['fontsize'] )
    
    def _plot_bars( self, vals, text, xlabels, params=dict() ):
        fparams = { 'bar_width' : 0.5,
                    'facecolor' : '#BBBBBB',
                    'edgecolor' : '#000000' }
        fparams.update( params )
    
        bar_width = fparams['bar_width']
        xloc = np.array(range(len(vals))) + bar_width
        pylab.xticks( xloc )
        self.__ax.set_xticklabels( xlabels )
        pylab.bar( xloc, vals, 
                yerr=fparams['yerr'],
                width=bar_width, 
                facecolor=fparams['facecolor'],
                ecolor=fparams['edgecolor'],
                label=text,
                align='center')
    
    def _plot_boxplot( self, data, text, xlabels, params=dict() ):
        fparams = { 'color' : '#000000',
                    'facecolor' : '#FFFFFF',
                    'linewidth' : 2.0,
                    'alpha' : 1.0,
                    'notched_plot' : 0,
                    'show_outliers' : '' }
        fparams.update( params )
        self.__ax.set_xticklabels( xlabels )
        bp = pylab.boxplot( data, 
                            fparams['notched_plot'], 
                            fparams['show_outliers'] )
    
        # customize boxplot color and linewidth
        for item in bp.values():
            pylab.setp(item, 
                    color=fparams['color'],
                    linewidth=fparams['linewidth'])
    
        numBoxes = len(bp['boxes'])
        medians = range(numBoxes)
        for i in range(numBoxes):
            box = bp['boxes'][i]
            boxX = []
            boxY = []
            for j in range(5):
                boxX.append(box.get_xdata()[j])
                boxY.append(box.get_ydata()[j])
            boxCoords = zip(boxX,boxY)
    
            boxPolygon = Polygon( boxCoords, 
                                facecolor=fparams['facecolor'], 
                                linewidth=fparams['linewidth'], 
                                alpha=fparams['alpha'] )
            self.__ax.add_patch(boxPolygon)
            # Now draw the median lines back over what we just filled in
            med = bp['medians'][i]
            medianX = []
            medianY = []
            for j in range(2):
                medianX.append(med.get_xdata()[j])
                medianY.append(med.get_ydata()[j])
                pylab.plot( medianX, medianY, fparams['color'] )
                medians[i] = medianY[0]
        
