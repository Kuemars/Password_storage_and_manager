passwords = []

while True:
    choice_1 = str(input("Do you want to store a password? Type yes or no: "))

    if choice_1.upper() == "yes".upper():
        passwordin = str(input("Enter your password: "))
        passwords.append(passwordin)
        print("Password stored")

        file = open("passwords.txt", 'a')
        for x in passwords:
            file.write(f"{x} \n")

        continue

    elif choice_1.upper() == "no".upper():

        while True:
            choice_2 = str(input("Do you want to see your passwords? Type yes or no: "))

            if choice_2.upper() == "yes".upper():
                print(passwords)

            elif choice_2.upper() == "no".upper():
                print("The program has now closed. You can find your passwords in the passwords.txt file")
                break

            else:
                print("invalid answer")
                continue
        break
    else:
        print("Invalid input, type yes or no.")