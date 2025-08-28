def add(p1, p2):
    print(f"in program7 add")
    print(f"{p1} + {p2} = {p1 + p2}")

def subtract(p1, p2):
    print(f"in program7 subtract")
    print(f"{p1} - {p2} = {p1 - p2}")

# import program3

# program3.add(80, 90)
# program3.subtract(80, 90)

# from program3 import add, subtract

# setting an alias to add from program3
from program3 import add as my_add

# setting an alias to subtract from program3
from program3 import subtract as program3_subtract

add(60, 70)
subtract(60, 70)

my_add(80, 90)
program3_subtract(80, 90)