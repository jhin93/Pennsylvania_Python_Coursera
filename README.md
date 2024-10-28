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
```python
eee = 'hello ' + 'there'
print(eee)
# hello there

print(eee+1)
Traceback (most recent call last):
  File "/Users/kimjinkyeong/Desktop/python/py4e/hello.py", line 2, in <module>
    print(eee + 1)
          ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```
