# local function
# - function declared withing another function
# - rule
#   - inner function can access all the members of outer function
#   - but outer function CAN NOT access any member of inner function

# scope: global
def function1():
    print("inside function1")

    # scope: local
    num = 200
    print(f"before inner_function, num = {num}")

    # scope: local
    def inner_function1():
        print("inside inner_function1")

        # nonlocal keyword will let inner_function1
        # to update the value of num variable
        nonlocal num
        num = 600

        # inner function can access all the 
        # members (parameters/local variables) of outer function
        print(f"num = {num}")

        # scope: local
        my_var = 400
        print(f"my_var = {my_var}")

    # calling inner function from function1
    inner_function1()   
    print(f"after inner_function, num = {num}") 

    # since my_var is declared inside the inner function
    # it can NOT be accessed by the outer function
    # print(f"my_var = {my_var}")

function1()

# since inner_function1 is a inner function of function1
# it CAN NOT be called outside the function1
# inner_function1()

# num is a local variable of function1
# it can NOT be accessed outside of function1
# print(f"num = {num}")
