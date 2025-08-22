# list
# - collection of similar or dissimilar values

def function1():
    # create an empty list
    list1 = []
    print(f"list1 = {list1}, type = {type(list1)}")

    # create an empty list
    # list() is a built in function used to convert any 
    # collection to list 
    list2 = list([])
    print(f"list2 = {list2}, type = {type(list2)}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}, type = {type(numbers)}")

    # len() is a built in function
    print(f"length of list = {len(numbers)}")

    # list of countries
    countries = ["india", "usa", "uk", "japan", "bhutan"]
    print(f"countries = {countries}, type = {type(countries)}")

    # list of mixed values
    mixed_values = [10, "test1", 15.60, True, False, 20, "test2"]
    print(f"mixed_values = {mixed_values}, type = {type(mixed_values)}")

# function2()

def function3():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # for..in loop
    # for every value in numbers: perform the operation
    for value in numbers:
        print(f"value = {value}, square = {value ** 2}")

    print('-' * 50)

    # list of countries
    countries = ["india", "usa", "uk", "japan", "bhutan"]
    for country in countries:
        print(f"country = {country}")

    print('-' * 50)

    # list of mixed values
    mixed_values = [10, "test1", 15.60, True, False, 20, "test2"]
    for value in mixed_values:
        print(f"value = {value}, type = {type(value)}")

# function3()
    
def function4():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}")
    
    # add a new value at the end of the list
    numbers.append(60)
    print(f"numbers = {numbers}")

    # add a new value at the end of the list
    numbers.append(70)
    print(f"numbers = {numbers}")

# function4()

def function5():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}")
    
    # add multiple values at the end of the list
    numbers.extend([60, 70])
    print(f"numbers = {numbers}")

    # add multiple values at the end of the list
    numbers.extend([80, 90, 100])
    print(f"numbers = {numbers}")

# function5()

def function6():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}")

    # add a value 15 between 10 and 20
    numbers.insert(1, 15)
    print(f"numbers = {numbers}")

# function6()

def function7():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}")
    
    # remove the last value from the list
    numbers.pop()
    print(f"numbers = {numbers}")

    # remove the last value from the list
    numbers.pop()
    print(f"numbers = {numbers}")

    # remove the last value from the list
    numbers.pop()
    print(f"numbers = {numbers}")

    # remove the last value from the list
    numbers.pop()
    print(f"numbers = {numbers}")

    # remove the last value from the list
    numbers.pop()
    print(f"numbers = {numbers}")

    # - remove the last value from the list
    # - pop will raise an exception and will crash app
    #   if the list is empty
    # numbers.pop()
    # print(f"numbers = {numbers}")

# function7()

def function8():
    # list of countries
    countries = ["india", "usa", "uk", "china", "japan"]
    print(f"countries = {countries}")

    # remove china using index position from countries 
    # pop(3): remove the value at 3rd position/index
    countries.pop(3)
    print(f"countries = {countries}")
    
    # remove usa using value
    countries.remove("usa")
    print(f"countries = {countries}")

function8()




    

