while True:
  line = input('> ')
  if line[0] == '#' :
    continue # Ignoring the line which starts with '#'
  if line == 'done' :
    break
  print(line)
print('Done!')