# string
# - collection/sequence of character
# - is immutable
# - it gets loaded in special area of PVM called string pool
# - if string pool area already has loaded a string value, 
#   it will never load the same string again
# - this principle is used to save the memory 
# - is case sensitive
# - string gets a contiguous memory (all the characters in a string
#   will get allocated contiguously)
# - string in python supports unicode (universal code)
#   - there are two types in unicode (utf => unicode transformation format)
#     - utf-8: 8 bit character (single byte character) => 1byte
#     - utf-16: 16 bit character (multi bytes characters) => 2 bytes
# - every character requires 2bytes in memory
# - python does NOT have any data type for a single character
#   - even if a variable contains a single character, 
#     it will get a data type of string (NOT A CHARACTER)
# string operations
# - finding length of a string
# - lower()
# - upper()
# - split()
# - join()
# - replace()
# - indexing and slicing
# - convert a string to list of characters

def function1():
    str1 = "test1"
    str2 = "test2"

    # in this case, since the value "test1" is same for both
    # str3 and str1, no new memory allocation happens
    str3 = str1

    # str3 will get a new memory from string pool
    str3 = "test3"

    # there will be no new memory for test1 allocated
    # since "test1" is already present in string pool
    str4 = "test1"

    # this time, a new memory is allocated for "test4"
    # and str4 will start referencing that memory
    str4 = "test4"
    str5 = "test4"

    # since string is case sensitive, a new memory gets allocated
    # in string pool area
    str6 = "Test1"

    num1 = 100
    num2 = 200

    # in this case, a new memory will be allocated for num3
    # and both num1 and num3 will have their separate memories
    num3 = num1

    # in this case, a new memory is allocated for num4
    num4 = 100


def function2():
    # string 
    name = "SunBeam"
    print(f"name = {name}")

    # size of string
    print(f"length of string = {len(name)}")

    # convert the case
    print(f"all in lowercase = {name.lower()}")
    print(f"all in uppercase = {name.upper()}")

    name = "sunbeam"
    print(f"name = {name.capitalize()}")

# function2()

def function3():
    # string
    data = "hello world"

    # split the string based on ' '
    # returns a list of strings splitted based on delimiter character
    words = data.split(' ')
    print(f"words = {words}")

    # extract protocol (https), domain name, file and query string
    url = "https://google.com/search?q=sunbeam&sca_esv=79222c262c147aa4"
    
    # split the url using :
    parts = url.split("://")
    # 0: https
    # 1: google.com/search?q=sunbeam&sca_esv=79222c262c147aa4
    print(f"parts = {parts}")
    print(f"protocol = {parts[0]}")
    print("-" * 80)

    # split the remaining string using /
    parts = parts[1].split("/")
    print(f"parts = {parts}")
    print(f"domain name = {parts[0]}")
    print("-" * 80)

    # split the remaining string using ?
    parts = parts[1].split("?")
    print(f"parts = {parts}")
    print(f"path = {parts[0]}")
    print("-" * 80)

    # split the remaining string using &
    # parts = ['q=sunbeam', 'sca_esv=79222c262c147aa4']
    parts = parts[1].split("&")
    print(f"query parameters = {parts}")

    # get all the query key and values
    for parameter in parts:
        # split the parameter using =
        parts = parameter.split("=")
        print(f"key = {parts[0]}, value = {parts[1]}")

# function3()

def function4():
    # string
    data = "hello world"

    # get a character from a string using +ve indexing
    print(f"data[0] = {data[0]}")
    print(f"data[1] = {data[1]}")
    print(f"data[2] = {data[2]}")
    print(f"data[3] = {data[3]}")
    print(f"data[4] = {data[4]}")
    print(f"-" * 80)

    # get a character from a string using -ve indexing
    print(f"data[-1] = {data[-1]}")
    print(f"data[-2] = {data[-2]}")
    print(f"data[-3] = {data[-3]}")
    print(f"data[-4] = {data[-4]}")
    print(f"data[-5] = {data[-5]}")
    print(f"-" * 80)

    # get a sub string from a string using slicing

    # extract the word hello
    print(f"data[0:5] = {data[0:5]}")
    print(f"data[:5] = {data[:5]}")
    print(f"data[6:11] = {data[6:11]}")
    print(f"data[6:] = {data[6:]}")

    # reverse a string
    print(f"data[::-1] = {data[::-1]}")
    
# function4()

