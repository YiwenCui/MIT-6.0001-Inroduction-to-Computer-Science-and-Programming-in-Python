#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 21:24:50 2020

@author: cuiyiwen
"""


starting_annual_salary = 150000
total_cost = 1000000
portion_down_payment = 0.25
r = 0.04
semi_annual_raise = float(0.07)

down_payment = total_cost * portion_down_payment
# steps = 0
low = 0
high = 1
epsilon = 0.0001

def get_saving (guess):
    monthly_pay = starting_annual_salary * guess / 12
    current_saving = 0
    for n in range(1,37):
        if n % 6 == 0:
            monthly_pay = monthly_pay + starting_annual_salary * guess  * semi_annual_raise / 12
        current_saving = monthly_pay + current_saving + current_saving * r / 12 
        n=n+1
    return current_saving

guess = (low + high)/2

saving = get_saving(guess)


while abs(saving - down_payment) >= epsilon:
    print(guess)
    print("saving:" + str(saving))
    print("down_payment:" + str(down_payment))
    saving = get_saving(guess)
    if saving > down_payment:
        high = guess
    else:
        low = guess
    guess = (float)(high + low) / 2

print (guess)

# given guesss, what is the saving of 36th month

    


        
    
        
      