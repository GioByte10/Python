def countNucleotides(dnaString):
    g = 0
    t = 0
    a = 0
    c = 0

    for char in dnaString:
        if char == 'A':
            a += 1

        elif char == 'C':
            c += 1

        elif char == 'G':
            g += 1

        elif char == 'T':
            t += 1

    return str(a) + " " + str(c) + " " + str(g) + " " + str(t)


def dnaToRna(dna):
    dna = dna.replace('T', 'U')
    return dna


def reverseComplement(dna):
    dna = dna[::-1]
    complement = ""

    for char in dna:
        if char == 'A':
            complement += 'T'

        elif char == 'C':
            complement += 'G'

        elif char == 'G':
            complement += 'C'

        elif char == 'T':
            complement += 'A'

    return complement


def fibonacciSequence(t, k):

    n1 = 0
    n2 = 1

    for i in range(t - 1):
        aux = n2
        n2 = n2 + k*n1
        n1 = aux

    return n2


def gc_Content(id, dnaString):
    i = 0

    for char in dnaString:
        if char == 'G' or char == 'C':
            i += 1

    return id + '\n' + str((i / len(dnaString)) * 100)

