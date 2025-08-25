def math_operations(p1, p2):
    addition = p1 + p2
    subtraction = p1 - p2
    multiplication = p1 * p2
    division = p1 / p2

    # packing values in a tuple
    return addition, subtraction, multiplication, division

result = math_operations(20, 10)
print(f"result = {result}, type = {type(result)}")

# unpacking the values in variables
addition, subtraction, multiplication, division = result

print(f"addition = {addition}")
print(f"subtraction = {subtraction}")
print(f"multiplication = {multiplication}")
print(f"division = {division}")
