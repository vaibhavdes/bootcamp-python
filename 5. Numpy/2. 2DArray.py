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
