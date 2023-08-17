def fibo(n):
    farray = [1,2]
    for i in range(0,n-2):
        farray.append(farray[i]+farray[i+1])
    print(farray[n-2])
a = int(input('Enter the nth term: '))
fibo(a)

