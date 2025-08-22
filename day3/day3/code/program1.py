# parameter less function
def function1():
    """
    this is a dummy function
    """
    print("inside function1")

# function1()
# print(function1.__name__)
# print(function1.__doc__)

# non-returning function
# - does not return any value
def function2(param1, param2):
    addition = param1 + param2
    print(f"addition = {addition}")

# function2 by default returns None
# my_addition_var will contain the value None 
# my_addition_var = function2(10, 20)
# print(f"my_addition_var = {my_addition_var}")

def function3(param1, param2):
    addition = param1 + param2
    return addition
    # any statement after return will be ignored 
    # because the function exits after return statement
    # print("this is a line after return statement")

# function3(10, 20)

def function4(param1, param2) -> int: 
    return param1 + param2

# function4 gets called and addition variable captures
# the value returned by the function4
addition = function4(10, 20)
print(f"addition = {addition}")
print(f"addition = {function4(10, 20)}")


def calculate_simple_interest(p, n, r):
    interest = (p * n * r) / 100
    return interest
    
# result = calculate_simple_interest(10000, 2, 8.5)
# result = calculate_simple_interest(p=10000, n=2, r=8.5)
result = calculate_simple_interest(p=10000, r=8.5, n=2)
print(f"result = {result}, type = {type(result)}")

# def function5():
#     return None
