# functional programming
# - function is considered as a first class citizen
# - function can be passed as a argument to another function
# - function can be returned as a return value of a function

# higher order function
# - function which take another function as an argument

def function1(param):
    # param = function2
    print("inside function1")
    print(f"param = {param}, type = {type(param)}")

    # since param is referring a function, it can be called
    param()

def function2():
    print("inside function2")

def function3():
    print("inside function3")

# function1(10)
# num = 10
# function1(num)
# print(f"function2 = {function2}, type = {type(function2)}")

# passing function2 as a parameter to function1
# function1(function2)
# function1(function3)

def perform_operation(function):
    print("inside perform operation")
    function(10, 20)

def add(p1, p2):
    print(f"{p1} + {p2} = {p1 + p2}")

def subtract(p1, p2):
    print(f"{p1} - {p2} = {p1 - p2}")

def multiply(p1, p2):
    print(f"{p1} * {p2} = {p1 * p2}")

def divide(p1, p2):
    print(f"{p1} / {p2} = {p1 / p2}")

def square(p1):
    print(f"square of p1 = {p1 ** 2}")

perform_operation(add)
perform_operation(subtract)
perform_operation(multiply)
perform_operation(divide)

# make sure the function is accepting only 2 params
# perform_operation(square)