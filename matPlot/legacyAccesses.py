#!/usr/bin/env python

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from itertools import groupby



def test_table():
    data_table = pd.DataFrame({'Bench':['Add']*2 + ['Binarization']*2 + ['Convolution']*2 + ['DES']*2 + ['Histogram']*2 + ['Matrix multiplication']*2 + ['Matrix transpose']*2 + ['YUV2RGB']*2,
                               'Pipeline':(['4-stage'] + ['5-stage'])*8,
                               'Avoided writes':[0.4910891089,0.5227722772,0.499968752,0.499968752,0.572576577,0.5960394646,0.7228608999,0.7493289378,0.6665798724,0.6665798724,0.5792775988,0.5575716466,0.5212464589,0.5439093484,0.5350486076,0.5490826694],
                               'Remaining writes':[0.5089108911,0.4772277228,0.500031248,0.500031248,0.427423423,0.4039605354,0.2745352047,0.2497459085,0.3334201276,0.3334201276,0.4207224012,0.4424283534,0.4787535411,0.4560906516,0.4649513924,0.4509173306],
                               'Avoided reads':[0.7605633803,0.7887323944,0.4997397189,0.4997397189,0.6914525217,0.7256827504,0.8859644216,0.8979161811,0.6359119943,0.6359119943,0.8243277205,0.7921588339,0.7573964497,0.7573964497,0.723820162,0.6970120078],
                               'Remaining reads':[0.2394366197,0.2112676056,0.5002602811,0.5002602811,0.3085474783,0.2743172496,0.1138584322,0.1031094121,0.3640880057,0.3640880057,0.1756722795,0.2078411661,0.2426035503,0.2426035503,0.276179838,0.3029879922]
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
plt.title('Register File Accesses with Explicit Bypassing (Legacy Compiler)')
plt.show()