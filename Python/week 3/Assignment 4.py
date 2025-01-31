while True :
    
    c = int(input("Please enter count of marks :"))
    marks = []

    for i in range(c) :
        mark = int(input("Please enter marks :"))
        marks.append(mark)

    sum1 = sum(marks)
    avg = sum1/c 

    print(avg)

    close = input("Enter 'c' for exit :")
    if close == 'c' :
        break

    
    
