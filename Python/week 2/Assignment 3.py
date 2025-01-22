clor = ""
color = input("Please enter color of trafic light(Green/Yellow/red) :")

if color.lower() == "green" :
    print("Go!")
elif color.lower() == "yellow" :
    print("Ready to go!")
elif color.lower() == "red" :
    print("Stop!!")
else :
    print("You entered wrong value.")