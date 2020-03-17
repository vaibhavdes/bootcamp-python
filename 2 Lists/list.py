  # In Previous Lesson we learned different basic data types as follows
  # int = integer
  # float = floating
  # str = string
  # bool = boolean
  
  # In this we gonna learn about new Python data type which can contain data points (Which are inter-related to each other) that can be used in future for analysis.
  
  # List (Values are wrapped in Square Brackets [...] ) (A Compound Data Type)
  # 1. Collection of Values
  # 2. Contain values of type (As Per Mentioned Data Types Above and advanced types)
  # 3. Contain values of Different Types (Can Contain Lists in List i.e Sub-List)
  
  # Lets take an example below list contain family member name with age
  my_family = ['x',21,'y',24]
  type(my_family)
  
  # Also it can be represented as Sub-List
  my_family = [['x',21],
               ['y',24]
              ]
  type(my_family)
  
  #Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
  # area variables (in square meters)
  hall = 11.25
  kit = 18.0
  liv = 20.0
  bed = 10.75
  bath = 9.50

  # Create list areas
  areas = [hall,kit,liv,bed,bath]
   
  #Print areas with the print() function.
  print(areas)

  # Build the list so that the list first contains the name of each room as a string and then its area
  areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]  

  # Try Following List 
  sample = [ 1 + 2, "a" * 5, 3]

  # Python List are 0 (Zero Indexing)
  print(areas[0])
  # -ve Index can be used to access element in reverse (from end-side)
  print(areas[-1])

  # List Slicing (Create New List from Exisiting List by specifying range with index)
  # [start:end] => [inclusive:exclusive]
  print(areas[3:5])
  # [:end] = elements from start i.e with zero
  print(areas[:5])
  # [start:] = element till end
  print(areas[5:])

  print(areas[1] + areas[3])

  # create a new variable, eat_sleep_area, that contains the sum of the area of the kitchen and the area of the bedroom.
  eat_sleep_area = areas[3] + areas[-3]
    
  # create a list, downstairs, that contains the first 6 elements of areas.
  downstairs = areas[0:6]
  downstairs = areas[:6]

  # Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
  upstairs = areas[6:10]
  upstairs = areas[6:]
  
  # Try ( In Python Shell )
  x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
  
  x[2]
  
  x[2][0]
  
  x[2][:2]

  # Try
  house = [['hallway', 11.25],
           ['kitchen', 18.0],
           ['living room', 20.0],
           ['bedroom', 10.75],
           ['bathroom', 9.5]]
  
  house[-1][1]

  
  # Manipulating List
  areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
  #Update the area of the bathroom area to be 10.50 square meters instead of 9.50.
  areas[-1] = 10.50
  #Make the areas list more trendy! Change "living room" to "chill zone".
  areas[4] =  "chill zone"
  
  # Try (Here 'x' holds the actual reference to memeory where array is stored and changes the value)
  x = ["a", "b", "c", "d"]
  x[1] = "r"
  x[2:] = ["s", "t"]
  
  # Extend List (To Copy the element and to avoid changes in earlier reference )
  
  #Use the + operator to paste the list ["poolhouse", 24.5] to the end of the areas list. Store the resulting list as areas_1.
  areas_1 = areas + ["poolhouse", 24.5]

  #Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.
  areas_2 = areas_1 + ["garage", 15.45]
  
  # Delete Element (and print the array to see reduced size and indexes)
  del(areas_2[1])
  # Type multiple commands in same line
  del(areas_2[1]); del(areas_2[1])
  
  # Try
  areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
  
  del(areas[-4:-2])
  
  # Behind the Scene of List
  
  # 1. We created a new List as follow
  areas = [11.25, 18.0, 20.0, 10.75, 9.50]
  # 2. We copied the same to another variable
  areas_copy = areas
  # 3. We made change in the another variable
  areas_copy[0] = 5.0
  # 4. Now try Printing the First List to see magic (Remember the reference to memory just like C/C++)
  print(areas)
  
  # To Avoid Copying Reference we can do it in another way
  areas_copy = list(areas)
  # OR 
  areas_copy = areas[:]

  
  # Hope you Enjoyed :-)


