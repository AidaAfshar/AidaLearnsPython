list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
subList = []
for element in list:
    if element%2 != 0:
        subList.append(element)

print(subList)
