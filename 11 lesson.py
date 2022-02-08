# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 08:10:57 2022

@author: Jetker
"""

# lesson - 11
# Task of 11 lesson

products = ["bread", "milk", "meat", "apple", "pen", "tea"]

print("Please enter 5 products!")

shop_basket = []

for n in range(5):
    shop_basket.append(input(f"{n+1}th enter product>>>"))
    
for product in shop_basket:
    if product in products:
        print(f"Yes, we have {product} from our shop!")
    
    else:
        print(f"sorry, we have not {product}!")

















    

