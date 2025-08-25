# slicing
# - reading a sequential part of a collection
# - use [] with range parameters separated by :
#   - param1: start position
#   - param2: stop position
#   - param3: step count

def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # [30, 40, 50, 60]
    new_values = []
    for index in range(2, 6):
        new_values.append(numbers[index])
    print(f"new_values = {new_values}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # [30, 40, 50, 60]
    print(f"numbers[2:6:1] = {numbers[2:6:1]}")
    print(f"numbers[2:6] = {numbers[2:6]}")
    print('-' * 80)
    
    # [10, 20, 30, 40, 50]
    print(f"numbers[0:5:1] = {numbers[0:5:1]}")
    print(f"numbers[0:5] = {numbers[0:5]}")
    print(f"numbers[:5] = {numbers[:5]}")
    print('-' * 80)

    # [60, 70, 80, 90, 100]
    print(f"numbers[5:10:1] = {numbers[5:10:1]}")
    print(f"numbers[5:10] = {numbers[5:10]}")
    print(f"numbers[5:] = {numbers[5:]}")
    print('-' * 80)

    # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers[0:10:1] = {numbers[0:10:1]}")
    print(f"numbers[0:10] = {numbers[0:10]}")
    print(f"numbers[0:] = {numbers[0:]}")
    print(f"numbers[:] = {numbers[:]}")

# function2()


def function3():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # read the values on even index positions
    # [0, 2, 4, 6, 8] => []
    print(f"numbers[0:10:2] = {numbers[0:10:2]}")

    # read the values on odd index positions
    # [1, 3, 5, 7, 9] => []
    print(f"numbers[1:10:2] = {numbers[1:10:2]}")
    print(f"numbers[1::2] = {numbers[1::2]}")

    # get the entire list reversed
    # this way, the original list does not get modified
    # instead, new list is created with all values reversed
    print(f"numbers[::-1] = {numbers[::-1]}")

# function3()

def function4():
    # tuple of numbers
    numbers = 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

    print(f"numbers[::-1] = {numbers[::-1]}")

# function4()

