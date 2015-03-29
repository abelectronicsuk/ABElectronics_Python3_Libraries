#!/usr/bin/python3

from ABE_ADCDACPi import ADCDACPi
import time

"""
================================================
ABElectronics ADCDAC Pi 2-Channel ADC, 2-Channel DAC | DAC Write Demo
Version 1.0 Created 29/02/2015

run with: python3 demo-dacwrite.py
================================================

this demo will generate a 1.5V p-p square wave at 1Hz
"""

adcdac = ADCDACPi()

while True:
    adcdac.set_dac_voltage(1, 1.5)  # set the voltage on channel 1 to 1.5V
    time.sleep(0.5)  # wait 0.5 seconds
    adcdac.set_dac_voltage(1, 0)  # set the voltage on channel 1 to 0V
    time.sleep(0.5)  # wait 0.5 seconds
