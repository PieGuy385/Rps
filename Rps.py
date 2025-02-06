import random
Cont = True

print("Rock = 1")
print("Paper = 2")
print("Scissor = 3")

while Cont == True:
    Cpu_rng = random.randint(1, 3)

    print("")

    while True:
        Human = float(input("Pick 1, 2, or 3: "))
        if Human == 1:
            break
        elif Human == 2:
            break
        elif Human == 3:
            break
        else:
            print("Please enter \"1\", \"2\", or \"3\"")

    if Cpu_rng == 1:
        print("The computer chose rock")
        if Human == 1:
            print("You tied")
        elif Human == 2:
            print("You win")
        elif Human == 3:
            print("You lose")

    elif Cpu_rng == 2:
        print("The computer chose paper")
        if Human == 1:
            print("You lose")
        elif Human == 2:
            print("You tied")
        elif Human == 3:
            print("You win")

    elif Cpu_rng == 3:
        print("The computer chose scissor")
        if Human == 1:
            print("You win")
        elif Human == 2:
            print("You lose")
        elif Human == 3:
            print("You tied")

    while Cont == True:
        yn = input("Would you like to continue? (y/n): ")
        if yn.lower() == "y":
            Cont = True
            break
        elif yn.lower() == "n":
            Cont = False
            break
        else:
            print("Please enter \"y\" or \"n\"")

print("Thanks for playing! :)")