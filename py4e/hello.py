smallest = None
print('Before', smallest)
for value in [41, 9, 23, 37, 74, 15] :
  if smallest is None :
    smallest = value
  elif value < smallest:
    smallest = value
  print(smallest, value)
print('After', smallest)