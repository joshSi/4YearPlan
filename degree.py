#!/usr/bin/env python3

class Degree:
    '''Degree superclass for any degree'''

    def __init__(self, school, name):
        '''Initialize degree class
        name: Degree name
        courses: Set of course requirements
        '''
        self.school = school
        self.name = name

    def __repr__(self):
        return self.school+': '+self.name

class Major(Degree):
    '''Major class'''
    def __init__(self, school, name, upperdiv=set(), lowerdiv=set()):
        super().__init__(school, name)
        self.lowerdiv = lowerdiv
        self.upperdiv = upperdiv

class MajorElement(Major):
    def __init__(self, elem):
        self.root = elem
        self.school = elem.attrib['school']
        self.name = elem[0].text

class Minor(Degree):
    '''Minor class'''
    def __init__(self, school, name, courses=set()):
        super().__init__(school, name)
        self.courses = courses