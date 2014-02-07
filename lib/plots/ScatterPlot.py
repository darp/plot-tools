

from lib.plots.MultiPlot import MultiPlot

class ScatterPlot(MultiPlot):

    def __init__(self, X, Y):
        MultiPlot.__init__(self, X, Y)
    

    def _multi_plot(self):
        
        X = self.X.pop()
        Y = self.Y.pop()
        
        params = dict()
        params['xlim'] = [min(X), max(X)]
        params['ylim'] = [min(Y), max(Y)]
        params['legend_location'] = 2
        self.setPlottingParams(params)
        
        # This isn't final yet.
        if self.tmp == 0:
            self._plot_scatter(X, Y, '',  { 'dotsize' : 30, 'color': 'b'})
            self.tmp = 1
        else:
            self._plot_scatter(X, Y, '',  { 'dotsize' : 30, 'color': 'r'})
