#!/usr/bin/env python2

from lib.tools.TimeSequencePlotTool import TimeSequencePlotTool

DESCRIPTION = """Creates a plot showing a sequence of measured 
values for a particular point in a discrete-time signal. Supply the 
sequence of measured values on the first line and the sequence of 
expected (or true) values on the second line.
"""

if __name__ == '__main__':
    
    tool = TimeSequencePlotTool(DESCRIPTION)
    tool.run()
