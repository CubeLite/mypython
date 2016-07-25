#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print(self):
        self.god = 'god'
        print('name:%s, score:%s, god:%s' % (self.name, self.score, self.god))

def test():
    bart = Student('Bart Simpson', 98)
    bart.print()
    bart.god = 'fuck'
    print('student, name:%s, score:%s, god:%s' % (bart.name, bart.score, bart.god))

    

if __name__ == '__main__':
    test()