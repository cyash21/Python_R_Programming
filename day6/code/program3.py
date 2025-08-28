# module
# - a file with .py or .pyc extension
# - a way to reuse the code in python
# - every module has a name which is stored in __name__ variable
# - __name__ contains
#   - __main__ for the module which is currently executing
#   - name of the file for the module which is imported
# package
# - collection of modules

# declare a constant
PI = 3.14

def add(p1, p2):
    print(f"inside program3 add")
    print(f"{p1} + {p2} = {p1 + p2}")

def subtract(p1, p2):
    print(f"inside program3 subtract")
    print(f"{p1} - {p2} = {p1 - p2}")


# only when program3 gets executed
if __name__ == '__main__':
    print(f"module name of program3 = {__name__}")
    print("code written in program3")
    add(100, 200)
    subtract(100, 200)