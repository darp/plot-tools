#!/usr/bin/env python2

from lib.tools.HistogramTool3D import HistogramTool3D

DESCRIPTION = """ Plot a 3D histogram. """

if __name__ == '__main__':
    
    tool = HistogramTool3D(DESCRIPTION)
    tool.run()
