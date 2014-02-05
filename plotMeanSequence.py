#!/usr/bin/env python2

from lib.PlotMeanSequence import PlotMeanSequence

DESCRIPTION = """Creates a plot showing a sequence of mean values and
its corresponding standard deviations. Supply the sequence of mean
values on the first line and the sequence of standard deviations on
the second line.
"""

if __name__ == '__main__':
    
    tool = PlotMeanSequence(DESCRIPTION)
    tool.run()
