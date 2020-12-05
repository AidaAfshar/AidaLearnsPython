n = int(input("enter a number: "))
f1 = 0
f2 = 1
print(f1)
print(f2)

for i in range(2, n):
    print(f1+f2)
    f3 = f1+f2
    f1 = f2
    f2=f3