# filter
# - is a higher order function
# - accepts
#   - param1: function / lambda to check a condition
#   - param2: collection
# - returns a filter object which can be converted to a list or a tuple
# - returns a collection which may have same size as that of the original one
# - always returns the original values when the condition is true

def function1():
    # list of numbers
    numbers = [2, 5, 7, 9, 11, 23, 8, 10, 40]

    # find the even numbers
    even_numbers = []
    for number in numbers:
        # check if the number is even
        if number % 2 == 0:
            # since the number is even
            even_numbers.append(number)

    print(f"numbers = {numbers}")
    print(f"even numbers = {even_numbers}")

# function1()

def function2():
    # list of numbers
    numbers = [2, 5, 7, 9, 11, 23, 8, 10, 40]

    # find the even numbers

    # checking logic
    is_even = lambda n: n % 2 == 0
    
    # iteration logic
    even_numbers = []
    for number in numbers:
        # check if the number is even
        if is_even(number):
            # since the number is even
            even_numbers.append(number)

    print(f"numbers = {numbers}")
    print(f"even numbers = {even_numbers}")

# function2()

def function3():
    # list of numbers
    numbers = [2, 5, 7, 9, 11, 23, 8, 10, 40]

    # checking logic
    is_even = lambda n: n % 2 == 0

    # iteration logic
    even_numbers = list(filter(is_even, numbers))

    print(f"numbers = {numbers}")
    print(f"even numbers = {even_numbers}")

# function3()

def function4():
    # list of numbers
    numbers = [2, 5, 7, 9, 11, 23, 8, 10, 40]

    # find the odd numbers

    # checking logic
    is_odd = lambda n: n % 2 != 0

    # iteration logic
    odd_values = list(filter(is_odd, numbers))

    print(f"numbers = {numbers}")
    print(f"odd numbers = {odd_values}")

# function4()

def function5():
    # list of dictionaries
    cars = [
        {"model": "triber", "company": "renault", "price": 10.0},
        {"model": "kwid", "company": "renault", "price": 7.0},
        {"model": "i20", "company": "hyundai", "price": 14.0},
        {"model": "i10", "company": "hyundai", "price": 10.0},
        {"model": "eon", "company": "hyundai", "price": 6.0},
        {"model": "nano", "company": "tata", "price": 3.0},
        {"model": "nexon", "company": "tata", "price": 13.0},
        {"model": "meridian", "company": "jeep", "price": 43.0},
        {"model": "compass", "company": "jeep", "price": 25.0},
        {"model": "defender", "company": "land rover", "price": 100.0},
        {"model": "range rover", "company": "land rover", "price": 200.0}
    ]

    # find all the cars of hyundai
    # hyundai_cars = []
    # for car in cars:
    #     if car['company'] == 'hyundai':
    #         hyundai_cars.append(car)

    # find all the cars of hyundai
    is_hyundai_car = lambda car: car['company'] == 'hyundai'
    hyundai_cars = list(filter(is_hyundai_car, cars))
    print(f"hyundai cars = {hyundai_cars}")

    # find the affordable cars (price <= 15)
    is_affordable = lambda car: car['price'] <= 15
    affordable_cars = list(filter(is_affordable, cars))
    print(f"affordable cars = {affordable_cars}")

function5()