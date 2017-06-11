#!/usr/bin/python3

from ABE_ExpanderPi import RTC
import struct

"""
================================================
ABElectronics Expander Pi | RTC memory demo
Version 1.0 Created 11/06/2017


run with: python3 demo-memory-int.py
================================================

This demo shows how to write to and read from the internal battery 
backed memory on the DS1307 RTC chip
"""

def int_to_array(val):
    # convert an integer into a four byte array
    x = [0, 0, 0, 0]
    x[3] = val & 0xFF
    val >>= 8
    x[2] = val & 0xFF
    val >>= 8
    x[1] = val & 0xFF
    val >>= 8
    x[0] = val & 0xFF    
    return x
    
    
def array_to_int(x):
    # convert a four byte array into an integer
    val = (x[0]<<24) + (x[1]<<16) + (x[2]<<8) + x[3]
    return val

# create a new instance of the RTC class
rtc = RTC()

# integer to be written to the RTC memory
writeval = 176247 

# convert the integer into an array of bytes
writearray = int_to_array(writeval)

# write the array to the RTC memory
rtc.write_memory(0x08, writearray)

# read four bytes from the RTC memory into an array
read_array = rtc.read_memory(0x08, 4)

# print the individual array values
print (read_array[0], read_array[1], read_array[2], read_array[3])

# combine the array values into an integer and print it
print (array_to_int(read_array))