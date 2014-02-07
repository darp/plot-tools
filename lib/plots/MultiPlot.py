from lib.plots.AbstractPlot import AbstractPlot

class MultiPlot(AbstractPlot):
    
    def __init__(self, X, Y):
        
        self.X = X
        self.Y = Y
        self.tmp = 0
        
        AbstractPlot.__init__(self)

    def registerPlottingFunctions( self ):
        functions = list()
        for i in range(len(self.X)):
            functions.append(self._multi_plot)
        return functions

    def _multi_plot(self):
        pass