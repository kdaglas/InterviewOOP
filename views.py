from models import Users
from validate import validate_username, validate_password
import re


the_users = []
passwords = []
maxLengthList = 3


def add_new_user(username, password):
    
    new_user = Users(username, password)
    the_users.append(new_user)
    return True
    

def register():
    
    while True:
        username = input("Enter your username: ")
        if validate_username(username) == False:
            print("Please enter correct username...")
            continue
        else:
            break
    
    print("Enter atmost 7 passwords...")

    # password = input().split(",")
    # passwords.append(password)

    while len(passwords) < maxLengthList:
        password = input()
        passwords.append(password)
        
    print("-----------------------------")
    print("These are your passwords:")
    print (passwords)
    print("-----------------------------") 

    username = username
    password = password
    add_new_user(username, password)

    if len(the_users) > 0:
        print("")
        print("New user added:")
        print("-----------------------------")

        for user in the_users:
            
            valid_passwords = []

            print("")
            print( "Welcome "+ user.username )
            print("")
            print("Your prefered Passwords are:")
            for password in passwords:
                if validate_password(password) == True:
                    valid_passwords.append(password)

            valid_passwords = ', '.join(map(str, valid_passwords))
            print(valid_passwords)

            print("")
            print("-----------------------------")

        return True
    return False    

if __name__ == '__main__':
    register()    
         