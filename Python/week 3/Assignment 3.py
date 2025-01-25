oldList = [1, 4, 7, 4, 3, 5, 5]
newList = []

for i in oldList:
    if i not in newList:
        newList.append(i)

print(newList)


