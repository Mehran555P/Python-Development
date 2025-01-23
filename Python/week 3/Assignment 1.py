numbers = [1, 15, 25, 2, 8, 17, 6]

i = 0
while i < 7 :
    if numbers[i] % 2 == 0 :
        print(numbers[i])
        i += 1
    else :
        i += 1
        continue
