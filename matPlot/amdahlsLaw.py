#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

def f1(t):
    return (1.0*N)/(0.05*N+(1.0-0.05))

def f2(t):
    return (1.0*N)/(0.1*N+(1.0-0.1))

def f3(t):
    return (1.0*N)/(0.25*N+(1.0-0.25))

def f4(t):
    return (1.0*N)/(0.5*N+(1.0-0.5))

#N = np.arange(1, 2, 4, 8, 16, 32)
#B = np.arange(0.05, 0.1, 0.25, 0.5)
N = np.arange(1.0, 32.0, 0.1)

#N = 32

#AX = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
#AX = [1, 2, 4, 8, 16, 32, 64, 128, 256]
AX = [1, 2, 4, 8, 16, 32, 64, 128]


ind = 2*np.arange(32)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

plt.plot(N, f1(N), 'black', N, f2(N), 'black', N, f3(N), 'black', N, f4(N), 'black')

#p1 = plt.bar(ind + 0.00, writeAcc, width)#, yerr=menStd)
#p2 = plt.bar(ind + 0.00, writeSaves, width, color='#d62728', bottom=writeAcc)
#             bottom=menMeans, yerr=womenStd)
#p3 = plt.bar(ind + 0.5, readAcc, width, color='y')#, yerr=menStd)
#p4 = plt.bar(ind + 0.5, readSaves, width, color='#d62728', bottom=readAcc)

plt.ylabel('Speedup (S)')
plt.xlabel('Number of Processors (N)')
plt.title("Amdahl's Law")
plt.xscale('log', basex=2, linthreshy=0.05)
plt.xticks(AX, AX)
plt.yticks(np.arange(0, 22, 1),np.arange(0, 21, 1))

plt.axhline(y=10, color='black', dashes=[10, 5, 10, 5])
plt.axhline(y=20, color='black', dashes=[10, 5, 10, 5])
#plt.xticks(rotation=45)
#plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Write accesses', 'Writes avoided', 'Read accesses', 'Reads avoided'))

plt.show()
