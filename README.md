# python
Everything about studying python

### if statement
```python
x = 25
if x < 10:
    print('smaller')
if x > 20:
    print('bigger')

print('fin')
# bigger
# fin
```

### repeated steps
```python
n = 5
while n > 0:
    print(n)
    n = n - 1
print('fin')

# ➜  py4e git:(master) ✗ python3 hello.py
# 5
# 4
# 3
# 2
# 1
# fin
```

### Operator Precedence Rules

1. Parenthesis
2. Power(Exponentation)
3. Multiplication, Division, Remainder
4. Addition, Subtraction
5. Left to right
```python
x = 1+2**3/4*5
print(x)
# 1

y = 1*2+(2**3)
print(y)
#10
```

### Type Matters

String
```python
eee = 'hello ' + 'there'
print(eee)
# hello there

print(eee+1)
# result
Traceback (most recent call last):
  File "/Users/kimjinkyeong/Desktop/python/py4e/hello.py", line 2, in <module>
    print(eee + 1)
          ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

Int, Float
```python

i = 42
print(type(i))
# <class 'int'>

f = float(i)
print(type(f))
# <class 'float'>

print(float(99) + 100)
# 199.0
```

### String Conversion
int(), float()
```python
sval = '123'
# convert
ival = int(sval)
print(ival + 1)
# 124

nsv = 'hello'
niv = int(nsv)
# result
Traceback (most recent call last):
  File "/Users/kimjinkyeong/Desktop/python/py4e/hello.py", line 8, in <module>
    niv = int(nsv)
          ^^^^^^^^
ValueError: invalid literal for int() with base 10: 'hello'
```

### Input Function
```python
nam = input('Who are you? ')
print('Welcome', nam)
# result
# Who are you? jin
# Welcome jin
```

### Conditional Excution
'if' statement
```python
x = 5
if x < 10:
  print('Smaller')
if x > 20:
  print('Bigger') # conditional code

print('Fins') # sequential code
```

### Comparison Operator
```python
x = 5
if x == 5:
  print('Equals 5')
if x > 4:
  print('Greater than 4')
if x >= 5:
    print('Greater than or Equals 5')
if x < 6: print('Less than 6')
if x <= 5:
    print('Less than or Equals 5')
if x != 6:
    print('Not equal 6')

print('Fins')

# Nested
for i in range(5) : 
    print(i)
    if i > 2 :
        print('Bigger than 2') # Nested. Block within a block
    print('Done with i', i)
print('All Done')
```
### Two way decisions
```python
x = 4

if x > 2 : 
  print('Bigger')
else : 
  print('Smaller')

print ('All done')
```

### Multi-way
elif
```python
x = 1
if x < 2:
  print('small')
elif x < 10:
  print('Medium')
else : 
  print('Large')
print('All done')
```

### Try and exception(prevent traceback)
<!-- Traceback -->
```python
astr = 'Hello Bob'
istr = int(astr)
print('test')

Traceback (most recent call last): # Traceback
  File "/Users/kimjinkyeong/Desktop/python/py4e/hello.py", line 2, in <module>
    istr = int(astr)
           ^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'Hello Bob'

# Traceback quit the program where it mal-function
```

<!-- Try and Except -->
```python
astr = 'Hello Bob'
try:
  istr = int(astr)
except:
  istr = -1
print('First', istr)

astr = '123'
try:
  istr = int(astr)
except:
  istr = -1
print('Second', istr)

# First -1
# Second 123

# try block stop when it wrong and go to except block
astr = 'Bob'
try:
  print('Hello')
  istr = int(astr)
  print('There')
except:
  istr = -1

print('Done', istr)
# Hello
# Done -1

# Try except & if statement
rawstr = input('Enter a number:')
try:
  ival = int(rawstr)
except:
  ival = -1

if ival > 0 : 
  print('Nice work')
else : 
  print('Not a number')
```

### Stored (and reused) Steps
<!-- Using Functions -->
```python
def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()
```
<!-- Max & Min -->
```python
big = max([10,9,8,7])
print(big)

tiny = min([10,9,8,7])
print(tiny)
# 10
# 7
```
<!-- Parameters -->
```python
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en') # Hello
greet('es') # Hola
greet('fr') # Boungjour
```

### Loops and iteration
```python
# While loop
n = 5
while n > 0 :
  print(n)
  n = n - 1
