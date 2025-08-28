# importing a module
# - loading the code of one module in another
# - achieved by using import keyword

print(f"module name of program4 = {__name__}")

# import entire module named program3
import program3

# call the add function defined by program3
program3.add(10, 20)

# call the subtract function defined by program3
program3.subtract(10, 20)

# access a variable/constant from program3
print(f"pi = {program3.PI}")