#!/usr/bin/env python
# -*- coding: utf8 -*-

#from __future__ import division
import numpy as np
import os
from glob import glob
import sys

#TODO: Give an error if wrong inputs
#TODO: Give minimum two inputs
#TODO: Exit if len(tmpFiles) != N

## Number of pictures for every HDR
N = int(sys.argv[1])
## jpg, JPG, png, etc.
imgType = sys.argv[2]
files = glob("*"+imgType)
files = np.sort(files)


for i in xrange(0, len(files), N):
    cmd = "luminance-hdr-cli -v -o HDR"+str(i+1)+".jpg "
    tmpFiles = files[i:i+N]
    if len(tmpFiles) != N:
        print "Number of files does not match with", N, "files per HDR."
        SystemExit
    for file in tmpFiles:
        cmd += str(file)+" "
    
    os.system(cmd)
#    print i, cmd

