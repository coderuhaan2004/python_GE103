n = int(input('Enter the factorial'))
def fac(a):
    p = 1
    for i in range(2,a+1):
        p = p*i
    print(p)
fac(n)
