#!/usr/bin/env python
"""
Script to open portions of big files.
In particular, this script has been designed to open big output files from sequencing projects or microarrays.
If the file has more than 1000 lines, only the first 1000 are showed
If the file has more than 100 bytes, cut it
In bash it would be "head -n1000 | (cut -f 18)|cut -b100"

>>> files = os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'] = '/proc/cpuinfo\\n/proc/meminfo'
>>> openbigfiles(files, 10, 10)

"""

import sys
import os
import logging
logging.basicConfig(filename = '/tmp/open_big_files.log', level = logging.ERROR)

def openbigfiles(files = '', rowlimit = 100, byteslimit = 100):
    """ """
    tmpfiles = ''
    for filename in files.split('\n'):
        output = ''
        
        f = file(filename, 'r')
        for n in range(rowlimit):
            line = f.readline()
            if line is None:
                break
            output += line[:byteslimit].strip() + '\n'
#            if line[100]:
#                output += '...\n'
#            else:
#                output += '\n'
        if f.readline():
            output += '\n....\nfile continues'
        
        # write the output to a temporary file and open it with gedit 
        tmpfilename = '/tmp/cutted_' + filename.split('/')[-1].strip()
        tmpfiles += ' ' + tmpfilename 
        logging.debug(tmpfilename)
        tmpfile = file(tmpfilename, 'w')
        tmpfile.write(output)
#        tmpfile.close()

    os.popen('/usr/bin/gedit %s' % (tmpfiles))     # TODO: change with sensible browser


def _test():
    import doctest
    doctest.testmod()
    
if __name__ == '__main__':
#    _test()
    files = os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS']
    openbigfiles(files)