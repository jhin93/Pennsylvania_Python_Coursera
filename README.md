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