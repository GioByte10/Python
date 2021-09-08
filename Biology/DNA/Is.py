import os

to_print = ""
to_print += "foo" + "\n"
print(to_print)

user_input = input("Enter some text: ")
os.system("cls")

to_print += "You just entered " + user_input + "\n"
print(to_print)