#!/usr/bin/env python2

from lib.tools.SequencePlotTool import SequencePlotTool

DESCRIPTION = """Creates a simple vertical line plot of a given sequence."""

if __name__ == '__main__':
    
    tool = SequencePlotTool(DESCRIPTION)
    tool.run()
