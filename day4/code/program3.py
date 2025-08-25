# multi dimensional collection
# - collection of collections
# - e.g. list of lists, list of tuples, 
#   tuple of lists or tuple of tuples

def function1():
    # list of numbers (1D collection)
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}")

    # for number in numbers:
    #     print(f"number = {number}")

    print(f"numbers[0] = {numbers[0]}")
    print(f"numbers[1] = {numbers[1]}")
    print(f"numbers[2] = {numbers[2]}")
    print(f"numbers[3] = {numbers[3]}")
    print(f"numbers[4] = {numbers[4]}")


# function1()

def function2():
    # list of lists (3 rows x 2 columns)
    numbers = [
        [10, 20], # row 0
        [30, 40], # row 1
        [50, 60]  # row 2
    ]

    print(f"numbers = {numbers}")
    print(f"numbers[0] = {numbers[0]}")
    print(f"numbers[1] = {numbers[1]}")
    print(f"numbers[2] = {numbers[2]}")
    print('-' * 80)

    # read all the inner lists of numbers
    for values in numbers:
        # iterate over the inner list to read all the values
        for value in values:
            print(f"value = {value}")
        print(f"--")
    
    print('-' * 80)
    print(f"numbers[0][1] = {numbers[0][1]}")

    # update the value at [0][1]
    numbers[0][1] = 200
    print(numbers)

    # insert a new value in outer list (numbers)
    numbers.append([70, 80])
    print(numbers)

    # insert a new value inside the inner list
    numbers[0].append(400)
    print(numbers)
    
# function2()

def function3():
    # list of lists
    # it is not mandatory to have same number of columns in every row
    # as the multi dimensional collection is made of collections
    numbers = [
        [10, 20],
        [30, 40, 50],
        [60, 70, 80, 90]
    ]

    # read all the inner lists of numbers
    for values in numbers:
        # iterate over the inner list to read all the values
        for value in values:
            print(f"value = {value}")
        print(f"--")
    
# function3()

def function4():
    # list of tuples
    numbers = [
        (10, 20),
        (30, 40),
        (50, 60)
    ]

    print(f"numbers = {numbers}")

    # read all the inner lists of numbers
    for values in numbers:
        # iterate over the inner list to read all the values
        for value in values:
            print(f"value = {value}")
        print(f"--")

    print('-' * 80)

    print(f"numbers[0][1] = {numbers[0][1]}")

    # update the value at [0][1] is NOT possible as 
    # the inner member is a tuple
    # numbers[0][1] = 200

    # insert a new value in outer list (numbers)
    numbers.append([70, 80])
    print(numbers)

    # insert a new value inside the inner list
    # this is not possible as the inner member is a tuple
    # numbers[0].append(400)
    # print(numbers)

function4()