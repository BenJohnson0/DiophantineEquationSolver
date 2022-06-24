# Diophantine Equation solver
# Python
# Author: Ben Johnson
# Date: June 2022

# This program will ask the user to input
# their Diophantine Equation and return 
# the x and y 'for all' solutions.

# imports
import math

class runSolver():
    def __init__(self):
        self.equation = input("Enter your Diophantine Equation: ").strip()

    def findGCD(self):
        x_value = self.equation[:self.equation.index('x')] # slice from index 0 to 'x'
        y_value = self.equation[self.equation.index('x') + 2:self.equation.index('y')] # slice from index 'x' + 1 to 'y'
        z_value = self.equation[self.equation.index('y') + 2:] # slice from index 'y' + 2 to the end

        gcd = math.gcd(int(x_value), int(y_value))

        print(z_value)

    def checkGCD(self, gcd):
        pass

rs = runSolver()

rs.findGCD()