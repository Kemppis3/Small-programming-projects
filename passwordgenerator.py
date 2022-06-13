import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@£$€%&?"


def ask_user():
    while True:
        count = int(input("How many passwords do you want to create? \n"))
        if count > 0:
            break
        else:
            print("Please enter a valid amount of passwords to create.")
    while True:
        passw_lengths = int(input("How long password do you want? \n"))
        if passw_lengths < 10:
            print("That short password is not very safe!")
        else:
            break
    return count, passw_lengths


def generate_passwords():
    count, passw_lengths = ask_user()
    passwordlist = []
    password = ""
    for amount in range(count):
        for chars in range(0,passw_lengths):
            passw_char = random.choice(characters)
            password = password + passw_char
        passwordlist.append(password)
        password = ""
    print("Here are your passwords: ")
    for passw in passwordlist:
        print(passw)


def main():
    while True:
        question = input("Select \"G\" if you want to generate passwords \nSelect \"Q\" to exit the program \n > ").lower()
        if question == "g":
            generate_passwords()
        elif question == "q":
            break
        else:
            print("Wrong choice")
        

if __name__ == "__main__":
    main()



