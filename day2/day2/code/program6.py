# explicit type conversion

# convert any value to integer
# - the conversion is done using a built in function: int()
salary = 15.60
print(f"salary = {salary}, type = {type(salary)}")

# float to int
salary_int = int(salary)
print(f"salary_int = {salary_int}, type = {type(salary_int)}")

# string to int
value1 = int("10")
print(f"value1 = {value1}, type = {type(value1)}")

# string to int
# this conversion will lead to exception and application crash
# since the value "abc" can not be converted to int
# value2 = int("abc")
# print(f"value2 = {value2}, type = {type(value2)}")
# print(f"'' in int = {int('')}")

# boolean to int
print(f"True in int = {int(True)}")
print(f"False in int = {int(False)}")
# print(f"None in int = {int(None)}")

print('------')

# convert any value to float
print(f"10 in float = {float(10)}")
print(f"'10.50' in float = {float('10.50')}")
# print(f"'abc' in float = {float('abc')}")
print(f"True in float = {float(True)}")
print(f"False in float = {float(False)}")
# print(f"None in float = {float(None)}")


print('------')

# convert any value to string
print(f"10 in string = {str(10)}")
print(f"15.60 in string = {str(15.60)}")
print(f"True in string = {str(True)}") # 'True'
print(f"False in string = {str(False)}") # 'False'
print(f"None in string = {str(None)}") # 'None'

print('------')

# convert any value to boolean
# - only 0 in integer will get converted to False (bool),
#   rest all integers (+ve or -ve) will get converted to True
# - only empty string gets converted to False (bool)
#   non-empty string gets converted to True (bool)

print(f"1 in boolean = {bool(1)}")
print(f"10 in boolean = {bool(10)}")
print(f"-10 in boolean = {bool(-10)}")
print(f"0 in boolean = {bool(0)}")
print(f"'True' in boolean = {bool('True')}")
print(f"'False' in boolean = {bool('False')}")
print(f"'' in boolean = {bool('')}")
print(f"' ' in boolean = {bool(' ')}") # True
print(f"None in boolean = {bool(None)}")

