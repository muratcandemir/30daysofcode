#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
	total_cost = meal_cost * (1 + ((tip_percent + tax_percent) / 100))
	return total_cost
	

if __name__ == '__main__':
 meal_cost = float(input("Meal Cost?"))
 tip_percent = int(input("Tip Percent?"))
 tax_percent = int(input("Tax Percent?"))
 print(round(solve(meal_cost, tip_percent, tax_percent)))
