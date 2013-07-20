#!/usr/bin/env python
# -*- coding: utf8 -*-

import numpy as np
import os
import sys
from glob import glob

## Number of pictures for every HDR
N = sys.argv[1]
## jpg, JPG, png, etc.
imgType = sys.argv[2]

cmdHDR = "python hdr.py "+N+" "+imgType
os.system(cmdHDR)

cmdTimelapse = "./timelapse.sh"
os.system(cmdTimelapse)
