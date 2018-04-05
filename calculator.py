"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def operation():
    inputs = raw_input("")
    calc_data = inputs.split()
    return calc_data


def calcing():
    calc_data = operation()
    if calc_data == ['q'] or calc_data == ["quit"]:
        return
    elif calc_data[0] == "+":
        print add(int(calc_data[1]), int(calc_data[2]))
        return calcing()
    elif calc_data[0] == "-":
        print subtract(int(calc_data[1]), int(calc_data[2]))
        return calcing()
    elif calc_data[0] == "*":
        print multiply(int(calc_data[1]), int(calc_data[2]))
        return calcing()
    elif calc_data[0] == "/":
        print divide(int(calc_data[1]), int(calc_data[2]))
        return calcing()
    elif calc_data[0] == "square":
        print square(int(calc_data[1]))
        return calcing()
    elif calc_data[0] == "cube":
        print cube(int(calc_data[1]))
        return calcing()
    elif calc_data[0] == "power":
        print power(int(calc_data[1]), int(calc_data[2]))
        return calcing()
    elif calc_data[0] == "mod":
        print mod(int(calc_data[1]), int(calc_data[2]))
        return calcing()
    elif calc_data[0] == "add_mult":
        print add_mult(int(calc_data[1]), int(calc_data[2]), int(calc_data[3]))
        return calcing()
    elif calc_data[0] == "add_cubes":
        print add_cubes(int(calc_data[1]), int(calc_data[2]))
        return calcing()
    else:
        print ("Input is in an incorrect format. Use a math prefix followed by 2 numbers; each should be separated by a blank space.")
        return calcing()


calcing()
