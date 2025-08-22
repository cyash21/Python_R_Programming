# default value or optional arguments
# - setting default value to the argument
# - when a default value is set to an argument, 
#   it becomes optional
# - if optional parameter is not passed, 
#   the default value will be taken
# - if the optional parameter is passed,
#   the value passed by caller will be used instead of default value

def function1(p=10000, n=2, r=8.5):
    print(f"rate of interest = {r}")
    interest = (p * n * r) / 100
    print(f"interest = {interest}")

function1(p=10000, n=2)
function1(p=50000, n=5)
function1(p=100000, n=1)
function1(p=177000, n=7)
function1(p=177000, n=7, r=7.5)
function1(n=6)
function1(r=7.5)