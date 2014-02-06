#!/usr/bin/env python2

from lib.ScatterPlotTool import ScatterPlotTool

DESCRIPTION = """Creates a 2D scatter-plot. Each line is expected to
contain a data point in the format 'xValue yValue'."""

if __name__ == '__main__':
    tool = ScatterPlotTool(DESCRIPTION)
    tool.run()
    
