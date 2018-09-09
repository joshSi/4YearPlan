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
        self.lowerdiv = self.root.find('lowerdiv')
        self.upperdiv = self.root.find('upperdiv')
    
    def list_required_lowerdiv(self):
        req = [i.attrib for i in self.lowerdiv.findall('course')]
        opt = [i.attrib for i in list(self.lowerdiv.findall('option'))]
        return {'req': req, 'opt': opt}
    
    def list_required_upperdiv(self):
        req = [i.attrib for i in self.upperdiv.findall('course')]
        opt = [i.attrib for i in list(self.upperdiv.findall('option'))]
        return {'req': req, 'opt': opt}

class Minor(Degree):
    '''Minor class'''
    def __init__(self, school, name, courses=set()):
        super().__init__(school, name)
        self.courses = courses