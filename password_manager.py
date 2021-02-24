# password_manager.py
# make and show passwords
# Brian =^._.^=

passwords = []

def cya_lol()
    print("goodbye mens))")
    exit()

def integer_check(question):
    while True:
        try:
            num = int(input(question))
            if num <= 0:
                print("Please input a positive number.")
                continue
            return num
        except ValueError:
            print("Please input a valid number.")            
    

def age_check():
    age = integer_check("How old are you?")
    if age < 13:
        print("You are not old enough to use this application.")
        cya_lol()
    


