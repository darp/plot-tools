#!/usr/bin/env python2

from lib.tools.MeanSequencePlotTool import MeanSequencePlotTool

DESCRIPTION = """Creates a plot showing a sequence of mean values and
its corresponding standard deviations. Supply the sequence of mean
values on the first line and the sequence of standard deviations on
the second line.
"""

if __name__ == '__main__':
    
    tool = MeanSequencePlotTool(DESCRIPTION)
    tool.run()
