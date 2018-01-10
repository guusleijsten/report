#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

fourStImp = (8.381589159,146.5240642,15.21020312,150,12.5999001,14.75903614)
fourStExp = (8.387558952,146.2765957,15.2,150,12.60535681,14.75903614)
fiveStImp = (14.42292796,135.8208955,14.88515901,150,12.55885462,14.43850267)
fiveStExp = (14.4539117,136.8159204,15.04854369,150,12.56725596,14.43850267)

N = 6
ind = 2*np.arange(N)    # the x locations for the groups
width = 0.3       # the width of the bars: can also be len(x) sequence

plt.axvline(x=100, color='black', dashes=[10, 5, 10, 5])

p1 = plt.barh(ind + 0.45, fourStImp, width, color='#3669c9')#, yerr=menStd)
p2 = plt.barh(ind - 0, fourStExp, width, color='#1d9524')
#             bottom=menMeans, yerr=womenStd)
p3 = plt.barh(ind - 0.45, fiveStImp, width, color='#d62728')#, yerr=menStd)
p4 = plt.barh(ind - 0.9, fiveStExp, width, color='#fd9827')

plt.xlabel('Normalized runtime of Vector version w.r.t. Scalar version (%)')
plt.title('Vector Performance Compared to Scalar version')
plt.xticks(np.arange(0, 160, 10))
plt.yticks(ind, ('YUV2RGB', 'Matrix transpose', 'Matrix mul', 'Histogram', 'Binarization', 'Addition'))
#plt.xticks(rotation=45)
plt.grid()
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('4-stage - Implicit', '4-stage - Explicit', '5-stage - Implicit', '5-stage - Explicit'))

plt.text(150.5, 6 + 0.45, str(543.1), color='#3669c9', fontweight='bold')
plt.text(150.5, 6 - 0, str(547.6), color='#1d9524', fontweight='bold')
plt.text(150.5, 6 - 0.45, str(387.1), color='#d62728', fontweight='bold')
plt.text(150.5, 6 - 0.9, str(388.7), color='#fd9827', fontweight='bold')
#for i, v in enumerate(fourStImp):
#    plt.text(v + 3, 2*i + .45, str(v), color='blue', fontweight='bold')
#line below gives logaritmic scale! 
#plt.xscale('symlog', linthreshy=0.05)
plt.show()
