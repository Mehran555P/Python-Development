password = "python123"
m = 3
geuss = ""
    # ///////////////////////guess 1

guess = input("Please enter your guess : ")
print(type(guess))

if geuss == password:
    print("You win!!!")
else :
    m -= 1
    print("Try again")
    print(m , "chances")

    # ///////////////////////guess 2

guess = input("Please enter your guess : ")

if geuss == password:
    print("You win!!!")
else :
    m -= 1
    print("Try again")
    print(m , "chances")

    # ///////////////////////guess 3

guess = input("Please enter your guess : ")

if geuss == password:
    print("You win!!!")
else :
    m -= 1
    print("You lost!")
    print(m , "chances")

