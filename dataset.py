#!/usr/bin/env python3
import degree
import xml.etree.ElementTree as ET

class Dataset:
    '''Handles data.xml'''
    def __init__(self, file='data.xml'):
        self.root = ET.parse(file).getroot()
    
    def get_major(self, dept='', major=''):
        if major:
            return [M for M in self.root.findall('.//Major') if M.find('name').text==major]
        elif dept:
            return self.root.findall('.//Major[@dept="'+dept+'"]')
if __name__=='__main__':
    ds = Dataset()
    print(ds.get_major(dept='Computer Science')[0].find('name').text)
    print(ds.get_major(major='Computer Science')[0].find('name').text)