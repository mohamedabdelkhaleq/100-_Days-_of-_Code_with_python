# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:43:14 2024

@author: O.R.G
"""

# Day 2 PROJECT (Tip calculator)
print("welcome to the tip calculator .")
bill=float(input("waht was the total bill ? $"))
tip=int(input ("what the percentage would you like to give ? 10% ,12%,15%?"))
people=int(input("how many people to spilt the bill "))
bill_with_tip=bill*(1+tip/100)
bill_per_people="{:.2f}".format(bill_with_tip/people)
print(f"each person should pay : ${bill_per_people} ")
