def calculate_average(n):
    total = 0
    
    for i in range(n):
        grade = float(input(f"Enter grade {i+1}: "))
        total += grade
    
    average = total / n
    return average

n = int(input("Enter the number of grades: "))
average = calculate_average(n)
print(f"The average grade is: {average}")