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
