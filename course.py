#!/usr/bin/env python3

class Course:
    '''Course superclass for any course'''
    def __init__(self, dept, num, name='',
        units=4, prereq=set(), restr=set(), coclass=None,):
        self.dept, self.num, self.name = dept, num, name
        self.units = units
        self.prereq, self.restr = prereq, restr
        if coclass:
            self.coclass = coclass
        else:
            self.coclass = 'No co-classes required'
    
    def __repr__(self):
        return self.dept+' '+self.num

    def get_info(self):
        return self.__repr__()+': '+self.name\
            +'\nPrerequisites: '+', '.join(self.prereq)\
            + '\nCoclasses: '+self.coclass
        

class GE(Course):
    '''GE class'''
    def __init__(self, section=set(), dept, num, name='',
        units=4, prereq=set(), restr=set()):
        self.section = section
        super.__init__(dept, num, name, units, prereq, restr)