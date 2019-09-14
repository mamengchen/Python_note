#!/usr/bin/env python
# coding=utf-8
'''
条件控制 循环控制 分支
if else for while switch
'''
'''
mood = True

if mood:
    print('go to left')
else:
    print('go to right')
print('back away')

a = 1
b = 2
if a>b:
    print("a big")
else:
    print("b big")

'''
'''
d = []
if d:
    print('kong')
    pass
else:
    print('bukong')
'''
account = 'qiyue'
password = '123456'
print('input_account:')
user_account = input()

print('input_password:')
user_password = input()

if account == user_account:
    if password == user_password:
        print('success')
        pass
    else:
        print('mima cuowu')
        pass
    pass
else:
    print('mei you gai yong hui')

