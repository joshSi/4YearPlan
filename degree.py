#!/usr/bin/env python3

class Degree:
    '''Degree superclass for any degree'''

    def __init__(self, dept, name):
        '''Initialize degree class
        name: Degree name
        courses: Set of course requirements
        '''
        self.department = dept
        self.name = name

    def __repr__(self):
        return self.dept+': '+self.name

class Major(Degree):
    '''Major class'''
    def __init__(self, dept, name, upperdiv=set(), lowerdiv=set()):
        super().__init__(dept, name)
        self.lowerdiv = lowerdiv
        self.upperdiv = upperdiv

class Minor(Degree):
    '''Minor class'''
    def __init__(self, dept, name, courses=set()):
        super().__init__(dept, name)
        self.courses = courses