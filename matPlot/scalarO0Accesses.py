#!/usr/bin/env python

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from itertools import groupby



def test_table():
    data_table = pd.DataFrame({'Bench':['Add']*2 + ['Binarization']*2 + ['DES']*2 + ['Convolution']*2 + ['Histogram']*2 + ['Matrix mul']*2 + ['Matrix transpose']*2 + ['YUV2RGB']*2,
                               'Pipeline':(['4-stage'] + ['5-stage'])*8,
                               #'Accesses':(['writes'] + ['reads'])*16,
                               'Avoided writes':[0.579787234,
0.691369606,
0.8884108258,
0.8996189643,
0.4414904449,
0.7453087305,
0.573243298,
0.5939090001,
0.9076732235,
0.9989497374,
0.4918862161,
0.7225153533,
0.5122470714,
0.6077844311,
0.5838449111,
0.6144155437],
                               'Remaining writes':[0.420212766,
0.308630394,
0.1115891742,
0.1003810357,
0.5585095551,
0.2546912695,
0.426756702,
0.4060909999,
0.09232677654,
0.001050262566,
0.5081137839,
0.2774846467,
0.4877529286,
0.3922155689,
0.4161550889,
0.3855844563],
                               'Avoided reads':[0.3751529988,
0.5312117503,
0.5999417007,
0.6665695011,
0.3397061077,
0.5213488295,
0.3348346939,
0.3829051804,
0.6108763948,
0.7773805655,
0.3046072061,
0.493738925,
0.350955414,
0.4305732484,
0.4024574596,
0.4044831181],
                               'Remaining reads':[0.6248470012,
0.4687882497,
0.4000582993,
0.3334304989,
0.6602938923,
0.4786511705,
0.6651653061,
0.6170948196,
0.3891236052,
0.2226194345,
0.6953927939,
0.506261075,
0.649044586,
0.5694267516,
0.5975425404,
0.5955168819]
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
fig = plt.figure(figsize=(16.35, 10.35), dpi=80)
ax = fig.add_subplot(111)
plot = df.plot(kind='bar',stacked=True,color=['#3669c9', '#1d9524', '#d62728', '#fd9827'],ax=fig.gca())

handles, labels = ax.get_legend_handles_labels()
ax.legend(reversed(handles), reversed(labels), loc='upper right')  # reverse both handles and labels
#following two lines give custom vertical gridlines
for level in range(7):
  ax.axvline(2*level+1.5, linestyle='--', color='k')
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
plt.title('Register File Accesses with Explicit Bypassing (Scalar version - O0)')
plt.show()

figural = plot.get_figure()
figural.savefig("scalarO0_accesses.png", bbox_inches='tight', dpi=800)