# 1. 변수와 자료형
# 정수형
a = 10
print(type(a))  # <class 'int'>

# 실수형
b = 20.5
print(type(b))  # <class 'float'>

# 문자열
text = "Hello, Python"
print(type(text))  # <class 'str'>


# 2. 리스트와 튜플
# 리스트
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # 요소 추가
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# 튜플
colors = ("red", "green", "blue")
print(colors[1])  # green
# 리스트는 요소를 추가, 삭제, 수정할 수 있지만, 튜플은 불변(immutable)이라서 수정할 수 없어.

# 3. 딕셔너리
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"])  # Alice

# 새로운 키-값 추가
person["job"] = "Developer"
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Developer'}
# 키-값 쌍으로 데이터를 저장하는 자료형으로, JSON 형식과 유사해.

# 4. List Comprehension
# 1부터 10까지의 제곱을 리스트로 생성
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 조건을 추가하여 짝수의 제곱만 생성
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]
# 리스트를 생성할 때 간결하게 표현할 수 있는 방법이야.

# 5. 함수
# 파이썬에서는 def 키워드를 사용하여 함수를 정의할 수 있어.
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!
# 기본값 매개변수를 설정할 수도 있어.
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Hello, Guest!

# 6. 람다 함수(Lambda Function)
# 두 수의 합을 구하는 람다 함수
add = lambda x, y: x + y
print(add(3, 5))  # 8

# 리스트의 정렬 기준으로 람다 사용
names = ["Alice", "Bob", "Charlie"]
names.sort(key=lambda name: len(name))  # 이름 길이 기준으로 정렬
print(names)  # ['Bob', 'Alice', 'Charlie']
# 람다는 간단한 함수를 한 줄로 정의할 때 사용해.

# 7. 파일 입출력
# 파일 쓰기
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# 파일 읽기
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Hello, World!
# with 문은 파일 작업이 끝나면 자동으로 파일을 닫아줘서 메모리 누수를 방지할 수 있어.

# 8. 예외처리(Exception handling)
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Cannot divide by zero!
else:
    print("Division successful")
finally:
    print("This code runs no matter what")  # 무조건 실행됨

# 9. Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# 객체 생성
p1 = Person("Alice", 30)
p1.introduce()  # My name is Alice and I am 30 years old.

# 10. Module & Library
import math

print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793
