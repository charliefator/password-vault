# imports
import json

# functions

def add_login(new_username, new_password):
    tmp_add_login = {}
    tmp_add_login[new_username] = new_password
    
    with open(filename, "r") as file:
        data = json.load(file)
    data.append(tmp_add_login)
    with open(filename, "w") as file:
        json.dump(data, file)

def list_logins():
    with open(filename, "r") as file:
        data = json.load(file)
        return(print(data))

# main code

running = True
filename = "logins.json"

while running == True:
    print("Enter a command")
    selection = input("add login (a), list logins (l), or quit (q): ")

    if selection == "a":
        new_username = input("Enter the username or email: ")
        new_password = input("Enter the password: ")

        add_login(new_username, new_password)

    elif selection == "l":
        list_logins()

    elif selection == "q":
        running = False

    else:
        print("The command you entered does not exist, please try again.")
