def gcd(a,b):
    if b==0:
        return a
    else: 
        return gcd(b,a%b)
#learning for recursion
p = int(input('Enter first number: '))
q = int(input('Enter second number: '))
print(gcd(p,q))

        

