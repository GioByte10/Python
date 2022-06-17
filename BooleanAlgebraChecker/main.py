import itertools

# (A + B) A'+ C
expression = input("expression: ")

literals = ''

for char in expression:
    if char.isalpha() and char not in literals:
        literals += char

literals = sorted(literals)
nLiterals = len(literals)

expression = expression.replace(' ', '')
expression = expression.replace('+', ' + ')
expression = expression.replace('+', 'or')

print(expression)

temp = ''

for i in range(len(expression) - 1):
    temp += expression[i]
    if (expression[i] == ')' or expression[i] in literals) and (expression[i + 1] in literals or expression[i+1]):
        temp += ' and '

expression = temp

print(expression)

for literal in literals:
    expression = expression.replace(literal + '\'', ' not ' + literal)

print(expression)

s = 0
e = len(expression)

while True:
    i = expression[s:e].find(')')

    if i == -1:
        break

    if expression[i + 1] == '\'':
        expression = expression.replace('(', ' not (')

    s = i + 5
    e += i + 5

print(expression)
values = [list(i) for i in itertools.product([0, 1], repeat=nLiterals)]
