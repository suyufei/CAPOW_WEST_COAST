# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:20:03 2018

@author: sdenaro
"""
import sys
import os
sys.path.append('Willamette/')
import Willamette_model as inner #reading in the inner function
#import time
initial_doy=1 #Set the simulation initial_doy
sys.argv = ["Willamette/settings.xml", str(initial_doy)] #simulation inputs
#starttime = time.time()
os.system("python Willamette/Willamette_outer.py")
#elapsed = time.time() - starttime
