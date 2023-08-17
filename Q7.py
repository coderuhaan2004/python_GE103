a = int(input('Enter the first number: '))
d = int(input('Enter the common difference: '))
b = int(input('Enter the last number: '))
r = int(((b-a)/d)+1)
for i in range(1,r+1):
	print(a+ (i-1)*d)




