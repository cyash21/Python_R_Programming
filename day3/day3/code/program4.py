# named function
def square(number):
    return number ** 2

# square_of_5 = square(5)
# print(f"square of 5 = {square_of_5}")

# lambda definition
square_lambda = lambda number: number ** 2

# square_of_6 = 6 ** 2
# square_of_6 = square_lambda(6)
# print(f"square of 6 = {square_of_6}")

# square_of_7 = 7 ** 2
# square_of_7 = square_lambda(7)

add = lambda n1, n2: n1 + n2
# print(f"10 + 20 = {10 + 20}")
print(f"10 + 20 = {add(10, 20)}")