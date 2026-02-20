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

"""
Exercise 6. Calculating Factorial with a Loop
ractice Problem: Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
"""
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")

"""
Exercise 7. List Manipulation: Add and Remove

Practice Problem: Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).
"""
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits[-1] = "fig"
fruits.pop(1)
print(fruits)

"""
Exercise 8. String Reversal
Practice Problem: Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).
"""
given_string = "Python"
print(given_string[::-1])

"""
Exercise 9. Vowel Frequency Counter

Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.
"""
vowels = "aeiou"
sentence = "Learning Python is fun!"
count = 0
for char in sentence.lower():
    if char in vowels:
        count += 1

print(count)

"""
Exercise 10. Finding Extremes (Min/Max) in a List
Practice Problem: Given a list of integers, find and print both the largest and the smallest numbers.
"""
nums = [45, 2, 89, 12, 7]
max = max(nums)
min = min(nums)

print(max, min)