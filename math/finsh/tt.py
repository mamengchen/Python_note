#!/usr/bin/env python
# coding=utf-8


def s(v):
    s1=3.14*((2.5+2*v*0.9877)**2)/4-3.14*(2.5**2)/4
    return s1

a = input("input: ")
print 3.14*(1.4**2)/4
print s(a)

