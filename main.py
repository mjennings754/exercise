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

"""
Exercise 2. Cumulative Sum of a Range

Practice Problem: Iterate through the first 10 numbers (0–9).
 In each iteration, print the current number, the previous number, and their sum.
"""
prev = 0
for i in range(10):
    sum = prev + i
    print(f"Current number: {i} Previous Number {prev} Sum: {sum} ")

    prev = i

"""
Exercise 3. String Indexing and Even Slicing
Practice Problem: Display only those characters which are present at an even index number in given string.
"""
rstr = "Python programming"
print("Original string is ", rstr)

even_chars = rstr[0::2]
print("Printing only even index chars")
for char in even_chars:
    print(char)

"""
Exercise 4. String Slicing and Substring Removal

Practice Problem: Write a function to remove characters from a string starting from index 0 up to n and return a new string.
"""

def remove_char(word, n):
    print(word)

    res = word[n:]
    return res

print(remove_char("Python", 4))

"""
Exercise 5. Variable Swapping (The In-Place Method)

Practice Problem: Write a program to swap the values of two variables, a and b, without using a third temporary variable.
"""

a = 5
b = 10
print(a, b)
a, b = b, a
print(a, b) 