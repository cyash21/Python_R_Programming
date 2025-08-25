# tuple
# - collection of similar or dissimilar values
# - tuple is immutable 
# - once created, it can NOT be changed 
#   (adding/removing from tuple is NOT possible)
# - when the values are not going to change, 
#   prefer tuple over list
# - in any language, the immutable collection is faster 
#   and memory efficient than the mutable version 

def function1():
    # create an empty tuple
    tuple1 = ()
    print(f"tuple1 = {tuple1}, type = {type(tuple1)}")

    # create an empty tuple
    # tuple() is a built in function used to convert any
    # collection to tuple
    tuple2 = tuple([])
    print(f"tuple2 = {tuple2}, type = {type(tuple2)}")

# function1()
    
def function2():
    # list with one value
    list1 = [10]
    print(f"list1 = {list1}, type = {type(list1)}")

    list2 = ["test"]
    print(f"list2 = {list2}, type = {type(list2)}")

    print("-" * 80)

    # though it looks like a tuple with one value
    # internally python degrades it to an int variable
    # tuple1 = 10
    tuple1 = (10)
    print(f"tuple1 = {tuple1}, type = {type(tuple1)}")

    # though it looks like a tuple with one value
    # internally python degrades it to an string variable
    # tuple2 = "test"
    tuple2 = ("test")
    print(f"tuple2 = {tuple2}, type = {type(tuple2)}")

    print("-" * 80)

    # tuple with one value
    tuple3 = (10,)
    print(f"tuple3 = {tuple3}, type = {type(tuple3)}")

    tuple4 = ("test",)
    print(f"tuple4 = {tuple4}, type = {type(tuple4)}")

    # tuple with no value but a comma
    # this leads to a syntax error
    # tuple5 = (,)

# function2()

def function3():
    # tuple of numbers
    numbers1 = (10, 20, 30, 40, 50)
    print(f"numbers1 = {numbers1}, type = {type(numbers1)}")

    # tuple of numbers
    numbers2 = 10, 20, 30, 40, 50
    print(f"numbers2 = {numbers2}, type = {type(numbers2)}")

# function3()

def function4():
    # tuple of numbers
    numbers = (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
    print(numbers)

    # append a value at the end of the collection
    # numbers.append(60)
    # print(numbers)

    # find the no of occurrences of 10
    print(f"10 is repeated = {numbers.count(10)}")
    print(f"10 is present on {numbers.index(10)} position")
    print(f"10 is present on {numbers.index(10, 1)} position")
    
# function4()

def function5():
    # tuple of numbers

    # tuple packing
    # - python will pack the values 10 and 20 in a tuple collection
    numbers = 10, 20
    print(f"value at 0th index = {numbers[0]}")
    print(f"value at 1st index = {numbers[1]}")

    # tuple unpacking
    # - separating the values of a tuple in individual variables
    # - in the following statement, n1 and n2 will be variables 
    #   of type int
    # n1 = numbers[0]
    # n2 = numbers[1]
    n1, n2 = numbers
    print(f"n1 = {n1}, n2 = {n2}")

    # - it is mandatory to have same number of values as
    #   that the number of variables
    # - following code will raise an exception
    # n3, n4 = 10, 20, 30, 40
    # print(f"n3 = {n3}, n4 = {n4}")

    # while unpacking a tuple, only one "Rest of the values"
    # operator (*) is allowed
    # here n3 = 10
    # n4 = [20, 30, 40] => rest of the values
    n3, *n4 = 10, 20, 30, 40
    print(f"n3 = {n3}, n4 = {n4}")

    # n5 = 10, n6 = 20, n7 = [30, 40]
    # n5, n6, *n7 = 10, 20, 30, 40
    # print(f"n5 = {n5}, n6 = {n6}, n7 = {n7}")

    # n5 = 10, n6 = [20, 30], n7 = 40
    n5, *n6, n7 = 10, 20, 30, 40
    print(f"n5 = {n5}, n6 = {n6}, n7 = {n7}")

# function5()

def function6():
    # tuple packing and unpacking
    n1, n2 = 10, 20
    print(f"n1: {n1}, n2 = {n2}")

    # swapping the values of n1 and n2
    # n1, n2 = 20, 10
    n1, n2 = n2, n1
    print(f"n1: {n1}, n2 = {n2}")

function6()
