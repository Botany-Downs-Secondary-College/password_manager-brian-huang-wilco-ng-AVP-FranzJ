import os
MasterKeyList = ["1705"]
f = open("passwordslist.txt", "x")

# Login stage
def login():

    while True:
        try:
            choice = int(input("1)Login 2)Register 3)Quit --> "))
        except ValueError:
            print("Please choose a whole number either 1, 2 or 3")
            continue

        # login
        if choice == 1:
            MasterKey = input("Enter your master key to continue:")
            if MasterKey in MasterKeyList:
                print ("Success")
                main()
            else:
                print ("Incorrect")
            login()

        # Registration stage
        elif choice ==2:
            if choice ==2:
                age = float(input("Please enter your age: "))
                if age < 13:
                    print("no")
                    end
                elif age > 13:
                    print("Welcome please create your master key,")
                    print("this key will be required the next time you login")
                    print("take note of this key as you will be unable to recover it if lost.")
                    print("")
                    print("")
                MasterKey = input("Enter your master Key:")
                print("Your master key has been successfully created!")
                MasterKeyList.append(MasterKey)

        # Quit option
        elif choice ==3:
            print("Thank you for using SmartPass, bye now")
            os.remove("passwordslist.txt")
            exit()

        else:
            print("Invalid input, please try again")


def main():

        LoggedIn = True
        print("You are currently logged in to SmartPass")

        while LoggedIn:
            choice = int(input("1)Add password 2)View password 3)Logout: "))

            if choice == 1:
                back = "menu"
                print("type 'menu' to go back")
                f = open("passwordslist.txt", "a")
                newpassword = input("Type the password would you like to add? ")
                f.write(newpassword)
                if back == newpassword:
                    main()

            elif choice == 2:
                f = open("passwordslist.txt", "r")
                print(f.read())

            # Logout and quit program
            if choice == 3:
                LoggedIn = False
                print("Logging out of your session....")
                os.remove("passwordslist.txt")



print("Hello")
login()
