# Abstract
"""
# The Numbers in Python
## Contents
- Integer and Float data types
- Basic mathematical operations
- Defining variables
--------------------------------------------------
# Integer and Float data types
### Integer
All the numbers (negative, zero or positive) are integer in the math.
For example: -100, 34, 2, 0

## Float
Floats are one of the vary of numbers like integers.
For example: 3.14, 3.55456, -13.54

# Basic mathematical operations
## Addition
3 + 4

## Subtraction
5 - 17

## Multiplication
13 * 4

# Division
4 / 2

# Defining variables
The variables keep a data which is one of the data types. For example:
i = 10

There some important point, when you define a variable:
1. The name of variables cannot start a number.
    Wrong using:
        5a = 12
2. The name of variables doesn't include space character.
    Wrong using:
        name of course = "Introduction to Python"
3. The symbols aren't used defining variables.
    Note: You can use just underline (_) symbol.
    Wrong using:
        ?a = 5
    Correct using:
        _a = 4
"""

# Let's calculate circumference of a circle using we learned

pi_number = 3.14
diameter = 4
circumference = pi_number * diameter
print(circumference)

# There is a practical way for the changing values of two variable in Python

a = 4
b = 3
print(a, b)
a, b = b, a
print(a, b)

# Finally, let's see how to increase the value of a variable

a = 10
print(a)
a += 1  # It is a same thing that a = a + 1
print(a)
