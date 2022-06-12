import random
import time
import os

def action():
    if(os.stat("masterpassword.txt").st_size == 0):
        setmasterpassword()
    else:
        askmasterpassword()
    while True:
        action = input("\nAre you going to add a new password to the safe or are just viewing stored ones? \nSelect \"Add\" to add a new password to the safe. \nSelect \"View\" if you want to view the existing passwords. \nSelect \"Delete\" if you want to delete all stored passwords. \nSelect \"ResetMP\" if you want to reset the master password. \nSelect \"Quit\" if you want to quit the program. \n > ").lower()
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
    with open("testpasswords.txt", "a+") as testpasswords:
        site = input("Please enter the site the password is for: ").capitalize()
        psw = input("Please select a password for this site: ")
        testpasswords.write(f"\n{site}: {psw}")

def view():
    with open("testpasswords.txt", "r") as testpasswords:
        if(os.stat("testpasswords.txt").st_size == 0):
            print("\nYou haven't saved any passwords yet.")
        else:
            print(testpasswords.read())

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
        


if __name__ == "__main__":
    action()

