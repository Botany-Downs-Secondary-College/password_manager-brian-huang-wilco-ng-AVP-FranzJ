# password_manager.py
# make and show passwords
# Brian =^._.^=

passwords = []

class PasswordManager():
    def __init__(self):
        print("Hello and welcome to pwManage")
        self.run()
    

    def run(self):
        self.age_check()
        
        

        

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
        age = self.integer_check("How old are you?")
        if age < 13:
            print("You are not old enough to use this application.")
            self.cya_lol()
        elif age > 140:
            print("There is no way you are old enough to se this application.")
            self.cya_lol()

def main():
    PasswordManager()

if __name__ == '__main__':
    main()


    
