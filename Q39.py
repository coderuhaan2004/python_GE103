def find_max(a):
    max =-1
    for i in range(0,len(a)+1):
        if(a[i]>max):
            a[i] == max
    return max
n = []
while(len(n)>=0):
    n.append(int(input()))
find_max(n)
