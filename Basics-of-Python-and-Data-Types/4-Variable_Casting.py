"""
# Casting
There may be times when you want to specify a type on to a variable. This can be done with casting.
We have some functions to use for the casting:
    int() - constructs an integer number from an integer literal, a float literal (by removing all decimals),
        or a string literal (providing the string represents a whole number)
    float() - constructs a float number from an integer literal, a float literal or a string literal
        (providing the string represents a float or an integer)
    str() - constructs a string from a wide variety of data types, including strings,
        integer literals and float literals
"""

# Converting Integers to Floats

a = 45
b = float(a)
print(b)

# Converting Floats to Integers

a = 3.14
b = int(a)
print(b)

a = 4
b = 2
print(int(a/b))

# Converting Numbers to Strings

# # Integers
my_int = 15
my_string = str(my_int)
print(my_string)

# # Floats
my_float = 3.1443
my_string2 = str(my_float)
print(my_string2)

"""
# Converting Strings to Integers
There are some points which you pay attention, when converting a integer to string. Let's see an example.
Wrong using:
    my_string = "dasdasd343435"
    my_int = int(my_string)
    print(my_int)
    
Output:
    my_int = int(my_string)
             ^^^^^^^^^^^^^^
    ValueError: invalid literal for int() with base 10: 'dasdasd343435'
    
You have to check your string which you want to convert to int that is in the suitable format or not.
"""

my_string = "32434324324234"
my_int = int(my_string)
print(my_int)

"""
# Converting String to Floats
Wrong using:
    my_string = "3.14.324324"
    my_float = float(my_string)
    print(my_float)
    
Output:
    my_float = float(my_string)
               ^^^^^^^^^^^^^^^^
    ValueError: could not convert string to float: '3.14.324324'
"""

my_string = "3.1444545"
my_float = float(my_string)
print(my_float)
