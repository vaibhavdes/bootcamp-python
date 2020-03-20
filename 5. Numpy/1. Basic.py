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
