#!/usr/bin/env python
# Script to open portions of big files.
# In particular, this script has been designed to open big output files from sequencing projects or microarrays.
# If the file has more than 1000 lines, only the first 1000 are showed
# If the file has more than 18 columns or 1000 bytes, cut it

import sys
import os

filename = sys.argv
tmpfile = file('/tmp/cuttedfile', 'w')


output = ''

for f in os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'].split('\n'):
    output += f

tmpfile.write(output)
os.popen('gedit /tmp/cuttedfile &')



if __name__ == '__main__':
    os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'] = '/proc/cpuinfo\n/proc/meminfo'