#A module in python is a piece of code that can be imported and used in other python programs. Modules are used to organize code and make it reusable.

#Folowing are some examples of modules in python:
import math #math module provides mathematical functions and constants
print(math.pi) #This prints the value of Pi, Now we already Imported maths so we chose the path of Pi in math module like so math.pi but you can also import specific things from a module like so: from math import pi and then you can just use pi directly.
from math import pi
print(pi) #As we have imported Pi from math we don't need to write math.pi we can just write pi directly.

import random #random module provides functions for generating random numbers
print(random.choice("123"))

import os #os module provides functions for interacting with the operating system
o = open("names.txt")
print(o.read())
o.close()

import sys as windows # You can also import a module and give it a different name like so: import sys as windows
print(windows.version)

#print(dir(math)) #dir() function returns a list of all the attributes and methods of a module.

for l in dir(math): #this is a cleaner way of the print(dir(math)).
    print(l) 

import faisalabad #faisalabad is a custom module we created in the same directory as this file. So we can import it like any other module.

print(faisalabad.overview())

print(faisalabad.__name__) #This prints the name of the current module. If the module is being run directly, the name will be "__main__". If the module is being imported, the name will be the name of the module.

