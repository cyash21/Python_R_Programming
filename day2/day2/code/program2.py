# string variables
# - single and double quotes are used to declare single line string
# - triple double or triple single quotes are used to declare
#   a multi-line string

# data type = string
first_name = "steve"
print(f"first_name = {first_name}, type = {type(first_name)}")

# data type = string
last_name = 'jobs'
print(f"last_name = {last_name}, type = {type(last_name)}")

# data type = string
address = """house number 100,
sinhgad road,
pune 411041"""
print(f"address = {address}, type = {type(address)}")

# data type = string
address = '''house number 100,
sinhgad road,
pune 411041'''
print(f"address = {address}, type = {type(address)}")

# when a double quote is required in a string 
# which started with double quote
# use escape character to escape the inner double quotes
dialog = "Arnold once said, \"I will be back.\""
print(f"dialog = {dialog}")

# when a quote is required in a string 
# which started with double quote
# use single quotes
dialog = "Arnold once said, 'I will be back.'"
print(f"dialog = {dialog}")

dialog = 'Arnold once said, \'I will be back.\''
print(f"dialog = {dialog}")

dialog = 'Arnold once said, "I will be back."'
print(f"dialog = {dialog}")

dialog = """Arnold once said, 'I will be back.'"""
print(f"dialog = {dialog}")

dialog = '''Arnold once said, "I will be back."'''
print(f"dialog = {dialog}")
