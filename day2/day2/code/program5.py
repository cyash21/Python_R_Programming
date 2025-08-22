# type hint
# - optional 
# - used only for reading the code or for IDEs/editors
# - when compiler decides the data type, the type hint is ignored

# data type : int
num: int = 200
print(f"num = {num}, type = {type(num)}")

# data type : float (type hint will be ignored)
salary: int = 15.60
print(f"salary = {salary}, type = {type(salary)}")
