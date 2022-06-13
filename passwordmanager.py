import os
from cryptography.fernet import Fernet


def action():
    try:
        with open("masterpassword.txt", "x") as masterpasswordfile:
            masterpasswordfile.write("")
    except FileExistsError:
        pass
    if(os.stat("masterpassword.txt").st_size == 0):
        setmasterpassword()
    else:
        askmasterpassword()
    while True:
        action = input("\nSelect \"Add\" to add a new password to the safe. \nSelect \"View\" if you want to view the stored passwords. \nSelect \"Delete\" if you want to delete all stored passwords. \nSelect \"Reset MP\" if you want to reset the master password. \nSelect \"Quit\" if you want to exit the program. \n > ").replace(" ", "").lower()
        if action == "add":
            add()
        elif action == "view":
            view()
        elif action == "delete":
            question = input("Are you sure you want to delete all of your stored passwords? (y/n) \n")
            if question == "y":
                deletepasswords()
            elif question == "n":
                pass
        elif action == "resetmp":
            resetmasterpassword()
        elif action == "quit":
            break
        else:
            print("Error occured during action selection. Please enter a valid action")

def add():
    key = load_key() + getmasterpassword().encode()
    fer = Fernet(key)
    with open("testpasswords.txt", "a+") as testpasswords:
        site = input("Please enter the site the password is for: ").title()
        psw = input("Please select a password for this site: ")
        testpasswords.write(site + "|" + fer.encrypt(psw.encode()).decode() + "\n")

def view():
    key = load_key() + getmasterpassword().encode()
    fer = Fernet(key)
    try:
        with open("testpasswords.txt", "x") as testpasswordsfile:
            testpasswordsfile.write("")
    except FileExistsError:
        pass
    with open("testpasswords.txt", "r") as testpasswords:
        if(os.stat("testpasswords.txt").st_size == 0):
            print("\nYou haven't saved any passwords yet.")
        else:
            for line in testpasswords.readlines():
                content = line.rstrip()
                site, passw = content.split("|")
                print("Site: " + site + " | Password: " + fer.decrypt(passw.encode()).decode())

def setmasterpassword():
    with open("masterpassword.txt", "a+") as masterpasswordfile:
        masterpassword = input("Please enter the master password that will be used to access stored contect in the future: ")
        print("\nNew master password has been set.")
        masterpasswordfile.write(f"{masterpassword}")

def askmasterpassword():
    with open("masterpassword.txt", "r") as masterpasswordfilecontent:
        masterpsw = masterpasswordfilecontent.read()
    tries = 3
    while(tries != 0):
        try:
            masterpasswordinput = input("Please enter the master password to access the stored content: ")
            if(masterpasswordinput == masterpsw):
                print("\nPassword correct!")
                break
            elif(masterpasswordinput != masterpsw):
                tries = tries - 1
                print("Wrong password!")
        except KeyboardInterrupt:
            quit()
    if tries == 0:
        print("You entered a wrong password too many times. The program will now close.")
        quit()

def getmasterpassword():
    with open("masterpassword.txt", "r") as masterkey:
        masterpassword = masterkey.read()
    return masterpassword

def resetmasterpassword():
    with open("masterpassword.txt", "r+") as mp:
        mp.truncate(0)
        mp.close()
        print("\nThe master passwords has been reset. The program will now close. Please open the program again to set up a new master password.")
        quit()

def deletepasswords():
    with open("testpasswords.txt", "r+") as tp:
        tp.truncate(0)
        tp.close()
        print("\nPasswords deleted.")

''' 
def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

if __name__ == "__main__":
    action()
