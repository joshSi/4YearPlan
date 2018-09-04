#!/usr/bin/env python3
import course, degree
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
    cs = ds.get_major('Computer Science')
    for c in cs.findall('.//course'):
        print(c.attrib['dept']+' '+c.attrib['num'])