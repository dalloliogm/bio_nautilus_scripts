#!/usr/bin/env bash
# Script to open portions of big files.
# In particular, this script has been designed to open big output files from sequencing projects or microarrays.
# If the file has more than 1000 lines, only the first 1000 are showed
# If the file has more than 18 columns or 1000 bytes, cut it

head -n 1000 $1 |cut -f 1-18|cut -b 1000