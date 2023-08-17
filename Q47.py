def numbers(n): #creates a function with some task.
    for i in range(1,n+1):
        yield i #generates n numbers inside the function.
a=int(input('Enter the number: '))#takes the input of number of numbers to be written.
file = open('output.txt','w') #opens the file from the directory.
for num in numbers(a): #Used for iterating through the numbers generated by the function.
    file.write(str(num)+ "\n") #writes the contents of the file
file.close() #closes the file

