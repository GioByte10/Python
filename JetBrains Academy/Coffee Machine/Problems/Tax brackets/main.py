income = int(input())
tax = 0

if income > 132406:
    tax = 28

elif income > 42707:
    tax = 25

elif income > 15527:
    tax = 15

else:
    tax = 0

taxed = round(income * tax / 100)

print(f"The tax for {income} is {tax}%. That is {taxed} dollars!")
