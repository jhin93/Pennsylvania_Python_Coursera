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