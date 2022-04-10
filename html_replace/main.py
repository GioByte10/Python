old = input("old: ")
new = input("new: ")

file = open("html.txt", 'r', encoding="utf8")
s = file.read()
s = s.replace(old, new)

file.close()

f = open("html_new.txt", 'w')
f.write(s)
f.close()


