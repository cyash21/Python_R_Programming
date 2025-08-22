# variables
# - named location which is used to store data (value)
# - variable data type is inferred
# - inferred: automatically decided by language
# - type()
#   - in built function
#   - used to get type of a variable

# to read value of a variable in a string
# - use formatted string (f"")
# - wrap the variable name using {}


# integer data type
# initialization: assigning a value for the first time
num = 200
print(f"num = {num}, type = {type(num)}")

# float data type
salary = 15.60
print(f"salary = {salary}, type = {type(salary)}")

# complex data type
complex_var = 10 + 5j
print(f"complex_var = {complex_var}, type = {type(complex_var)}")

# assignment of a value
# this assignment simply will overwrite the previous value
num = 300
print(f"num = {num}, type = {type(num)}")

# assignment of a value
# since '300' is a string literal, 
# the data type of num changes to str
# and a new memory will be allocated to accomodate the new value
num = '300'
print(f"num = {num}, type = {type(num)}")

num = True
print(f"num = {num}, type = {type(num)}")
