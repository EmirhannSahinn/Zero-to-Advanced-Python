"""
# Strings

## Creating Strings
There are many ways to create a string. Let's see these ways.
"""

# # The creation of a string with single quote

my_string = 'Emirhan Sahin'
print(my_string)

# # The creation of a string with double quotes

my_string = "Emirhan Sahin"
print(my_string)

# # The creation of a string with triple quotes

my_string = """Emirhan Sahin"""
print(my_string)

"""
Note:
If you start to create string with using double quotes,
you have to use double quotes in the end of the string.
Wrong using:
    my_string = "Emirhan Sahin'
    
Okay then how we can define this string: Emirhan's got a lesson today
Wrong using:
    my_string = 'Emirhan's got a lesson today'
    print(my_string)
    
    Output:
    my_string = 'Emirhan's got a lesson today'
                                             ^
    SyntaxError: unterminated string literal 

Let's see the correct way in the above.
"""
my_string = "Emirhan's got a lesson today"
print(my_string)

"""
Note: 
There are some characters in the Python which is called "Escape Characters"
In our case, you can use backslash which is one of the escape characters
Wrong using:
    my_string = 'Emirhan's got a lesson today'
    print(my_string)
    
    Output:
    my_string = 'Emirhan's got a lesson today'
                                             ^
    SyntaxError: unterminated string literal 
    
Let's see the another correct way with using the backslash 
"""

my_string = 'Emirhan\'s got a lesson today'
print(my_string)

"""
## Indexing Strings
Strings are ordered sequences of character data. 
Indexing allows you to access individual characters in a string directly by using a numeric value. 
String indexing is zero-based: the first character in the string has index 0, the next is 1, and so on.

We will use square brackets [], when the indexing a string. Let's see the examples.
"""

# Try to reach first character of my_string
my_string = "Emirhan"
print(my_string[0])

# Try to reach second character of my_string
print(my_string[1])

# Then, how we can reach the last character of a string?
my_string = "I'm learning Python"

# If you know the length of the string you can reach the last character easily.
# We will use len() function to reach the length of the string

"""
print(my_string[len(my_string)])

Output:
    print(my_string[len(my_string)])
          ~~~~~~~~~^^^^^^^^^^^^^^^^
    IndexError: string index out of range

UPPS! There is an error there!!!

You shouldn't forget that the indexing of a strings starts with 0
Let's see the correct way.
"""
print(my_string[len(my_string) - 1])

# There is the easiest way to reach the last character of a string
print(my_string[-1])

# You can also use negative numbers to index a string from right to left
print(my_string[-2])

"""
# But you have to pay attention the length of the string
Wrong using:
print(my_string[-len(my_string) - 1])

Output:
     print(my_string[-len(my_string) - 1])
          ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
    IndexError: string index out of range
"""

# Let's see  the correct way and reach to first character using indexing from right to left
print(my_string[-len(my_string)])

"""
## Slicing Strings
We will use square brackets [] with indexes to slice a string
[starting index: ending index: step value]
Syntax:
    arr[start:stop]         # items start through stop-1
    arr[start:]             # items start through the rest of the array
    arr[:stop]              # items from the beginning through stop-1
    arr[:]                  # a copy of the whole array
    arr[start:stop:step]    # start through not past stop, by step
    
Let's see examples. 
"""

# Try to reach "on Pro" part of "Python Programming Language"

my_string2 = "Python Programming Language"
# Start with 4th index and take the part until 10th index (10th index not included)
print(my_string2[4:10])

# If the starting index is not specified, start with beginning of string
print(my_string2[:10])

# If the ending index is not specified, take until the ending of the string
print(my_string2[4:])

# If the both starting and ending indexes are not specified, take the whole index
print(my_string2[:])

# Take until last character
print(my_string2[:-1])

# Start with beginning of the string and take the part by jumping 2 characters
print(my_string2[::2])

# Start with 4th index and take the part until 12th index by jumping 3 characters
print(my_string2[4:12:3])

# Take part beginning to ending by jumping -1 character (inverse of the string)
print(my_string2[::-1])

# # String Properties

# 1) Using len() function: used to determine the length of a string
my_string3 = "Emirhan"
print(len(my_string3))

# 2) Immutable: Python strings are "immutable" which means they cannot be changed after they are created

"""
my_string3 = "Emirhan"
my_string[0] = "T"
print(my_String3)

Output:
    my_string[0] = "T"
    ~~~~~~~~~^^^
    TypeError: 'str' object does not support item assignment
"""

# 3) Addition of Strings

my_string = "I'm "
my_string2 = "learning "
my_string3 = "Python"
my_string4 = my_string + my_string2 + my_string3
print(my_string4)

# 4) Multiplication

my_string5 = my_string3 + my_string3 + my_string3
print(my_string5)

my_string6 = my_string3 * 3
print(my_string6)