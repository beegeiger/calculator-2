"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def operation():
    inputs = raw_input('')
    calc_data = inputs.split()
    return calc_data


def calcing(calc_data):
    if calc_data[0] == "+":
        print add(int(calc_data[1]), int(calc_data[2]))


calcing(operation())
