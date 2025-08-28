# file handling
# - writing and reading from file
# - to open a file call a function open()
# - open accepts two parameters
#   - 1st param: file name or path to open
#   - 2nd param: mode and file type
#     - mode: 
#       - read(r): 
#         - open file for reading
#         - if file does not exist, app will raise an exception FileNotFoundError
#       - write(w): 
#         - open file for writing
#         - if file does not exist, a new empty file will be created first
#         - if file contains data, it gets overwritten with new data
#       - append(a): 
#         - open file to append new data
#         - if file does not exist, a new empty file will be created first
#     - types:
#       - text(t): 
#         - file can opened or edited in any text editor
#         - default type of file considered
#         - file stores the data as characters
#       - binary(b):
#         - file contains the byte stream 
#         - such file can NOT be opened or edited in any text editor
# - returns file descriptor (reference)
# - every OS has a limit of number of files opened by a process
# - never perform any IO operation after the file gets closed
#   - else the application will raise an Exception: ValueError
# - when a process gets created, its gets 3 descriptors (integer value)
#   - stdin: standard input (keyboard)
#   - stdout: standard output (console)
#   - stderr: standard error (console)
# - read()
#   - used to read contents of a file
#   - by default, it reads the entire contents of a file
#   - not recommended if the file is huge
# - read(n)
#   - read first n bytes (characters)
#   - read internally maintains the current position
#   - if read(10) is called twice
#     - in the first attempt, first 10 bytes are read
#     - in the second attempt, next 10 bytes are read
# - seek(n)
#   - set the current position for reading the contents of the file
# - write()
#   - used to write the contents to file in both write and append mode
#   - writes the contents at the current position
#   - never adds a new line character (by default)
#     - to add a new line, write \n character explicitly
# - tell():
#   - used to get the current position


def function1():
    # open file for reading the contents
    # file = open("mydata.txt", "r")
    file = open("mydata.txt", "rt")
    
    # read the all contents of the file
    # contents = file.read()
    # print(f"contents = {contents}")

    # reading file chunk by chunk or byte by byte
    # reading first 10 bytes from file
    contents = file.read(10)
    print(f"contents = {contents}")
    print(f"current position is at: {file.tell()}")

    # set the current position
    file.seek(5)

    # start reading the file from 6th character
    contents = file.read(10)
    print(f"contents = {contents}")
    print(f"current position is at: {file.tell()}")

    # close the file
    file.close()

function1()

def function2():
    # open file for reading the contents
    file = open("mydata.txt", "rt")

    # read the data line by line
    contents = file.readline()
    print(f"contents = {contents}")

    # read the data line by line
    contents = file.readline()
    print(f"contents = {contents}")

    # read the data line by line
    contents = file.readline()
    print(f"contents = {contents}")

    # close the file
    file.close()

# function2()

def function3():
    # open the file for writing
    # file = open("mydata.txt", "w")
    file = open("mydata.txt", "wt")

    # write contents to the file
    file.write("line1 added by program2\n")
    file.write("line2 added by program2\n")
    file.write("line3 added by program2\n")
    file.write("line4 added by program2\n")

    # close the file
    file.close()

# function3()

def function4():
    # open the file for writing
    file = open("mydata.txt", "wt")

    # write contents to the file
    file.write("new contents written")
    
    # - with latest version of python, file contents get written on the disk
    #   even without closing the file
    # - with the older version, without closing file, the contents
    #   can NOT be persisted

# function4()

def function5():
    # open the file for appending new contents
    # file = open("mydata.txt", "w")
    file = open("mydata.txt", "at")

    # write contents to the file
    file.write("line1 added by program2\n")
    file.write("line2 added by program2\n")
    file.write("line3 added by program2\n")
    file.write("line4 added by program2\n")

    # close the file
    file.close()

# function5()

def function6():
    # open the file for writing
    # write the contents
    # when with block losses the control, file automatically gets closed
    with open("mydata.txt", "wt") as file:
        # write contents to the file
        file.write("line1 added by program2\n")
        file.write("line2 added by program2\n")
        file.write("line3 added by program2\n")
        file.write("line4 added by program2\n")

    with open("mydata.txt", "rt") as file:
        print(file.read())
    

# function6()

