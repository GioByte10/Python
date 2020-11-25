grade1 = int(input("what is your percentage for english? "))
if grade1 <= 100 and grade1>=0 :
    print("percentage taken")
else:
    print("try again")
    print("reenter percentages")
    grade1 = int(input("what is your percentage for english? "))
grade2 = int(input("what is your percentage for math? "))
if grade2 <= 100 and grade2>=0 :
    print("percentage taken")
else:
    print("try again")
    print("reenter percentages")
    grade2 = int(input("what is your percentage for english? "))
grade3 = int(input("what is your percentage for science? "))
if grade3 <= 100 and grade3>=0 :
    print("percentage taken")
else:
    print("try again")
    print("reenter percentages")
    grade3 = int(input("what is your percentage for english? "))
grade4 = int(input("what is your percentage for history? "))
if grade4 <= 100 and grade4>=0 :
    print("percentage taken")
else:
    print("try again")
    print("reenter percentages")
    grade4 = int(input("what is your percentage for english? "))
grade5 = int(input("what is your percentage for engr? "))
if grade5 <= 100 and grade5>=0 :
    print("percentage taken")
else:
    print("try again")
    print("reenter percentages")
    grade5 = int(input("what is your percentage for english? "))

if grade1 >= 90:
    g1 = 4
elif grade1 >=80 :
    g1 = 3
elif grade1 >=70 :
    g1 = 2
elif grade1 >=60 :
    g1 = 1
else:
    g1= 0

if grade2 >= 90:
    g2 = 4
elif grade2 >=80 :
    g2 = 3
elif grade2 >=70 :
    g2 = 2
elif grade2 >=60 :
    g2 = 1
else:
    g2= 0

if grade3 >= 90:
    g3 = 4
elif grade3 >=80 :
    g3 = 3
elif grade3 >=70 :
    g3 = 2
elif grade3 >=60 :
    g3 = 1
else:
    g3= 0

if grade4 >= 90:
    g4 = 4
elif grade4 >=80 :
    g4 = 3
elif grade4 >=70 :
    g4 = 2
elif grade4 >=60 :
    g4 = 1
else:
    g4= 0

if grade5 >= 90:
    g5 = 4
elif grade5 >=80 :
    g5 = 3
elif grade5 >=70 :
    g5 = 2
elif grade5 >=60 :
    g5 = 1
else:
    g5= 0

gradetotal = (g1+g2+g3+g4+g5)/5

print(gradetotal)