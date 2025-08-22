# function
# - in python, function declaration and definition go together
# - function declaration or signature
#   - def <function name> (<parameters>):
# - function definition
#   - function body

# empty function
# parameter less function
# - function which does not have any statement in the body
def function1():
    pass

# function call or function invocation
# function1()

# parameter less function
# - function which does not take any input parameter
def function2():
    print(f"inside function2")
    print(f"another line in function2")
    
# function invocation
# function2()
# function2()
# function2()

# parameterized function
# - which accepts at least one parameter
def can_vote(age):
    if age >= 18:
        print(f"person is eligible")
    else:
        print(f"person is NOT eligible")

can_vote(19)
can_vote(15)
can_vote(50)
