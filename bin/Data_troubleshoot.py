# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import sys
# sys.path.append('/Users/joeyr/Code/PyEIS_fork/')
from PyEIS import *
from PyEIS.PyEIS_Data_extraction import *
# from PyEIS_Data_extraction import *


df1 = EIS_exp(path='/Users/joeyr/Documents/Data/AIM/20240321_ULD/',data=['Potentiostatic Impedance.z'])
# ex1 = EIS_exp(path='https://raw.githubusercontent.com/kbknudsen/PyEIS/master/Tutorials/data/', data=['ex1.mpt'])

# ex1.df_raw.head()

# path = '/Users/joeyr/Documents/Data/AIM/20240321_ULD/'
# file = 'Potentiostatic Impedance.z'


# dummy_col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J','K','L','M','N','O','P']
# init = pd.read_csv(path+file, encoding='latin1', sep=',', names=dummy_col)
# ZC = pd.Index(init.A)
# header_loc = ZC.get_loc('Frequency (Hz)')
# data = pd.read_csv(path+file,sep=',',header=header_loc)

# data = modulab_rename_columns(data)


fig = figure(dpi=90, facecolor='w', edgecolor='k')
fig.subplots_adjust(left=0.1, right=0.95, hspace=0.5, bottom=0.1, top=0.95)
ax = fig.add_subplot(111)

ax.plot(df1.df_raw.re, df1.df_raw.im, 'o--')

ax.set_xlabel("Z' [$\Omega$]")
ax.set_ylabel("-Z'' [$\Omega$]")