#!/usr/bin/env python

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from itertools import groupby

def test_table():
    data_table = pd.DataFrame({'Bench':['Add']*2 + ['Binarization']*2 + ['Histogram']*2 + ['Matrix multiplication']*2 + ['Matrix transpose']*2 + ['YUV2RGB']*2,
                               'Pipeline':(['4-stage'] + ['5-stage'])*6,
                               'Avoided writes':[0.5182186235,0.5182186235,0.441014333,0.4980842912,0.08880785459,0.5038971716,0.4334621756,0.6598821639,0.05267489712,0.0845410628,0.2990750257,0.2786228983],
                               'Remaining writes':[0.4817813765,0.4817813765,0.558985667,0.5019157088,0.9132574444,0.4961028284,0.5670900055,0.3401178361,0.9473251029,0.9154589372,0.7009249743,0.7213771017],
                               'Avoided reads':[0.3431372549,0.3799019608,0.3619791667,0.5065827546,0.5449868052,0.627418158,0.417721519,0.5755274262,0.4533538936,0.3577486507,0.2738666667,0.3026],
                               'Remaining reads':[0.6568627451,0.6200980392,0.6380208333,0.4934172454,0.4592620869,0.372581842,0.5827004219,0.4244725738,0.5466461064,0.6422513493,0.7261333333,0.6974]
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
ticks = ax.get_yticks()/2
ax.set_yticklabels(ticks)
plt.ylabel('Accesses to the RF normalized to standard bypassing')
plt.title('Register File Accesses with Explicit Bypassing (Vector version)')
plt.show()

