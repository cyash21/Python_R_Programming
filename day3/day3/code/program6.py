# calling convention
# - the way the function gets arguments
# - python uses C calling convention
#   - parameters will be assigned from left to right
# passing parameters
# - all parameters of a function are mandatory (required)
# - indexed parameters
#   - the first parameter gets assigned to the first argument
#   - the second parameter gets assigned to the second argument
# - named parameters
#   - passing parameter along with the parameter name 
#   - order of parameters can be changed

def function1(num1, num2):
    print(f"inside function1")
    print(f"num1 = {num1}, type = {type(num1)}")
    print(f"num2 = {num2}, type = {type(num2)}")

# index parameters
# function1(10, 20)
# function1(20, 10)
# function1("test1", "test2")
# function1(10, "test2")

# named parameters
# function1(num1=10, num2=20)
# function1(num2=20, num1=10)

# mixed behavior
# function1(10, num2=20)