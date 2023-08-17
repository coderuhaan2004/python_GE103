def fibo(n):
    farray = [1,2]
    for i in range(0,n-2):
        farray.append(farray[i]+farray[i+1])
    for i in farray:
        print(i)

a = int(input('Enter the last number: '))
fibo(a)

