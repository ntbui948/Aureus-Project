from passlib.hash import pbkdf2_sha256

import sys
# establishes array and number of pairs desired
username = []

password = []

class UserPass:

    def __init__(self, us, pa):
        self.USER = us
        self.PASS = pa

# allows you to store passwords in the array(hashed)
entering = "yes"

x = 1

while entering == "yes":
    
    entering = input("would you like to input username and password, yes/no?: ")
    
    if entering == "yes":
        
        USERPASS = UserPass(input(f"enter username # {x}: "), input(f"enter password # {x}: "))
        
        user_name = pbkdf2_sha256.hash(USERPASS.USER)
        # showing the hash for the username to make sure it works
        print(user_name)
         
        pass_word = pbkdf2_sha256.hash(USERPASS.PASS)
        # showing the hash for the password to make sure it works
        print(pass_word)

        num = user_name
        
        username.append(num)
        
        num2 = pass_word
        
        password.append(num2)
        
        num3 = x - 1

        x += 1
    
    elif entering == "no":         
        
        end = input("Would you like to end program(y) or continue to the login?(n): ")
            
        if end == 'n':
                
            break
            
        elif end == 'y':
            
            print("Goodbye")    
            
            exit()    
    
    else:
        
        print("please answer yes or no")
        
        entering = "yes"
   
# asks for you to enter username and password
verifyuser = str(input("enter username: "))

verifypass = str(input("enter password: "))
# check if entered password matches hashed password from array

for y in range (0, num3 + 1):   
    
    if pbkdf2_sha256.verify(verifyuser, username[y]):
        
        verified = 1
        
        break
    
    else:
        
        print("username is incorrect")
        
        verified = 0

for k in range (0, num3 + 1):

    if pbkdf2_sha256.verify(verifypass, password[k]):

        verified2 = 1

        break
    
    else:

        print("Password is incorrect")
        
        verified2 = 0

if verified == 1 & verified2 == 1:
    
    print("welcome")
    exit()

else:
    
    exit()


    