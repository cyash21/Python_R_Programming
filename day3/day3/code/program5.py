num1 = 200
print(f"num1 = {num1}, type = {type(num1)}")

num2 = num1
print(f"num2 = {num2}, type = {type(num2)}")

num1 = 500
print(f"num1 = {num1}, type = {type(num1)}")
print(f"num2 = {num2}, type = {type(num2)}")

print('-' * 50)

def function1():
    print(f"inside function1")

print(f"function1 = {function1}, type = {type(function1)}")

# function reference
my_function1 = function1
print(f"my_function1 = {my_function1}, type = {type(my_function1)}")

function1()
my_function1()

my_function2 = my_function1
my_function2()