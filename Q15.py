n = input('Enter the string')
for i in range(0,len(n)):
    if(n[i]==n[len(n)-1-i]):
        print("It's a palindrome")
    else:
        print("not a palindrome")


