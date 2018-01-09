#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

fourStImp = (175.0731605,71.1026616,49.71817755,68.88563765,98.43158963,60.62907407,90.94316052,86.01036269)
fourStExp = (175.0731605,71.48288973,49.90605918,68.88563765,98.11478651,63.13276507,90.94883879,85.7881137)
fiveStImp = (134.9289298,76.42585551,52.38315595,88.94428788,101.3424241,93.97816559,108.3441778,96.89119171)
fiveStExp = (134.2554077,76.42585551,52.42943082,88.92501084,101.7079576,103.3647195,108.3545885,96.39175258)

N = 8
ind = 2*np.arange(N)    # the x locations for the groups
width = 0.3       # the width of the bars: can also be len(x) sequence

p1 = plt.barh(ind + 0.45, fourStImp, width, color='#3669c9')#, yerr=menStd)
p2 = plt.barh(ind - 0, fourStExp, width, color='#1d9524')
#             bottom=menMeans, yerr=womenStd)
p3 = plt.barh(ind - 0.45, fiveStImp, width, color='#d62728')#, yerr=menStd)
p4 = plt.barh(ind - 0.9, fiveStExp, width, color='#fd9827')

plt.axvline(x=100, color='black', dashes=[10, 5, 10, 5])

plt.xlabel('Normalized runtime of Scalar version w.r.t. Legacy compiler (%)')
plt.title('Scalar Performance Compared to Legacy compiler')
plt.xticks(np.arange(0, 160, 10))
plt.yticks(ind, ('YUV2RGB', 'Matrix transpose', 'Matrix mul', 'Histogram', 'DES', 'Convolution', 'Binarization', 'Addition'))
#plt.xticks(rotation=45)
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('4-stage - Implicit', '4-stage - Explicit', '5-stage - Implicit', '5-stage - Explicit'))

plt.show()
