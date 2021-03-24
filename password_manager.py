# password_manager.py
# make and show passwords
# Brian =^._.^=

import re

logins = {}

with open("logins.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        f_username = line[:line.index(";")]
        f_password = line[line.index(";") + 1:-1]
        
        logins[f_username] = f_password

print("Hello")
print("test")

class PasswordManager():
    def __init__(self):
        print("Hello and welcome to pwManage")
        self.run()

    def run(self):
        self.age_check()
        running = True
        while running:
            option = self.integer_check("What would you like to do? "
                                        "(Enter Number) \n"
                                        "    1. Add a new login \n"
                                        "    2. View Logins \n"
                                        "    3. Exit application \n")

            if option == 1:
                self.create_login()
            elif option == 2:
                self.check_logins()
            elif option == 3:
                self.cya_lol()
            else:
                print("Please enter a valid option")

    def cya_lol(self):
        print("goodbye mens))")
        exit()

    def integer_check(self, question):
        while True:
            try:
                num = int(input(question))
                if num <= 0:
                    print("Please input a positive number.")
                    continue
                return num
            except ValueError:
                print("Please input a valid number.")

    def age_check(self):
        age = self.integer_check("How old are you? ")
        if age < 13:
            print("You are not old enough to use this application.")
            self.cya_lol()
        elif age > 140:
            print("There is no way you are old enough to se this application.")
            self.cya_lol()

    def password_check(self, pw):
        password_regex = re.compile(r"""
                                    (?=.*[A-Z]) # must match atleast 1 Upper
                                    (?=.*[a-z]) # must match atleast 1 Lower
                                    (?=.*\d)    # must match atleast 1 Digit
                                    .{8,}       # must match 8 of the above
                                    """, re.VERBOSE)
        if password_regex.search(pw) is None:
            return False
        else:
            return True

    def create_login(self):
        create_name = True
        create_pass = True

        while create_name:
            username = input("What would you like your username to be? ")
            if username in logins:
                print("Username %s already exists." % (username))
                continue
            create_name = False

        while create_pass:
            password = input("Please input the password for the username "
                             "(Password must include at least 1 uppercase, "
                             "1 lowercase and 1 number): ")
            eligible = self.password_check(password)
            if not eligible:
                print("Your password does not meet the requirements. "
                      "Please try again: \n")
                continue
            create_pass = False

        logins[username] = password
        with open("logins.txt", "a") as f:
            f.write("%s;%s\n" % (username, password))

        print("Username and password added to logins. \n")

    def check_logins(self):
        if not logins:
            print("There are no logins.")
        else:
            print()
            for count, i in enumerate(logins):
                print("%s. Username: %s, Password: %s"
                      % (count + 1, i, logins[i]))
        print("")


def main():
    PasswordManager()


if __name__ == '__main__':
    main()
