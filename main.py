"""
Exercise 1. Arithmetic Product and Conditional Logic
Practice Problem: Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, return their product; otherwise, 
return their sum.
"""

def intake_number(num1, num2):
    n = num1 * num2
    if n <= 1000:
        return n
    else:
        return num1 + num2
    
res = intake_number(20, 30)
print(res)