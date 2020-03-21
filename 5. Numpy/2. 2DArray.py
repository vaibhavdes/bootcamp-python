# After Learning One Dimension Python List &  Numpy Array 
# Lets have quick intro for Multi-Dimension Array that are required for Data Analyis 
# Unlike Python List, Numpy Array can contain only one type of data

# We have our older baseball data from last Lesson [heigh,weight]
# This is Python List of List
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

import numpy as np

# Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
np_baseball = np.array(baseball)

print(type(np_baseball))

# Shape is attribute which gives meta-information about array
print(np_baseball.shape)

# Subsetting 2D Array

# Lets say we want to print 'a' & 'c' from below list
x = [["a", "b"], ["c", "d"]]

# Using Regular Python List
[x[0][0], x[1][0]]

# Using Numpy
np_x = np.array(x)
# The indexes before the comma refer to the rows, while those after the comma refer to the columns. 
# : means slicing, i.e to include 0 th coloum data from all rows
np_x[:,0]

# Print out the 50th row of np_baseball.
print(np_baseball[49,:])

# Make a new variable, np_weight_lb, containing the entire second column of np_baseball.
np_weight_lb = np_baseball[:,1]

# Select the height (first column) of the 124th baseball player in np_baseball and print it out.
print(np_baseball[123,0])


# Try 
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat

# numpy array with 3 columns representing height (in inches), weight (in pounds) and age (in years).
# You managed to get hold of the changes in height, weight and age of all baseball players. It is available as a 2D numpy array, updated. Add np_baseball and updated and print out the result.
                        # print(np_baseball + updated)
# You want to convert the units of height and weight to metric (meters and kilograms respectively). As a first step, create a numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.
                        # conversion = np.array([0.0254,0.453592,1])
# Multiply np_baseball with conversion and print out the result.
                        # print(np_baseball * conversion)
            
            
# Try
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)

# Create numpy array np_height_in that is equal to first column of np_baseball.
                        # np_height_in = np.array(np_baseball[:,0])

# Try
med = None
print("Median: " + str(med))

# Use np.std() on the first column of np_baseball to calculate stddev. Replace None with the correct code.
stddev = np.std(np_baseball[:,0])

# Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column of np_baseball in corr. Replace None with the correct code.
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])

# After Baseball Data, Lets Analyze Soccer Data

