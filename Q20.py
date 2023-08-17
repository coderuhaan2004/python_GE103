n = int(input('Enter the number'))
t = int(input('Enter the curvature'))
for i in range(0,n+1):
    print((((n-i)*(n-i))+t*(n-i)-5)*" ","*")
for i in range(0,n+1):
    print(((i*i)+t*i-5)*" ","*")


