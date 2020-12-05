def reverse(string):
    stringList = string.split(" ")
    inverseStringList = stringList[::-1]
    inverseString = " ".join(inverseStringList)
    return inverseString

string = input("enter a string: ")
print(reverse(string))