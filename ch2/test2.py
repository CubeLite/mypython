#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def my_move(x, y, step, angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx, ny
    
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad input')
    if x >= 0:
        return x
    else:
        return -x


    
