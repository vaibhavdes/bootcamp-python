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


    
  
