# set
# - collection of unique values of similar or dissimilar values
# - is mutable collection
# - NOT an ordered collection
#   - you can not retrieve the values using index ([])
#   - NOT subscriptable 
# - does not honor the insertion order
#   - the values added to a set will not follow the insertion order
#   - because, set uses hash function to decide the 
#     position/index of an element

def function1():
    # the following variable is NOT of type set, it is of type dict
    # empty_set = {}
    # print(f"empty_set = {empty_set}, type = {type(empty_set)}")

    # create an empty set
    empty_set = set()
    print(f"empty_set = {empty_set}, type = {type(empty_set)}")

# function1()

def function2():
    # list of numbers
    # - duplicates are allowed
    numbers_list = [10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]
    print(f"numbers_list = {numbers_list}, type = {type(numbers_list)}")
    
    # tuple of numbers
    # - duplicates are allowed
    numbers_tuple = 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40
    print(f"numbers_tuple = {numbers_tuple}, type = {type(numbers_tuple)}")

    # set of numbers
    # - duplicates are NOT allowed
    numbers_set = {10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40}
    print(f"numbers_set = {numbers_set}, type = {type(numbers_set)}")

# function2()

def function3():
    # create an empty set
    s1 = set()

    # add the values dynamically
    s1.add(10)
    s1.add(20)
    s1.add(30)
    s1.add(10)
    s1.add(10)

    print(f"s1 = {s1}")
    s1.add(40)
    s1.add(50)
    s1.add(60)
    print(f"s1 = {s1}")
    print("-" * 80)

    # read the first value from set
    # can NOT read value using subscript
    # print(f"s1[0] = {s1[0]}")

    # read all the values from set
    for value in s1:
        print(f"value = {value}")
    print("-" * 80)

    # convert the set to list
    list_s1 = list(s1)
    print(f"list_s1 = {list_s1}")
    print(f"list_s1[0] = {list_s1[0]}")
    print("-" * 80)

    # convert the set to tuple
    tuple_s1 = tuple(s1)
    print(f"tuple_s1 = {tuple_s1}")
    print(f"tuple_s1[0] = {tuple_s1[0]}")

# function3()

def function4():
    # set of numbers
    s1 = {10, 20, 30, 40, 50}
    s2 = {40, 50, 60, 70, 80}

    # intersection
    print(f"s1 intersection s2 = {s1.intersection(s2)}")
    print(f"s2 intersection s1 = {s2.intersection(s1)}")
    print(f"-" * 80)

    # union
    print(f"s1 union s2 = {s1.union(s2)}")
    print(f"s2 union s1 = {s2.union(s1)}")
    print(f"-" * 80)

    # subtraction
    print(f"s1 - s2 = {s1 - s2}")
    print(f"s2 - s1 = {s2 - s1}")
    print(f"-" * 80)

# function4()

def function5():
    # list of strings
    names = ["amit", "nilesh", "vishal", "nilesh", "amit", "amit", "nitin"]
    print(f"names = {names}")
    
    # find the unique names from the collection
    # convert the list to a set
    names_set = set(names)
    print(names_set)

# function5()


