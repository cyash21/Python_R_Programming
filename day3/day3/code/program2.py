# scope of variables

# scope: global
num = 200
print(f"in global scope before function2 modifies num, num = {num}")

num = 500
print(f"in global scope before function2 modifies num, num = {num}")


def function1():
    print(f"inside function1")

    # scope: local to the function1
    name = "steve"
    print(f"name = {name}")

    name = "bill"
    print(f"name = {name}")

    # accidental change in function1
    # function1 creates a local copy of global num
    # which is why, the global variable num wont get updated
    num = 200

    # accessing the global variable
    print(f"after updating, num = {num}")


# function1()
# since the name variable is local to function1
# it can NOT be accessed outside of function1
# print(f"in global scope, name = {name}")


def function2():
    # - from this line, let me access and update the global num
    #   the updates to the global variable will be persisted
    # - even after function2 exits, the global variable num will 
    #   store the value 400 instated of 200
    # - global keyword is not required to access the 
    #   value of global variable
    # - global keyword is required only when global variable
    #   needs update
    global num
    num = 400
    # num = 800
    # num = 100
    # num = 1000

    # accessing the global variable
    print(f"after updating, num = {num}")

# function2()
# print(f"in global scope after function2 modifies num, num = {num}")

# # scope: global
# name = "sunbeam"

def function3(param):
    # print(f"my_var = {my_var}")
    if param == True:
        my_var = 200
    else:
        my_var = 300
    print(f"my_var = {my_var}")

function3(False)
