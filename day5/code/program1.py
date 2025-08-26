def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]

    # positive index: starts with 0 and goes till len() - 1
    print(f"first value = {numbers[0]}")
    print(f"last value = {numbers[len(numbers) - 1]}")
    print("-" * 80)

    # negative index: start with -len() and goes till -1
    print(f"first value = {numbers[-len(numbers)]}")
    print(f"last value = {numbers[-1]}")

# function1()

def function2():
    # list of numbers
    numbers1 = [10, 20, 30, 40, 50]
    print(f"numbers1 = {numbers1}")

    # shallow copy
    # - does NOT create a separate memory, instead it creates 
    #   a new reference and refers the old memory
    # - if one of the references is used to update the collection,
    #   the other one will also get updated
    numbers2 = numbers1
    print(f"numbers2 = {numbers2}")

    # deep copy
    # - create a new reference along with separate memory
    #   to store the data
    # - updating one, wont affect another
    numbers3 = numbers1.copy()
    print(f"numbers3 = {numbers3}")

    # update numbers1
    # - since numbers2 is a shallow copy, the following 
    #   statement will also affect the numbers2
    # - but the numbers3 is a deep copy, the following statement
    #   wont affect it
    numbers1.append(60)
    numbers1.append(70)

    print(f"numbers1 = {numbers1}")
    print(f"numbers2 = {numbers2}")
    print(f"numbers3 = {numbers3}")

# function2()

# - function3 now can accepts variable number of parameters
# - it can accept any number of parameters without declaration
# - all the indexed/positional arguments will be collected in args as a tuple
# - all the named arguments will be collected in kwargs as a dictionary
def function3(my_param, *args, **kwargs):
    print(f"my_param = {my_param}, type = {type(my_param)}")
    print(f"args = {args}, type = {type(args)}")
    print(f"kwargs = {kwargs}, type = {type(kwargs)}")
    result, max = 0, 0
    for number in args:
        result += number
        if number > max:
            max = number
    print(f"addition = {result}, max = {max}")
    print('-' * 80)

# calling function with indexed parameters
# function3(10)
# function3(10, 20)
# function3(10, 20, 30)
# function3(10, 20, 30, 40)
# function3(10, 20, 30, 40, 50)

# calling the function with named parameters
# function3(100, operation="addition")

def function4(p1, p2):
    print(f"p1 = {p1}, p2 = {p2}")

# indexed or positional parameters
# function4(10, 20)

# named parameter
# function4(p1=10, p2=20)


def function5():
    print(f"hello", end="-")
    print(f"world", end="\n")
    print(f"my name is amit")

function5()