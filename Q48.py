def read():
    file = open('output.txt','r')
    num = file.read()
    file.close() #it is a good practise to close a file.
    return num #it is important to return and not a print a variable which is inside the function.
contents = read()
print(contents)
