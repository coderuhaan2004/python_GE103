n = float(input('Enter the temperature: '))
print("Type 1 if you want to convert it to degree celsius")
print("Type 2 if you want to convert it to degree fahrenheit")
a = int(input())
b=0
if(a==1):
    b=((a-32)*5)/9
if(a==2):
    b=a*(9/5)+32
print(b)


