# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 11:11:57 2015

@author: YY
"""

from functions import *

def start():
    print "List of intervals?"
    intervals_raw = raw_input()
    
    try:
        interval_merged = mergeOverlapping (intervals_raw)
        print interval_merged
    except:
        print('Invalid intervals')
        
        
    while True:

        print "Add an interval?"
        interval_add = raw_input()
        if interval_add.lower() == "quit":
            break
        
        try:
            interval_merged = insert(interval_merged, interval_add)
            print interval_merged
        except:
            print('Invalid interval')
    

start()   
