#!/usr/bin/env python

from distutils.core import setup

setup(
    name='abelectronics',
    version='0.1',
    description='ABElectronics Python 3 libraries',
    author='Brian Dorey',
    author_email='sales@abelectronics.co.uk',
    url='https://github.com/abelectronicsuk/ABElectronics_Python3_Libraries',
    packages=['ADCDACPi', 'ADCDifferentialPi', 'ADCPi', 'DeltaSigmaPi', 'ExpanderPi', 'IOPi',
              'RTCPi', 'ServoPi'],
)
