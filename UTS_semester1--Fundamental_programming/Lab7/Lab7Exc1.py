import random

# Step 1:
# Numbers has a numbers a field which is a list of integers
# Define a procedue "populate" that initializes the list as follows:
# List values are randomly generated integers between 1 and 100
# Read the initial list size from keyboard;
# Only populate the list if it is empty.
# Define a procedure "clear" that empties the list.
# Define a procedure "show" that shows the list

class Numbers:
    def __init__(self):
        self.list = []

    def populate(self):
        if len(self.list) == 0:
            self.list = [random.randint(1, 100) for _ in range(int(input("Enter the initial list size: ")))]

    def clear(self):
        if len(self.list) > 0:
            self.list.clear()

    def show(self):
        if len(self.list) > 0:
            print(self.list) 

numbers = Numbers()

def main():
    numbers.populate()
    numbers.show()
    numbers.clear()
    numbers.show()

if __name__ == "__main__":
    main()  
