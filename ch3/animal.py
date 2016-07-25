#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    __slots__ = ('nameX', 'ageX') # 用tuple定义允许绑定的属性名称
    name = 'animal' #类属性
    def run(self):
        print("Animal is running...")

def test():
    d = Dog()
    d.run()

    c = Cat()
    c.run()

    print(dir(c))
    print(type(c.__dir__))
    
class Dog(Animal):
    def run(sefl):
        print('Dog is eating...')

class Cat(Animal):
    #def run(sefl):
    print('Cat is eating...')




if __name__ == '__main__':
    test()