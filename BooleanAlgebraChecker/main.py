# (A + B) A'+ C
expression = input("expression: ")

expression = expression.replace('+', 'or')
print(expression)

literals = ''

for char in expression:
    if char.isalpha() and char not in literals:
        literals += char

literals = sorted(literals)

nLiterals = len(literals)
print(nLiterals)

values = []

for literal in literals:
    values.append(0)