def function5():
    # string formatting
    name = "sunbeam"
    print(f"name = {name}")

    # left aligned string
    print(f"name (left)   = {name:<15}, size = {len(name)}")

    # right aligned string
    print(f"name (right)  = {name:>15}, size = {len(name)}")

    # center aligned string
    print(f"name (center) = {name:^15}, size = {len(name)}")

# function5()

def function6():
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

    print('-' * 43)
    print(f"| {'Model':^13} | {'Company':^13} | {'Price':^7} |")
    print('-' * 43)
    for car in cars:
        print(f"| {car['model']:<13} | {car['company']:<13} | {car['price']:>7} |")
    print('-' * 43)
    
# function6()

def function7():
    num = 1456977

    # print the value in integer format
    print(f"num (integer) = {num:d}")

    # print the value in binary format
    print(f"num (binary)  = {num:b}")

    # print the value in octal format
    print(f"num (octal)   = {num:o}")

    # print the value in hexa-decimal format
    print(f"num (hex)     = {num:x}")
    print(f"num (hex)     = {num:X}")

    print("-" * 80)

    salary = 16.563453436
    print(f"salary        = {salary}")

    # display the float to scientific format
    print(f"salary (e)    = {salary:e}")
    print(f"salary (E)    = {salary:E}")

    # print only 2 digits after decimal
    print(f"salary        = {salary:.2f}")

    # create a new string with salary in 3 digits decimal precision
    # salary_str = str(salary)
    salary_str = f"{salary:.3f}"
    print(f"salary_str    = {salary_str}")

    num_str = f"{num:.3f}"
    print(f"num_str       = {num_str}")

    print("-" * 80)

    num2 = 100
    num3 = -100
    
    print(f"num2(+)       = {num2:+}")
    print(f"num3(-)       = {num3:-}")

    # this will NOT make num2 negative
    print(f"num2(-)       = {num2:-}")

    # this will NOT make num3 as positive
    print(f"num3(+)       = {num3:+}")

    print("-" * 80)

    num4 = 10000000
    print(f"num4           = {num4}")
    print(f"num4           = {num4:,}")
    print(f"num4           = {num4:_}")

function7()

def function8():
    # convert first 20 numbers in different number systems
    print(f"| integer | binary | octal | hex |")
    for number in range(21):
        print(f"| {number:d} | {number:b} | {number:o} | {number:X} |")

# function8() 


def function9():
    # string
    data = "hello world"
    print(f"data = {data}")

    # replace the word 'world' with 'hell'
    print(f"data = {data.replace('world', 'hell')}")
    print(f"data = {data}")

# function9()

def function10():
    # string
    data = "hello world"
    print(f"data = {data}")

    # convert the string to list of characters
    data_list = list(data)
    print(f"data_list = {data_list}")

    # convert the string to tuple of characters
    data_tuple = tuple(data)
    print(f"data_tuple = {data_tuple}")
    
# function10()


def function11():
    # string
    data = "India is my country. I love India. All indians are my brothers and sisters. "
    print(f"data = {data}")

    # split the string into collection of words
    words = data.split(' ')
    print(f"words = {words}")

    # join all the words in a new string
    print(f"new string = {''.join(words)}")
    print(f"new string = {' '.join(words)}")
    print(f"new string = {'-'.join(words)}")
    print(f"new string = {'-*-'.join(words)}")

# function11()

def function12():
    part1 = "hello"
    part2 = "world"

    data = part1 + part2
    print(f"data = {data}")

    print(f"joined string = {''.join([part1, part2])}")

# function12()


def function13():
    # string comparison is case sensitive
    print(f"'test1' == 'test2' = {'test1' == 'test2'}")

    # since case matches, the result is True
    print(f"'test1' == 'test1' = {'test1' == 'test1'}")

    # since case does not match, the result is False
    print(f"'test1' == 'Test1' = {'test1' == 'Test1'}")

    # case insensitive string comparison 
    # convert both the operands to same case (lower or upper)
    print(f"'test1' == 'Test1' = {'test1'.lower() == 'Test1'.lower()}")
    print(f"'test1' == 'Test1' = {'test1'.upper() == 'Test1'.upper()}")

# function13()

def function14():
    num1 = 10
    num2 = 20
    print(f"num1 = {num1}, num2 = {num2}")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"-" * 80)

    # first {} will be replaced by num1
    # second {} will be replaced by num2
    print("num1 = {}, num2 = {}".format(num1, num2))
    print("{} + {} = {}".format(num1, num2, num1 + num2))

# function14()