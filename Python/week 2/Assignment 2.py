password = "python123"
m = 3

# ///////////////////////guess 1
guess = input("Please enter your guess : ")

if guess == password:
    print("You win!!!")
else:
    m -= 1
    print("Try again")
    print(m, "chances left")

    # ///////////////////////guess 2
    guess = input("Please enter your guess : ")

    if guess == password:
        print("You win!!!")
    else:
        m -= 1
        print("Try again")
        print(m, "chances left")

        # ///////////////////////guess 3
        guess = input("Please enter your guess : ")

        if guess == password:
            print("You win!!!")
        else:
            m -= 1
            print("You lost!")
            print(m, "chances left")