n = int(input('Enter the decimal number: '))
binary = ""
while (n>0):
    r = n%2
    binary = binary + str(r)
    n= n//2
reversed_binary = binary[::-1]
print(reversed_binary)
