#!/usr/bin/env python2

from lib.tools.HistTool import HistTool

DESCRIPTION = """Create a histogram"""

if __name__ == '__main__':
    
    tool = HistTool(DESCRIPTION)
    tool.run()
