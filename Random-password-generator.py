import string
import random



characters = list(string.ascii_letters + string.digits + "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=<>?:|][?}{|")

def generate_password():
    
    password_length = int(input("How long do you want your password to be? : "))
    
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(characters)
    password = "".join(password)
    
    print(password)
    
    
    
    
option = input("Do you want to generate a password? (yes/no): ")

if option == "yes":
    generate_password()
elif option == "no":
    print()
    print("program ended")
    quit()
else:
    print("Invalid word, option is: yes/no")
    quit()

