# map
# - used to perform transformation of a collection
# - is higher order function
# - accepts
#   - param1: transformation function/lambda
#   - param2: collection
# - returns a map object which can be converted to a list of tuple
# - it is mandatory for map function that it will return a collection of 
#   same size of the original collection

# requirement: transform/convert every value to its square

def function1():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # iterate over the list
    for number in numbers:
        print(f"number = {number}, square = {number ** 2}")

# function1()

def function2():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # collect all the squares 
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    
    print(f"numbers = {numbers}")
    print(f"squares = {squares}")

# function2()

def function3():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # transform a value to its square
    square = lambda n: n ** 2

    # collect all the squares 
    squares = []
    for number in numbers:
        squares.append(square(number))
    
    print(f"numbers = {numbers}")
    print(f"squares = {squares}")

# function3()

def function4():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # transform a value to its cube
    cube = lambda n: n ** 3

    # iteration logic
    cubes = []
    for number in numbers:
        cubes.append(cube(number))

    print(f"numbers = {numbers}")
    print(f"cubes = {cubes}")

# function4()

def function5():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # transformation logic
    square = lambda n: n ** 2

    # iteration logic will be provided by python
    squares = list(map(square, numbers))
    
    print(f"numbers = {numbers}")
    print(f"squares = {squares}")

# function5()

def function6():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # transformation logic
    cube = lambda n: n ** 3

    # iteration logic using map
    cubes = list(map(cube, numbers))

    print(f"numbers = {numbers}")
    print(f"cubes = {cubes}")
    
# function6()

def function7():
    # temperatures in celsius
    temperatures_celsius = [20, 29, 27, 27, 30, 31, 33]

    # transformation logic to convert celsius to fahrenheit
    to_fahrenheit = lambda t: 32 + (t * (9/5))

    # iteration logic
    temperatures_fahrenheit = list(map(to_fahrenheit, temperatures_celsius))

    print(f"temperatures_celsius = {temperatures_celsius}")
    print(f"temperatures_fahrenheit = {temperatures_fahrenheit}")

# function7()


def function8():
    # list of dictionaries
    cars = [
        {"model": "triber", "company": "renault", "price": 10.0},
        {"model": "i20", "company": "hyundai", "price": 14.0},
        {"model": "nano", "company": "tata", "price": 3.0},
        {"model": "meridian", "company": "jeep", "price": 43.0},
        {"model": "defender", "company": "land rover", "price": 100.0}
    ]

    # get the model name of every car
    # models = []
    # for car in cars:
    #     models.append(car['model'])

    # get the model name of every car using map
    # extract_model = lambda car: car['model']
    # models = list(map(extract_model, cars))

    # get the model name of every car using map
    models = list(map(lambda car: car['model'], cars))
    print(f"models = {models}")

    # get model and company of every car
    # extract_model_company = lambda car: {"model": car['model'], "company": car['company']}
    extract_model_company = lambda car: (car['model'], car['company'])
    model_and_company_info = list(map(extract_model_company, cars))
    print(f"models and company = {model_and_company_info}")

# function8()

