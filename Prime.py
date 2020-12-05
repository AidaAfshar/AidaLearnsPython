def isPrime(num):
    numSQRT =int(pow(num,0.5))
    for i in range(2,numSQRT):
        if num%i==0:
            return False
    return True


num = int(input("enter a number: "))
if isPrime(num):
    print(str(num)+" is Prime")
else:
    print(str(num) + " is not Prime")