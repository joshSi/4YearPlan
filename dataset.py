#!/usr/bin/env python3
import degree
import xml.etree.ElementTree as ET

class Dataset:
    '''Handles data.xml'''
    def __init__(self, file='data.xml'):
        self.root = ET.parse(file).getroot()
    
    def get_dept_majors(self, dept):
        '''Return list of majors in department'''
        return self.root.findall('.//Major[@dept="'+dept+'"]')
    def get_major(self, major):
        '''Return major Element'''
        for M in self.root.findall('.//Major'):
            if M.find('name').text==major:
                return M
            
if __name__=='__main__':
    ds = Dataset()
    print(ds.get_dept_majors('Computer Science')[0].find('name').text)
    print(ds.get_major('Computer Science').find('name').text)