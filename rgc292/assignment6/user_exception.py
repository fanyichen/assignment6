'''
Created on Oct 29, 2015

@author: Rafael Garcia (rgc292)
'''
"""This class is public and intended for facilitating user's programming to handle 
    expected errors not covered by other exception"""
    
#This exception is raised in case of impossibility to merge two intervals     
class Raised_exception(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)