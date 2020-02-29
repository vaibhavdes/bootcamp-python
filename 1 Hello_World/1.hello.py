# No Semicolon My Friend
print("Hello World")

# Anything starting with # is Single Line Comment
print(5 / 8)

# Simple Calculations
print(7 + 10)
print(3 * 5)
print(10 / 2)
# Modulo - Prints Remainder of Division
print(18 % 7)

# Some More Calculation Below
# Exponentiation : 4 raise to 2 ( 4 ^ 2 )
print(4 ** 2)

# How much is your $100 worth after 7 years? (If you get 10% Interest Every Year)
print(100*(1.1**7))


# Variables & Data Types
# Variable name are case-sensative
savings = 100
print(savings)

# Let do Previous Example with Variable
growth_multiplier = 1.1
result = (savings * growth_multiplier ** 7)
print(result)

# String - Data Type
desc = "compound interest"

# Bool / Boolean - Data Type [ Useful for Condition Checking ] 
profitable = True

# type(arg) is used to know data type of variable 
type(savings)
type(desc)
type(profitable)

# By Writing Just Variable Name in Python Shell it will print the value

# Playing with Data Types
# here savings [int] & growth_multiplier [float]
year1 = savings * growth_multiplier
print(year1)
# Check What Data Type it returns
type(year1)
print(type(year1))


# here adding string with string [str] (Appending / Binding Strings)
doubledesc = desc + desc
print(doubledesc)

# Type Conversion
# Here Saving [int] and Result [float] are converted to string to be appended with rest of string message
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# here pi is string
pi_string = "3.1415926"
# here string is converted to float
pi_float = float(pi_string)

# try this
print("I said " + ("Hey " * 2) + "Hey!")

# try this
print(True + False)
print(True + True)

# That's All Hope you Enjoyed :-)

