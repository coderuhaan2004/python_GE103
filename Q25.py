n = int(input('Enter the year: '))
if ((n%400==0) or
    (n%100!=0) and
    (n%4==0)):
    is_leap = True
else:
    is_leap = False
if is_leap:
    print("It is leap year.")
else:
    print("It is not leap year.")

