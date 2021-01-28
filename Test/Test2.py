items = ["Mouse",              "Monopoly",    "Divine Comedy Book", "Shirt"]
purposes = ["For my computer", "Have fun",    "Learn new jokes",     "Wear"]

print("What do you want to do?")
option = input("add, remove, purpose, sublist: ")
print()

if option == "add":
    items.append(input("What is the first item? "))
    purposes.append(input("What is its purpose? "))

    items.append(input("What is the second item? "))
    purposes.append(input("What is its purpose? "))



elif option == "remove":
    toRemove1 = input("What element do you want to remove? ")
    toRemove2 = input("What other element do you want to remove? ")

    purposes.remove(purposes[items.index(toRemove1)])
    items.remove(toRemove1)

    purposes.remove(purposes[items.index(toRemove2)])
    items.remove(toRemove2)

    print()

elif option == "purpose":
    print(purposes[items.index(input("Which element's purpose do you need? "))])

elif option == "sublist":
    start = input("What is the first element? ")
    end = input("What is the las element? ")

    startIn = items.index(start)
    endIn = items.index(end)

    print(items[startIn:endIn + 1])
    print(purposes[startIn:endIn + 1])

    print()


print(items)
print(purposes)
