# Addition (+)

# # Integer
a = 14
b = 15
print(a + b)

# # Float
i = 3.1
j = 4.8
print(i + j)

# Subtraction (-)

# # Integer
a = 28
b = 35
c = 40
print(a - b - c)

# You can also use negative integer numbers
t = -1
y = 5
print(t - y)

# # Float
k = 3.1
l = 5.8
print(k - l)

# Multiplication (*)

# # Integer
a = 4
b = 5
print(a * b)

# # Float
i = 3.14
j = 4.5
print(i * j)

# You can mutliply one integer number and float number
a = 3
b = 3.14
print(a * b)

# Division (/)

# # Integer
a = 4
b = 2
print(a / 2)

# # Float
i = 3.14
j = 1.25
print(i / j)

# Integer Division (Floor Division) (//)

a = 4
b = 2
print(a // b)

i = 22
j = 7
print(i // j)

# Finding the Remainder Term (%)
# This operator ensure you to find the reminder number of divisible two number

a = 13
b = 4
print(a % b)

# Power Operator (**)

a = 4
b = 2
print(a ** b)

i = 8
j = 1/3
print(i ** j)

# Changing Sign (-)

a = 4
print(-a)

"""
# Using operators together and order of processing
The order of processing in Python is exactly same in the math. 
1. The priority is the inside of the parenthesis  
2. Multiplication and division is made before the addition and subtraction
3. The order of processing is left to right
"""

print(8 + ((4 * 3) / 2) - 18)
