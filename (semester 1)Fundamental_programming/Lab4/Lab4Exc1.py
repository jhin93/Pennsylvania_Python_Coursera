import math
from tabulate import tabulate

table = []
for i in range(1, 10):  
    table.append([i, round(math.sqrt(i), 2), i**2])

print(tabulate(table, headers=["Number", "Square Root", "Square"], tablefmt="grid"))





