print("This program will try to crack your password using Brute Force")
username = input("Let's give it the username: ")
password = input("Enter the password to be cracked: ")


def login(username, guess):
    if guess == password:
        return guess
    else:
        return None

def bruteForce():
    guess = ""
    while login(username, guess) is not None:
        