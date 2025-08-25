# collection indexing
# - reading a value from collection using positions
# - types
#   - positive indexing
#     - the index starts from 0 to the count of list - 1
#     - it starts from left to right
#   - negative indexing
#     - using -ve index position to read a value from collection
#     - the -1 represents the last value
#     - the -len(collection) represents the first value
#     - -ve indexing starts at -len(collection) and it goes till -1
#     - before the code gets compiled, python subtracts the negative
#       index from len(collection)
#       - e.g. numbers[-1] => numbers[len(numbers)-1]
# - applicable for both list as well tuple


def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]

    # positive indexing
    print(f"numbers[0] = {numbers[0]}")
    print(f"numbers[1] = {numbers[2]}")
    print(f"numbers[2] = {numbers[1]}")
    print(f"numbers[3] = {numbers[3]}")
    print(f"numbers[4] = {numbers[4]}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]

    # read value at -1 index
    # print(f"last value (numbers[-1]) = {numbers[len(numbers)-1]}")
    # print(f"last value (numbers[-1]) = {numbers[-1]}")

    # negative indexing
    print(f"last value (numbers[-1]) = {numbers[-1]}")
    print(f"numbers[-2] = {numbers[-2]}")
    print(f"numbers[-3] = {numbers[-3]}")
    print(f"numbers[-4] = {numbers[-4]}")
    print(f"first value (numbers[-5]) = {numbers[-5]}")
    print(f"first value (numbers[-len(numbers)]) = {numbers[-len(numbers)]}")

function2()
