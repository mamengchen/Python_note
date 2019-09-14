#!/usr/bin/env python
# coding=utf-8

p2 = 0.1
x = []
y = []
z = []
while True:
    if p2 > 1.0:
        break
    p1=(100*p2+50)*10.3/10000
    y.append(p2)
    x.append(p1)
    z.append(p1/p2)
    p2=p2+0.05
    pass

for a in x:
    print (a)
    pass
print '--------------------------------------'
for a in y:
    print(a)
    pass
print '--------------------------------------'
for a in z:
    print(a)
