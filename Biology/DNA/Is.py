st1 = input("Son ")
st2 = input("mas que ")

sYear1 = ""
sYear2 = ""

for c in st1:
    if c.isdigit():
        sYear1 += c

for c in st2:
    if c.isdigit():
        sYear2 += c

year1 = int(sYear1)
year2 = int(sYear2)

if year1 > year2:
    print("Si")

else:
    print("no :(")