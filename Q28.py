def avg(a):
    sum = 0
    average = 0
    for i in a:
        sum = sum +i
    average = sum/len(a)
    return average
marks = []
for i in range(1,6):
    marks.append(float(input()))
n = avg(marks)
if n>=90:
    print("A")
elif n in range(80,91):
    print("B")
elif n in range(70,81):
    print("C")
elif n in range(60,71):
    print("D")
else:
    print("F")

