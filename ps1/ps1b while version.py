#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:45:17 2020

@author: cuiyiwen
"""


#starting_annual_salary = float(input("Enter your starting annual salary: "))
#portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
#total_cost = float(input("Enter the cost of your dream home: "))
#semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

starting_annual_salary = float(80000)
portion_saved = float(0.1)
total_cost = float(800000)
semi_annual_raise = float(0.03)

portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
r=0.04
n=0
current_saving = 0
monthly_pay = starting_annual_salary / 12 * portion_saved

while current_saving < down_payment:    
    i = 0
    while i<6:
        i = i + 1
        current_saving = monthly_pay + current_saving + current_saving * r / 12 
        if current_saving >= down_payment:
            break
    
    n= n + i
    #print(monthly_pay)
    monthly_pay = monthly_pay + monthly_pay * semi_annual_raise
    
print("Number of month: " + str(n))




