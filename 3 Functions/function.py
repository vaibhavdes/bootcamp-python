
  # Function is a piece of code for particular functionality or to get  processed output when certain input is provided.
  # We already used few of python function, do you remember ? e.g print(), type()
  # Function are reusable
  
  # Try this
  var1 = [1, 2, 3, 4]
  var2 = True
  
  # Use print() in combination with type() to print out the type of var1.
  print(type(var1))
  
  # Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
  print(len(var1))

  # Use int() to convert var2 to an integer. Store the output as out2.
  out2 = int(var2)

  # To Know About Any Function and What argument does it take (Few arguments might be optional)
  help(type)
  help(max)
  ?max
  ?type
  # Also there are thousand of function in python, if you need for anything search on internet

  # Lets learn one new function i.e sorted()
  # Ref https://docs.python.org/2/glossary.html#term-iterable
  # Try
  first = [11.25, 18.0, 20.0]
  second = [10.75, 9.50]
  
  # Use + to merge the contents of first and second into a new list: full.
  full = sorted(first)  + sorted(second)
  # Call sorted() on full and specify the reverse argument to be True. Save the sorted list as full_sorted.
  full_sorted = sorted(full,reverse=True)
  print(full_sorted)
