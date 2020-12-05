num = int(input("enter a number: "))
divisors = [1]
candidates = range(2, int(num/2))
for number in candidates:
    if num % number == 0:
        divisors.append(number)

# i = 1
# while i <= num/2:
#     if num % i == 0:
#         divisors.append(i)
#     i = i+1
divisors.append(num)
print(divisors)
