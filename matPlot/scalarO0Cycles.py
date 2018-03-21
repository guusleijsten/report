#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

fourStImp = (235.9322742,564.2585551,350.5401597,106.4496464,176.1324845,607.8763245,145.5056499,384.9740933)
fourStExp = (241.0430602,564.2585551,350.5401597,106.4496464,175.5639547,607.7501337,145.5056499,383.9793282)
fiveStImp = (248.4218227,669.9619772,422.7672374,133.4272708,177.7758327,663.2356616,166.685753,473.0569948)
fiveStExp = (252.2358569,669.9619772,422.7672374,133.3983528,177.1767277,663.1063168,166.685753,470.6185567)

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
plt.title('Scalar (-O0) Performance Compared to Legacy compiler')
plt.xticks(np.arange(0, 900, 100))
plt.yticks(ind, ('YUV2RGB', 'Matrix transpose', 'Matrix mul', 'Histogram', 'DES', 'Convolution', 'Binarization', 'Addition'))
#plt.xticks(rotation=45)
plt.grid()
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('4-stage - Implicit', '4-stage - Explicit', '5-stage - Implicit', '5-stage - Explicit'))

plt.show()
