#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y1)

plt.figure(num = 3, figsize = (8,5))
l1, = plt.plot(x, y2, label='up')
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')

# 设置坐标xlim是范围，xlabel是名称 xticks是更改下标，gca之下是关于边框的操作
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am X')
plt.ylabel('I am y')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-1, -0.25 , 1, 1.25, 2], 
          [r'$very\ not\ good$', r'$not\ good$', r'$good$', r'$fingood$', r'$best$'])

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 图例
plt.legend(handles=[l1,l2,], labels=['aaa', 'bbb'], loc='best')

plt.show()