print('Blastoff!')
print(n)
# 5
# 4
# 3
# 2
# 1
# Blastoff!
# 0

# Breaking Out of a Loop
while True:
  line = input('> ')
  if line == 'done' :
    break
  print(line)
print('Done!')
# > ef
# ef
# > ae
# ae
# > done
# Done!

# Finishing an Iteration with Continue
while True:
  line = input('> ')
  if line[0] == '#' :
    continue # Ignoring the line which starts with '#'
  if line == 'done' :
    break
  print(line)
print('Done!')
# > ej
# ej
# > it
# it
# > #test
# > aj
# aj
# > done
# Done!
```

### Definite Loops
```python
for i in [5,4,3,2,1] :
  print(i)
print('Blastoff')
# 5
# 4
# 3
# 2
# 1
# Blastoff

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
  print('Happy New Year:', friend)
print('Done!')
# Happy New Year: Joseph
# Happy New Year: Glenn
# Happy New Year: Sally
# Done!
```
### Finding the Largest Value
```python
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 23, 37, 74, 15] :
  if the_num > largest_so_far :
    largest_so_far = the_num
  print(largest_so_far, the_num)
print('After', largest_so_far)
# Before -1
# 9 9
# 41 41
# 41 23
# 41 37
# 74 74
# 74 15
# After 74
```

### Loop idioms
```python
# Counting in a Loop
zork = 0
print('Before', zork)
for thing in [9, 41, 23, 12, 5, 52, 15] :
  zork = zork + 1
  print(zork, thing)
print('After', zork)
# Before 0
# 1 9
# 2 41
# 3 23
# 4 12
# 5 5
# 6 52
# 7 15
# After 7

# Summing in a Loop
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
  zork = zork + thing
  print(zork, thing)
print('After', zork)
# Before 0
# 9 9
# 50 41
# 62 12
# 65 3
# 139 74
# 154 15
# After 154

#Search Using a Boolean Variable
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
  if value == 3 :
    found = True
  print(found, value)
print('After', found)
Before False
# False 9
# False 41
# False 12
# True 3
# True 74
# True 15
# After True # There's a 3 in a list

# Finding the Smallest Value
# None value
smallest = None
print('Before', smallest)
for value in [41, 9, 23, 37, 74, 15] :
  if smallest is None :
    smallest = value
  elif value < smallest:
    smallest = value
  print(smallest, value)
print('After', smallest)
# Before None
# 41 41
# 9 9
# 9 23
# 9 37
# 9 74
# 9 15
# After 9
```

### is, is, ==, != not operator

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# 비교
print(a == b)       # True - 값이 같음
print(a is b)       # False - 서로 다른 객체임

print(a != b)       # False - 값이 같기 때문에 False
print(a is not b)   # True - a와 b가 같은 객체가 아님

print(a is c)       # True - a와 c는 같은 객체를 가리킴
```

### Strings
```python
fruit = 'banana'
index = 0
letter = fruit[1]
print(letter)
# a
print(len(fruit))
# 6
while index < len(fruit):
  letter = fruit[index]
  print(index, letter)
  index = index + 1

word = 'banana'
count = 0
for letter in word:
  if letter == 'a'
    count = count + 1
print(count)
# 3

# 'for in' method
for letter in fruit:
  print(letter)


# while method
index = 0
while index < len(fruit):
  letter = fruit[index]
  print(letter)
  index = index + 1

zot = 'abc'
print(zot[5])
# Index Error

# Slicing Strings
s = 'Monty Python'
print(s[0:4]) # Mont
print(s[6:7]) # P
print(s[6:20]) # Python
```

### Manipulating Strings
```python
fruit = 'banana'
'n' in fruit # True
'm' in fruit # False
'nan' in fruit # True
if 'a' in fruit:
  print('Found it') # Found it

greet = 'Hello Bob'
zap = greet.lower()
print(zap) # hello bob
print(greet) # Hello Bob

fruit = 'banana'
pos = fruit.find('na')
print(pos) # 2
aa = fruit.find('z')
print(aa) # -1

# Search and Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr) # Hello Jane
nstr = greet.replace('o', 'x')
print(nstr) # Hellx Bxb

# Stripping Whitespace
greet = '    Hello Bob    '
greet.lstrip() # 'Hello Bob    '
greet.rstrip() # '    Hello Bob'
greet.strip() # 'Hello Bob'

```