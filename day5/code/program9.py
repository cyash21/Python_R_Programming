# comprehension
# - list comprehension
# - tuple comprehension
# - syntax
#   [<return value> <iteration logic> <filter logic>]

def function1():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # square of each number
    squares = [n ** 2 for n in numbers]
    print(f"squares = {squares}")

    # cube of each number
    cubes = [n ** 3 for n in numbers]
    print(f"cubes = {cubes}")

    # square of each number along with the original number
    squares = [(n, n ** 2) for n in numbers]
    print(f"squares = {squares}")


# function1()


def function2():
    # temperatures in celsius
    temperatures_celsius = [20, 29, 27, 27, 30, 31, 33]

    # convert the temperature to fahrenheit
    temperatures_fahrenheit = [(32 + (t * (9/5))) for t in temperatures_celsius]
    print(f"temperatures_fahrenheit = {temperatures_fahrenheit}")

# function2()

def function3():
    # list of dictionaries
    cars = [
        {"model": "triber", "company": "renault", "price": 10.0},
        {"model": "i20", "company": "hyundai", "price": 14.0},
        {"model": "nano", "company": "tata", "price": 3.0},
        {"model": "meridian", "company": "jeep", "price": 43.0},
        {"model": "defender", "company": "land rover", "price": 100.0}
    ]
    
    # get all the models
    models = [car['model'] for car in cars]
    print(f'models = {models}')

# function3()

def function4():
    # list of numbers
    numbers = [2, 5, 7, 9, 11, 23, 8, 10, 40]

    # find even numbers
    even_numbers = [n for n in numbers if n % 2 == 0]
    print(f"even numbers = {even_numbers}")

    # find odd numbers
    odd_numbers = [n for n in numbers if n % 2 != 0]
    print(f"odd numbers = {odd_numbers}")

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
    hyundai_cars = [car for car in cars if car['company'] == 'hyundai']
    print(f"hyundai cars = {hyundai_cars}")

    # find the affordable cars (price <= 15)
    affordable_cars = [car for car in cars if car['price'] <= 15]
    print(f"affordable cars = {affordable_cars}")

# function5()

def function6():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # find square of even number
    even_squares = [n ** 2 for n in numbers if n % 2 == 0]
    print(f"squares of even numbers = {even_squares}")


# function6()

def function7():
    # list of numbers
    numbers = [2, 5, 7, 9, 11, 23, 8, 10, 40]

    def is_prime(number):
        if number == 2:
            return True
        
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    
    prime_numbers = tuple([n for n in numbers if is_prime(n)])
    print(f"prime numbers = {prime_numbers}")

# function7()