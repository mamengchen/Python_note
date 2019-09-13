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

s2=3.14*(1.4**2)/4
data=loaddataSet('text.txt')
y=[float(i) for i in data]
datalen = len(y)
while datalen < 10000:
    y.append(0.0)
    datalen=datalen+1
    pass

judge = 1
length = 0
X0 = 0
Y0 = 0
X1 = 0
Y1 = 0
MaxS = []
for i in y:
    s1=3.14*((2.5+2*i*0.9877)**2)/4-3.14*(2.5**2)/4
    length=length+1
    if s1 > s2:
        MaxS.append(s2)
        pass
    else:
        MaxS.append(s1)
        pass
    pass
i = 0.0
x = []
while i<100:
    x.append(i)
    i=i+0.01
    pass
X0=0.20
X1=2.25
S2=1.5386
plt.plot(x,MaxS,)

plt.scatter(X0, S2,s=75, color='k')
plt.scatter(X1, S2,s=75, color='r')
plt.annotate(r'$S2 = %s\ when\ \{X0=0.20\}\ then\ \{Y0=0.19098\}\ satisfies\ the\ condition$'%S2, xy=(X0,S2), xycoords='data', xytext=(+30,-30),textcoords='offset points', fontsize=10,arrowprops=dict(arrowstyle='->',connectionstyle='arc3, rad=.2'))
plt.annotate(r'$S2 = %s\ when\ \{X1=2.25\}\ then\ \{Y1=0.18911\}\ satisfies\ the\ condition$'%S2, xy=(X1,S2), xycoords='data', xytext=(+20,-50),textcoords='offset points', fontsize=10,arrowprops=dict(arrowstyle='->',connectionstyle='arc3, rad=.2'))



plt.show()
