#!/usr/bin/env python

import sys
import os

filename = sys.argv
tmpfile = file('/tmp/cuttedfile', 'w')

tmpfile.write(str(filename) + '\n')
tmpfile.write(str(dir()) + '\n')
tmpfile.write(str(os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS']) + '\n')

os.popen('gedit /tmp/cuttedfile &')