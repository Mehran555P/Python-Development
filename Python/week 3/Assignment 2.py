numList = [1, 2, 3, 4, 5]

userNum = int(input("Please enter a number :"))

while (userNum != 0):
    picker = numList[-1]
    numList.pop(-1)
    numList.insert(0 , picker)
    userNum -= 1
print(numList)
