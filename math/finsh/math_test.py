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

data = loaddataSet('tsst.txt')
y = [float(x) for x in data]
i = 0.00
x = []
while i<6.27:
    x.append(i)
    i = i+0.01
    pass
plt.plot(x, y, 'ro')

x0 = 3.14
y0 = 2.413
plt.scatter(x0, y0,s=75, color='k')
plt.plot([x0, x0],[y0, 0], 'b--', lw=2.5)
plt.annotate(r'$X = 3.14\  Y = %s$'%y0, xy=(x0,y0), xycoords='data', xytext=(+30,-30),textcoords='offset points', fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3, rad=.2'))

plt.text(1, -0.25, r'$This\ is\ the\ mid\ print.\ \mu\ \sigma_X\ \alpha_Y$',fontdict={'size':16, 'color':'g'})

plt.figure()
data = loaddataSet('fileY.txt')
y = [float(i) for i in data]
data = loaddataSet('fileX.txt')
x = [float(i) for i in data]
plt.plot(x, y, 'go')

plt.show()
