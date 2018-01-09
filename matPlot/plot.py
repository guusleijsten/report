#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt
writeSaves = (0.441014333, 0.3258047547, 0.5182186235, 0.4334621756, 0.05267489712, 0.2990750257)
writeAcc = (0.558985667, 0.7089477525, 0.4817813765, 0.5670900055, 0.9473251029, 0.7009249743)
readSaves = (0.3619791667, 0.389875872, 0.3431372549, 0.417721519, 0.4533538936, 0.2738666667)
readAcc = (0.6380208333, 0.6532844408, 0.6568627451, 0.5827004219, 0.5466461064, 0.7261333333)
N = 6
#menMeans = (20, 35, 30, 35, 27)
#womenMeans = (25, 32, 34, 20, 25)
#menStd = (2, 3, 4, 1, 2)
#womenStd = (3, 5, 2, 3, 3)
ind = 2*np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind + 0.00, writeAcc, width)#, yerr=menStd)
p2 = plt.bar(ind + 0.00, writeSaves, width, color='#d62728', bottom=writeAcc)
#             bottom=menMeans, yerr=womenStd)
p3 = plt.bar(ind + 0.5, readAcc, width, color='y')#, yerr=menStd)
p4 = plt.bar(ind + 0.5, readSaves, width, color='#d62728', bottom=readAcc)

plt.ylabel('Write accesses normalized to standard bypassing')
plt.title('Writes with explicit bypassing')
plt.xticks(ind, ('Binarization', 'Histogram', 'Addition', 'Matrix mul', 'Matrix transpose', 'Color conversion'))
plt.yticks(np.arange(0, 1.1, 0.1))
#plt.xticks(rotation=45)
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Write accesses', 'Writes avoided', 'Read accesses', 'Reads avoided'))

plt.show()
