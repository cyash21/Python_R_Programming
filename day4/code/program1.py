# List
# - collection of similar or dissimilar values
# - mutable
# - no contiguous memory allocation

def function1():
    # list of numbers
    numbers = [10, 20, 40, 50]
    print(numbers)
    
    # insert 30 between 20 and 40 (one the position of 40)
    numbers.insert(2, 30)
    print(numbers)
    
    # append a value at the end of the list
    numbers.append(60)
    print(numbers)

    # append multiple values at the end of the list
    numbers.extend([70, 80, 90, 100])
    print(numbers)

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    # remove the last value from the list
    numbers.pop()
    print(numbers)

    # remove by index
    # remove a value using index position
    numbers.pop(1)
    print(numbers)

    # remove by value
    # remove a value using value (not the position)
    numbers.remove(30)
    print(numbers)

    # remove all the values
    numbers.clear()
    print(numbers)

# function2()

def function3():
    # list allows duplicate values
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
    print(numbers)
    print(f"no of items present in numbers: {len(numbers)}")

    # find how many time the value 10 is repeated 
    print(f"10 is repeated {numbers.count(10)} times")
    print(f"50 is repeated {numbers.count(50)} times")

    # if the value is missing, the code DOES NOT raise any exception
    # instead the count() returns 0
    print(f"150 is repeated {numbers.count(150)} times")

# function3()

def function4():
    # list allows duplicate values
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
    print(numbers)
    
    # find the repeatation count
    print(f"20 is present {numbers.count(20)} times")

    # find the position of 20
    # index() accepts 2 parameters
    # param1: value 
    # param2: start position (default to 0)
    # print(f"20 is present on {numbers.index(20, 0)} position")
    print(f"20 is present on {numbers.index(20)} position")
    print(f"20 is present on {numbers.index(20, 2)} position")
    print(f"20 is present on {numbers.index(20, 7)} position")

# function4()

def function5():
    # iterative over the numbers collection
    # for number in numbers:
    #     print(f"number = {number}")

    # traditional for loop in C
    # for (index i = 0; i < 10; i++) { printf("i = %d", i); }

    # but python DOES NOT support traditional for loop

    # create a new list of positions to iterate
    # positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # generate a sequence of values
    # param1: start position (default value = 0)
    # param2: stop position (stop value is excluded)
    # param3: step count (how to generate next value) (default value = 1)
    # positions = range(0, 10, 1)
    # positions = range(0, 10)
    # positions = range(10)

    # [0, 2, 4, 6, 8]
    # positions = range(0, 10, 2)

    # [0, 3, 6, 9]
    positions = range(0, 10, 3)
    for index in positions:
        print(f"index = {index}")

    # _ is used when a variable is not required (or you want to ignore it)
    # for _ in range(5):
    #     print(f"hello world")

# function5()

def function6():
    # list of numbers
    numbers = [10, 20, 10, 30, 70, 80, 20, 10, 50, 60, 90]

    # find the positions of 10
    # step1: find the count of value 10
    count = numbers.count(10)

    # declare a start position
    start_position = 0

    # step2: run for loop for count times
    for _ in range(count):
        # step3: find the next position value 10
        position = numbers.index(10, start_position)
        print(f"position of value 10 = {position} from {start_position}")

        # step4: change the start position
        start_position = position + 1

# function6()

def function7():
    # list of numbers
    numbers = [10, 20, 10, 30, 70, 80, 20, 10, 50, 60, 90]
    print(numbers)

    # this will remove only the first occurrence of value 10
    # numbers.remove(10)
    # print(numbers)

    # numbers.remove(10)
    # print(numbers)

    # numbers.remove(10)
    # print(numbers)

    # remove all occurrences of value 10
    count = numbers.count(10)
    for _ in range(count):
        numbers.remove(10)
    print(numbers)

# function7()

def function8():
    # list of numbers
    numbers = [10, 20, 10, 30, 70, 80, 20, 10, 50, 60, 90]
    print(numbers)

    # start position
    start_position = 0

    # create a list to hold all the positions
    all_positions = []

    # find the count of value 10
    count = numbers.count(10)
    for _ in range(count):
        position = numbers.index(10, start_position)
        start_position = position + 1

        # append the positions of 10
        all_positions.append(position)

    print(f"value 10 is present on: {all_positions} positions")

    # remove values from all the position
    delete_position = 0
    for position in all_positions:
        print(f"deleting value at {position} position")
        numbers.pop(position - delete_position)
        delete_position = delete_position + 1

    print(numbers)

# function8()

def function9():
    # list of numbers
    numbers = [30, 50, 10, 20, 40, 80]
    print(numbers)

    # sort the list in ascending order
    # numbers.sort()
    # print(numbers)

    # sort the list in descending order
    numbers.sort(reverse=True)
    print(numbers)

    # reverse the list
    # numbers.reverse()
    # print(numbers)

# function9()

def function10():
    # list of numbers
    numbers = [30, 50, 10, 20, 40, 80]
    print(f"numbers = {numbers}")

    # create a new copy of numbers with all the values
    # this is an example of deep copy of a list
    numbers2 = numbers.copy()
    print(f"numbers2 = {numbers2}")

    # this will NOT create a separate copy of numbers
    # instead henceforth both numbers2 and numbers will share
    # the same memory, which means, modifying either will 
    # update the another
    # - this is an example of shallow copy of a list 
    # numbers2 = numbers

    # sort the list
    numbers.sort()
    print(f"numbers = {numbers}")
    print(f"numbers2 = {numbers2}")


function10()



