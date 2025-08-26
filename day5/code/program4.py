# frozenset
# - is immutable set
# - once created can not be updated

def function1():
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

    # frozen set of numbers
    # - duplicates are NOT allowed
    numbers_frozenset = frozenset([10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40])
    print(f"numbers_frozenset = {numbers_frozenset}, type = {type(numbers_frozenset)}")

# function1()

def function2():
    numbers = frozenset([10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40])

    # frozenset does not support mutability
    # numbers.add(40)

# function2() 

def function3():
    # set of numbers
    s1 = frozenset(10, 20, 30, 40, 50)
    s2 = frozenset(40, 50, 60, 70, 80)

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
