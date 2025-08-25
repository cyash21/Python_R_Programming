# variable length argument function
# - function which can accept variable number of arguments
# - one can pass any number of arguments to such function
# - such function accepts two parameters
#   - *args: 
#     - args is a tuple with all the arguments passed to the function
#     - args is NOT a keywords
#     - args can accept only indexed parameters

# def add(p1, p2, p3, p4, p5):
#     result = p1 + p2 + p3 + p4 + p5
#     print(f"result = {result}")

# def add(*args):
#     print(f"args = {args}, type = {type(args)}")
#     result = 0
#     for value in args:
#         result += value
#     print(f"result = {result}")

def add(*params):
    print(f"args = {params}, type = {type(params)}")
    result = 0
    for value in params:
        result += value
    print(f"result = {result}")


add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)
add(10, 20, 30, 40, 50)