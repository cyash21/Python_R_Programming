# dictionary
# - collection of key-value pairs
#   - where both key and value can be of any type
#   - but most often, key will be of type string
# - is a mutable collection
# - to read value using key
#   - use of []: when the key exists
#     - if the key does not exist, the app will raise an exception
#   - use of get(): when the key may not exist
#     - if they key does not exist, it returns None and wont raise any exception
# - duplicate keys are NOT allowed, duplicate values are allowed

def function1():
    # empty dictionary
    dictionary1 = {}
    print(f"dictionary1 = {dictionary1}, type = {type(dictionary1)}")

    # empty dictionary
    dictionary2 = dict({})
    print(f"dictionary2 = {dictionary2}, type = {type(dictionary2)}")

# function1()

def function2():
    # dictionary with key-value pairs
    person = {
        "name": "person1",
        "address": {
            "city": "pune",
            "state": "MH",
            "zipcode": 411041
        },
        "age": 30,
        "email": "person1@test.com",
        "hobbies": ["reading books", "trekking"],
        "salary": 15.60,
        "salary": 25.60,
        "salary": 45.60,
        "can_vote": True,
        "is_dead": True
    }

    print(person)
    print('-' * 80)

    print(f"key: {person.keys()}")
    print(f"values = {person.values()}")
    print("-" * 80)

    # read a value using key
    print(f"address = {person['address']}")
    print(f"name = {person['name']}, {person.get('name')}")
    print(f"city = {person['address']['city']}")
    print(f"city = {person.get('address').get('city')}")
    print(f"state = {person['address']['state']}")
    print(f"zipcode = {person['address']['zipcode']}")
    print(f"age = {person['age']}")
    print(f"email = {person['email']}")
    print(f"salary = {person['salary']}")

    # read value of a key which does not exist
    # this statement will raise an exception and will crash app
    # print(f"company name = {person['company']}")

    # read value of a key which does not exist
    print(f"company name = {person.get('company')}")
    print("-" * 80)
    
    # iterate over a dictionary to access all key-value pairs
    for key in person.keys():
        print(f"key = {key}, value = {person[key]}")
    print("-" * 80)
    
    # iterate over a dictionary to access all key-value pairs
    # for item in person.items():
        # print(f"item = {item}, type = {type(item)}")
        # print(f"key = {item[0]}, value = {item[1]}")

        # tuple unpacking
        # key, value = item
        # print(f"key = {key}, value = {value}")

    # for every item of type tuple, get the key and value unpacked
    for key, value in person.items():
        print(f"key = {key}, value = {value}")
    
# function2()

def function3():
    # start with empty dictionary
    person = {}
    print(f"person = {person}")

    # get input from user and build the dictionary
    name = input("enter your name: ")
    address = input("enter your address: ")
    age = int(input("enter your age: "))
    email = input("enter your email: ")

    # add the keys with their values
    # - if key does not exist, it will get added
    # - if key exists, it will get overwritten
    person['name'] = name
    person['address'] = address
    person['age'] = age
    person['email'] = email

    print(f"person: {person}")

    # this will NOT change the name value in dictionary
    name = "test"

    # this will change the name value in the dictionary
    person['name'] = "updated_name"
    print(f"after updating name: person: {person}")
    person['first_name'] = "new_name"
    print(f"after updating name: person: {person}")

    # delete a key
    del person['name']

# function3()

def function4():
    # list of dictionaries
    persons = [
        {"name": "person1", "age": 20, "email": "person1@test.com"},
        {"name": "person2", "age": 10, "email": "person2@test.com"},
        {"name": "person3", "age": 50, "email": "person3@test.com"},
        {"name": "person4", "age": 80, "email": "person4@test.com"},
        {"name": "person5", "age": 26, "email": "person5@test.com"}
    ]

    for person in persons:
        # print(f"person = {person}, type = {type(person)}")
        print(f"name = {person['name']}, age = {person['age']}, email = {person['email']}")

    print("-" * 80)

    for person in persons:
        for key, value in person.items():
            print(f"{key}: {value}")
        print('----')

# function4()


def function5():
    data = """NEW DELHI: The US on Tuesday issued a notice to India over the implementation of additional tariffs set to take effect from August 27.
    Issued by the department of homeland security, the notice said that the tariffs were imposed in response to "threats to the United States by the government of Russian Federation," with India being targeted for new duties as part of the policy.
    "The duties set out in the Annex to this document are effective with respect to products of India that are entered for consumption, or withdrawn from warehouse for consumption, on or after 12.01am eastern daylight time on August 27, 2025," the notice read.
    "To address that unusual and extraordinary threat to the national security and foreign policy of the United States, Executive Order 14066 prohibited, among other things, the importation into the United States of certain products of Russian Federation origin, including crude oil; petroleum; and petroleum fuels, oils, and products of their distillation," it added.
    The notice also listed a broad range of Indian products listed in the annex. It said that tariffs will apply to any goods that arrive for use or are taken out of warehouses after the deadline."""

    # count every word present in the news article
    # {"NEW": 1, "DELHI": 2 ....}

    # split the string into multiple words
    words = data.split(" ")
    # print(words)

    # create a dictionary to keep the word counts
    word_counts = {}
    for word in words:
        # check if the word is present in the dictionary
        if word in word_counts:
            # if it is present, increment the count
            word_counts[word] += 1
        else:
            # if it is not present, add the word with count = 1
            word_counts[word] = 1

    print(word_counts)

function5()