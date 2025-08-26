# when map and filter are used together
# - always implement the filter first and then the map

def function1():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # find the square of even numbers

    # find the even numbers
    is_even = lambda n: n % 2 == 0
    even_numbers = list(filter(is_even, numbers))

    # get the square of even numbers
    square = lambda n: n ** 2
    square_of_even_numbers = list(map(square, even_numbers))

    print(f"even numbers = {even_numbers}")
    print(f"square of even numbers = {square_of_even_numbers}")

# function1()

def function2():
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

    # find the prices of renault cars

    # find the renault cars
    is_renault = lambda car: car['company'] == 'renault'
    renault_cars = list(filter(is_renault, cars))

    # extract the price info
    extract_price = lambda car: car['price']
    renault_car_prices = list(map(extract_price, renault_cars))

    print(f"renault car prices: {renault_car_prices}")

function2()