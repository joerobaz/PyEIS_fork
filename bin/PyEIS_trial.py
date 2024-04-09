#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Wrapper to test and troubleshoot
'''

import sys
sys.path.append('/Users/joeyr/Code/PyEIS_fork/')
from PyEIS import *


ex4 = EIS_exp(path='https://raw.githubusercontent.com/kbknudsen/PyEIS/master/Tutorials/data/', data=['ex1.mpt','ex2.mpt'], cycle=[2,4])

ex4.EIS_plot(legend='potential', bode='log_im')

#ex4.Lin_KK(legend='potential')


print(ex4.KK_circuit_fit)