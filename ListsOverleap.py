list1 = [1, 3, 13, 2, 6, 57, 11, 3, 33, 455, 8]
list2 = [5, 2, 23, 9, 50, 12, 78, 11, 455, 3, 6]
overLeap = []
for element in list1:
    if element in list2:
        overLeap.append(element)

print(overLeap)
