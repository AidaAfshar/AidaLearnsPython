string = input("please enter a string: ")
inverse = string[::-1]
# inverse = ""
# for i in range(1, len(string)+1):
#     inverse += string[len(string)-i]

print(inverse)
if string == inverse:
    print("palindrome ")
else:
    print("not palindrome ")