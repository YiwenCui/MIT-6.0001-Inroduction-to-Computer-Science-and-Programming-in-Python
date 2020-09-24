#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:14:13 2020

@author: cuiyiwen
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = total_cost * 0.25

current_saving = 0
n = 0
r = 0.04
while current_saving < portion_down_payment:
    current_saving = start_annual_salary / 12 * portion_saved + current_saving + current_saving * (r / 12)
    n=n+1
print("Number of months: " + str(n))





