# Importing Numpy Package and to avoid conflict we are using it as np you can call it as 
import numpy as np

# Following is normal python list
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# To Convert to Numpy Array
np_baseball = np.array(baseball)

print(np_baseball)
print(type(np_baseball))

# Lets try some more 
# Ref http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights Player data

# Problem Statement : You are a huge baseball fan. You decide to call the MLB (Major League Baseball) 
# and ask around for some more statistics on the height of the main players. 
# They pass along data on more than a thousand players, which is stored as a regular Python list: height_in. 
# The height is expressed in inches. Can you make a numpy array out of it and convert the units to meters?

# Create a numpy array from height_in. Name this new array np_height_in.
import numpy as np

np_height_in = np.array(height_in)

# Multiply np_height_in with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
np_height_m = np_height_in * 0.0254
print(np_height_m)

# height_in is in inches and weight_lb is in pounds.

# Create a numpy array from the weight_lb list with the correct units. Multiply by 0.453592 to go from pounds to kilograms. Store the resulting numpy array as np_weight_kg.
# Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation:
# Formulae - BMI=weight(kg)height(m)2

np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg/np_height_m**2
print(bmi)

# To Subset in Numpy Array or Python List we use subscript and in both subsetting works the same way
x = [4 , 9 , 6, 3, 1]
print(x[1])
y = np.array(x)
print(y[1])

# Print out a sub-array of np_height_in that contains the elements at index 100 up to and including index 110.
print(np_height_in[100:111])


# In Numpy we have more than that let's see

# Create a boolean numpy array: the element of the array should be True if the corresponding baseball player's BMI is below 21. 
# You can use the < operator for this. Name the array light.
light = bmi < 21
print(light)

# Also see this
#Print out a numpy array with the BMIs of all baseball players whose BMI is below 21.
# Use light inside square brackets to do a selection on the bmi array.
print(bmi[light])
print(bmi[bmi < 21])

# First of all, numpy arrays cannot contain elements with different types.
# If you try to build such a list, some of the elements' types are changed to end up with a homogeneous list. 
# This is known as type coercion.

# Second, the typical arithmetic operators, such as +, -, * and / have a different meaning for regular Python lists and numpy arrays.

# Try
np.array([True, 1, 2]) + np.array([3, 4, False])

