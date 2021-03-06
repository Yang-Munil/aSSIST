#!/usr/bin/env python
# coding: utf-8

# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Set graph size and dpi
plt.rc(group = 'figure', figsize = (6, 6), dpi = 100)

# Set line width and style
plt.rc(group = 'lines', linewidth = 0.5, linestyle = '-')

# Set Korean font and size
plt.rc(group = 'font', family = 'Gamja Flower', size = 10)

# Set not to use unicode minus code
plt.rc(group = 'axes', unicode_minus = False)
