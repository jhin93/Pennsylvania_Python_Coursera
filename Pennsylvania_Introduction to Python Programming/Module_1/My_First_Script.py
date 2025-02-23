
a = 2
print(a)

b = 3
print(b)

age = input("enter your age: ")
age = int(age)
print("You are an adult: ", age > 26)

age = input("Enter your age: ")
try:
    age = int(age)
    print('How old will you be in 1 year? ', age + 1)
except ValueError:
    print("The given age is not valid")