#!/usr/bin/env python

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from itertools import groupby



def test_table():
    data_table = pd.DataFrame({'Bench':['Add']*2 + ['Binarization']*2 + ['DES']*2 + ['Convolution']*2 + ['Histogram']*2 + ['Matrix mul']*2 + ['Matrix transpose']*2 + ['YUV2RGB']*2,
                               'Pipeline':(['4-stage'] + ['5-stage'])*8,
                               #'Accesses':(['writes'] + ['reads'])*16,
                               'Avoided writes':[0.3063829787,
0.40625,
0.1997752528,
0.6661115737,
0.3925897176,
0.4113347389,
0.8286943262,
0.6496284325,
0.5698386199,
0.6655112652,
0.5389473684,
0.3331640427,
0.3333333333,
0.5377358491,
0.1882147914,
0.2513089005],
                               'Remaining writes':[0.6936170213,
0.59375,
0.8002247472,
0.3338884263,
0.6074197488,
0.5922317473,
0.2168233232,
0.3978827223,
0.4301613801,
0.3344887348,
0.4610526316,
0.6668359573,
0.6666666667,
0.4622641509,
0.8117852086,
0.7486910995],
                               'Avoided reads':[0.201754386,
0.2346491228,
0.2223764575,
0.5554553026,
0.3168717983,
0.3715426985,
0.5225472445,
0.405304784,
0.4167750325,
0.6662873862,
0.4082914573,
0.2326826196,
0.3858921162,
0.3153526971,
0.4199551274,
0.3403897254],
                               'Remaining reads':[0.798245614,
0.7653508772,
0.7776235425,
0.4445446974,
0.6831348546,
0.636038194,
0.5057428992,
0.6835744599,
0.5832249675,
0.3337126138,
0.5917085427,
0.7673173804,
0.6141078838,
0.6846473029,
0.5800448726,
0.6596102746]
                               }, columns=['Bench','Pipeline','Remaining writes','Remaining reads','Avoided writes','Avoided reads'])
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
df = test_table().groupby(['Bench','Pipeline']).sum()
fig = plt.figure()
ax = fig.add_subplot(111)
df.plot(kind='bar',stacked=True,color=['#3669c9', '#1d9524', '#d62728', '#fd9827'],ax=fig.gca())
#Below 3 lines remove default labels
labels = ['' for item in ax.get_xticklabels()]
ax.set_xticklabels(labels)
ax.set_xlabel('')
label_group_bar_table(ax, df)
fig.subplots_adjust(bottom=.1*df.index.nlevels)
#Bewlow 2 lines rescale y-axes
ticks = ax.get_yticks()/2
ax.set_yticklabels(ticks)
plt.ylabel('Accesses to the RF normalized to standard bypassing')
plt.title('Register File Accesses with Explicit Bypassing (Scalar version)')
plt.show()
