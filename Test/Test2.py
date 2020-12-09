items = ["Earphones", "Charger", "Mouse", "Stylus"]
purposes = ["Listen to audio", "Give phone battery", "Maneuver computer", "Write on tablet"]

print("What do you want to do?")

task = input("add, remove, purpose, or sublist: ")

if task == "add":
    addElement1 = input("\nAdd element 1: ")
    addPurpose1 = input("Add purpose 1: ")
    addElement2 = input("\nAdd element 2: ")
    addPurpose2 = input("Add purpose 2: ")

    items.append(addElement1)
    items.append(addElement2)

    purposes.append(addPurpose1)
    purposes.append(addPurpose2)

    print(items)
    print(purposes)

elif task == "remove":
    removeElement1 = input("\nWhat element do you want to remove? ")
    removeElement2 = input("What other element do you want to remove? ")

    purposes.remove(purposes[items.index(removeElement1)])
    purposes.remove(purposes[items.index(removeElement2) - 1])

    items.remove(removeElement1)
    items.remove(removeElement2)

    print(items)
    print(purposes)

elif task == "purpose":
    purposeElement = input("What item's purpose do you need? ")
    print(purposes[items.index(purposeElement)])

elif task == "sublist":
    startingItem = input("What is the starting item? ")
    endingItem = input("What is the ending item? ")
    print(items[items.index(startingItem) : items.index(endingItem) + 1])
    print(purposes[items.index(startingItem) : items.index(endingItem) + 1])

else:
    print("Select only the options given.")