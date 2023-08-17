n = input('Enter the string: ')
c = 0
v = 0

for i in range(0,len(n)):
    if(n[i] in ["a","e","i","o","u"]):
        v= v+1
    else:
        c = c+1
print("It has",(v),"vowels,")
print("It has",(c),"consonants.")



