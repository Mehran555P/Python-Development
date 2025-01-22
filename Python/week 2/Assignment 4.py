score = input("Please enter score of student(Between 1 / 100 ) :")

score = int(score)

if score >= 0 and score <= 100 :
    if score >= 90 :
        print("Great!!!")
    elif score >= 70 and score < 90 :
        print("Good!")
    elif score >= 50 and score < 70 :
        print("you need more hardworking.")
    else :
        print("you failed!")
else :
    print("You entered a wrong value. Try again.")
