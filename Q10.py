n = int(input('Enter the number'))
is_prime = True
for i in range(2,):
    if(n%i==0):
        is_prime = False
if is_prime:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")

