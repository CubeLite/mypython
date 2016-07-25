#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

n1 = 255
n2 = 1000

print(n1, ' hex is %s', hex(n1))
print(n2, ' hex is %s', hex(n2))

fs = [d for d in os.listdir('.')]
print(fs)


L = [x*x for x in range(1, 11)] #list
print(L)

g = (x*x for x in range(1, 11)) # generator
print(next(g))
print(next(g))
print([x for x in g])

def odd():
    print('step 1')
    yield 1

    print('step 2')
    yield 2

    print('step 3')
    yield 3


d = odd()
print(d)
print(next(d))


def f(x):
    return x*x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def add(x, y):
    return x+y

from functools import reduce
print(reduce(add, [1, 3, 5, 7, 9]))

from functools import reduce
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print(str2int('35'))


from functools import reduce

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2intx(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2intx('35'))


def is_odd(n):
    return n%2 == 0

print(list(filter(is_odd, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))

def now():
    print('2016.7.21')

print(now.__name__)

f = now
print(f.__name__)

import sys
print(sys.path)