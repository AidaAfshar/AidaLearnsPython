num1 = int(input("Please enter first number: "))
num2 = int(input("please enter second number: "))
remainder = num1 % num2
if remainder == 0:
    print(str(num1) + " is dividable by " + str(num2))
else:
    print(str(num1) + " is not dividable by " + str(num2))
    print("the remainder is " + str(remainder))
