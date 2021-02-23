
MasterKeyList = []
PasswordList = []

# Login stage
def login():

    choosing = True
    while choosing:
        choice = int(input("1)Login 2)Register 3)Quit --> "))

        # login
        if choice ==1:
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
                print ("Welcome please create your master key,")
                print ("this key will be required the next time you login")
                print ("take note of this key as you will be unable to recover it if lost.")
                print ("")
                print ("")
            MasterKey = input("Enter your master Key:")
            print("Your master key has been successfully created!")
            MasterKeyList.append(MasterKey)

        # Quit option
        elif choice ==3:
            print("Thank you for using SmartPass, bye now")
            end

        else:
            print("Invalid input, please try again")

def main():

        LoggedIn = True
        print("You are currently logged in to SmartPass")

        while LoggedIn:
            choice = int(input("1)Add password 2)Edit password 3)Delete password 4)Logout> "))

            if choice == 1:
                back = "menu"
                print("type 'menu' to go back")
                add = input("Type the password would you like to add? ")
                PasswordList.append(add)
                if back in PasswordList:
                    PasswordList.remove("menu")
                    main()

            elif choice == 2:
                i = 0
                while i < len(PasswordList):
                    print("{}. {}".format(i + 1, PasswordList[i]))
                    i += 1

            elif choice == 3:
                i = 0
                while i < len(PasswordList):
                    print("{}. {}".format(i + 1, PasswordList[i]))
                    i += 1
                kachow = input("Please enter the password that you want to remove: ")
                PasswordList.remove("kachow")

            # Logout and quit program
            if choice ==4:
                LoggedIn = False
                print("Logging out of your session....")

            else:
                print("You are now logged out, bye!")


print("Hello")
login()
