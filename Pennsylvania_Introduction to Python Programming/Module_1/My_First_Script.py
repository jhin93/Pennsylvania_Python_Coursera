def numeric_to_letter_grade(grade):
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")
        

grade = input('Enter a numeric grade: ')
grade = int(grade)
numeric_to_letter_grade(grade)