# Lets understand this new topic 
# Package is a folder/directory
#          -> (which contain different .py files called scripts or module)
#            -> (Each script/module file can contain many resuable specific functions, methods, and types )

# There are thousands of package distributed for various use like :
# numpy (mathematical operations)
# matplotlib (for graph visualization of data)
# scikit-learn (machine learning)

# To use this package, we need to install it via package installer using terminal
# Read https://pip.readthedocs.io/en/stable/installing/

# To use in your .py script it needs to be imported 

# Lets give some hard try for this topic

""" Import package

  As a data scientist, some notions of geometry never hurt. Let's refresh some of the basics.

   For a fancy clustering algorithm, you want to find the circumference, C, and area, A, of a circle. 
   When the radius of the circle is r, you can calculate C and A as:
                                        C=2πr
                                        A=πr2
    To use the constant pi, you'll need the math package. 
    A variable r is already coded in the script. Fill in the code to calculate C and A and 
    see how the print() functions create some nice printouts """.

  # Try
  r = 0.43
  
  # Import the math package
  import math

  # Calculate C
  C = 0
  C = 2*math.pi*r

  # Calculate A
  A = 0
  A = math.pi * r * r
  
  # Build printout
  print("Circumference: " + str(C))
  print("Area: " + str(A))
  
  
  # Importing a package just like one above "math" imports all its functionality and even we have to call functions by appending 
  # the package name with function or constant name e.g math.pi (We cannot use "pi" as it is)
  
  # Some times we need just specfic part to be imported from package,
  # Let see example
  
  from math import pi

  # Let's say the Moon's orbit around planet Earth is a perfect circle, with a radius r (in km) that is defined in the script.
  
  # Perform a selective import from the math package where you only import the radians function.
  from math import pi
  from math import radians

  # Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist. 
  # You can calculate this as r * phi, where r is the radius and phi is the angle in radians. 
  # To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported.
  dist = r * radians(12)
  print(dist)
