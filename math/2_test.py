#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

def loaddataSet(fileName):
    file=open(fileName)
    dataMat=[]
    for line in file.readlines():
        line=line.rstrip("\n")
        dataMat.append(line)
    return dataMat

data = loaddataSet('tsst.txt')
y = [float(x) for x in data]
#i=0.00
#x = []
#while i<6.27:
#    x.append(i)
#    i=i+0.01
#    pass
#colors = x
x=np.arange(0,2*np.pi, np.pi/0.005)
colors = x

ax = plt.subplot(111, projection='polar')
ax.scatter(x, y, c=colors, s = 10, cmap='hsv', alpha=0.75)
plt.show()


