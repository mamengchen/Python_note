#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import string
import numpy as np
def loaddataSet(fileName):  
    file=open(fileName)  
    dataMat=[]
    for line in file.readlines():
        line=line.rstrip("\n")
        dataMat.append(line)  
    return dataMat

data = loaddataSet('text.txt')
y = [float(x) for x in data]
datalen = len(y)
while datalen < 10000:
    y.append(0.0)
    datalen=datalen+1
    pass

i = 0.0
x = []
while i<100:
    x.append(i)
    i=i+0.01
    pass
plt.plot(x,y,)
plt.show()
