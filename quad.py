#Lionel Lynch
#quad.py
#ask the user for the coefficients a,b,c of a qudratic requation 
#and return the roots

import math

def determinant(a,b,c):
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    formula = b**2 -4*a*c
    return formula

print(determinant(1,2,3))
