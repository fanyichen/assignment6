'''
Created on Oct 24, 2015

@author: bk1051

Python packaging based on info from:
http://python-packaging.readthedocs.org/
https://the-hitchhikers-guide-to-packaging.readthedocs.org/
'''

from setuptools import setup

setup(name='interval',
      version='0.1dev',
      description='Define, use, and manipulate closed and open intervals',
      packages=['interval'],
      install_requires=[
    ],
      test_suite='nose.collector',
      tests_require=['nose'])