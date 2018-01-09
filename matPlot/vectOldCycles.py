#!/usr/bin/env python

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from itertools import groupby

def test_table():
    data_table = pd.DataFrame({'Bench':['Add']*4 + ['Binarization']*4 + ['Histogram']*4 + ['Matrix multiplication']*4 + ['Matrix transpose']*4 + ['YUV2RGB']*4,
                               'Pipeline':(['4-stage']*2 + ['5-stage']*2)*6,
                               'Bypass':(['implicit'] + ['explicit'])*12,
                               'Cycles':[49,49,54,54,2018,2019,2614,2616,22237,24799,22551,23449,322,323,337,341,274,275,273,275,1404,1405,1862,1866],
                               #'Accesses avoided':[0.3431372549,0.5182186235,0.3799019608,0.5182186235,0.3619791667,0.441014333,0.5065827546,0.4980842912,0.389875872,0.3258047547,0.4449221448,0.6133431626,0.417721519,0.4334621756,0.5755274262,0.6598821639,0.4533538936,0.05267489712,0.3577486507,0.0845410628,0.2738666667,0.2990750257,0.3026,0.2786228983],
                               #'Remaining accesses':[0.6568627451,0.4817813765,0.6200980392,0.4817813765,0.6380208333,0.558985667,0.4934172454,0.5019157088,0.6532844408,0.7089477525,0.5607805574,0.3909459505,0.5827004219,0.5670900055,0.4244725738,0.3401178361,0.5466461064,0.9473251029,0.6422513493,0.9154589372,0.7261333333,0.7009249743,0.6974,0.7213771017]
                               })
    return data_table

def add_line(ax, xpos, ypos):
    line = plt.Line2D([xpos, xpos], [ypos + .1, ypos],
                      transform=ax.transAxes, color='black')
    line.set_clip_on(False)
    ax.add_line(line)

def label_len(my_index,level):
    labels = my_index.get_level_values(level)
    return [(k, sum(1 for i in g)) for k,g in groupby(labels)]

def label_group_bar_table(ax, df):
    ypos = -.1
    scale = 1./df.index.size
    for level in range(df.index.nlevels)[::-1]:
        pos = 0
        for label, rpos in label_len(df.index,level):
            lxpos = (pos + .5 * rpos)*scale
            ax.text(lxpos, ypos, label, ha='center', transform=ax.transAxes)
            add_line(ax, pos*scale, ypos)
            pos += rpos
        add_line(ax, pos*scale , ypos)
        ypos -= .1


#continue found code
df = test_table().groupby(['Bench','Pipeline','Bypass']).sum()
fig = plt.figure()
ax = fig.add_subplot(111)
df.plot(kind='bar',stacked=True,color=['b','#d62728'],ax=fig.gca())
#Below 3 lines remove default labels
labels = ['' for item in ax.get_xticklabels()]
ax.set_xticklabels(labels)
ax.set_xlabel('')
label_group_bar_table(ax, df)
fig.subplots_adjust(bottom=.1*df.index.nlevels)
plt.ylabel('Accesses to the RF normalized to standard bypassing')
plt.title('Register Accesss Improvements with explicit bypassing (Vector version)')
plt.show()

writeSaves = (0.441014333, 0.3258047547, 0.5182186235, 0.4334621756, 0.05267489712, 0.2990750257)
writeAcc = (0.558985667, 0.7089477525, 0.4817813765, 0.5670900055, 0.9473251029, 0.7009249743)
readSaves = (0.3619791667, 0.389875872, 0.3431372549, 0.417721519, 0.4533538936, 0.2738666667)
readAcc = (0.6380208333, 0.6532844408, 0.6568627451, 0.5827004219, 0.5466461064, 0.7261333333)
#N = 6
##menMeans = (20, 35, 30, 35, 27)
##womenMeans = (25, 32, 34, 20, 25)
##menStd = (2, 3, 4, 1, 2)
##womenStd = (3, 5, 2, 3, 3)
#ind = 2*np.arange(N)    # the x locations for the groups
#width = 0.35       # the width of the bars: can also be len(x) sequence

#p1 = plt.bar(ind + 0.00, writeAcc, width)#, yerr=menStd)
#p2 = plt.bar(ind + 0.00, writeSaves, width, color='#d62728', bottom=writeAcc)
#             bottom=menMeans, yerr=womenStd)
#p3 = plt.bar(ind + 0.5, readAcc, width, color='y')#, yerr=menStd)
#p4 = plt.bar(ind + 0.5, readSaves, width, color='#d62728', bottom=readAcc)

#plt.ylabel('Write accesses normalized to standard bypassing')
#plt.title('Writes with explicit bypassing')
#plt.xticks(ind, ('Binarization', 'Histogram', 'Addition', 'Matrix mul', 'Matrix transpose', 'Color conversion'))
#plt.yticks(np.arange(0, 1.1, 0.1))
##plt.xticks(rotation=45)
#plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Write accesses', 'Writes avoided', 'Read accesses', 'Reads avoided'))

#plt.show()
