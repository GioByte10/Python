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

    return "There are " + str(a) + " A, " + str(t) + " T, " + str(c) + " C, " + str(g) + " G; a total of " + str(a + t + c+ g) + " bases"


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

        elif char == ' ':
            complement += ' '

    return complement


def fibonacciSequence(t, k):

    n1 = 0
    n2 = 1

    for i in range(t - 1):
        aux = n2
        n2 = n2 + k*n1
        n1 = aux

    return n2


def gc_Content(dnaString):
    i = 0

    dnaString = dnaString.replace(" ", "")

    for char in dnaString:
        if char == 'G' or char == 'C':
            i += 1

    return str((i / len(dnaString)) * 100)


def dnaToRna(dnaString):
    rnaString = ""

    for base in dnaString:
        if base == 'A':
            rnaString += 'U'

        elif base == 'T':
            rnaString += 'A'

        elif base == 'C':
            rnaString += 'G'

        elif base == 'G':
            rnaString += 'C'

    return separateRna(rnaString)


def separateRna(rnaString):
    new = ""

    for i in range(len(rnaString)):
        new += rnaString[i]

        if (i + 1) % 3 == 0:
            new += ' '

    return new


def getAminoAcids(codons):
    aminoAcids = []

    for codon in codons:
        aminoAcids.append(codonToAminoAcid(codon))

    return aminoAcids


def codonToAminoAcid(codon):
    if codon == "AUG":
        return "START - Methionine (Met)"

    elif codon == "AUA" or codon == "AUC" or codon == "AUU":
        return "Isoleucine (Ile)"

    elif (codon[0] == 'C' and codon[1] == 'G') or codon == "AGG" or codon == "AGA":
        return "Arginine (Arg)"

    elif codon == "CAG" or codon == "CAA":
        return "Glutamine (Gln)"

    elif codon == "CAU" or codon == "CAC":
        return "Histidine (His)"

    elif codon[0] == 'C' and codon[1] == 'C':
        return "Proline (Pro)"

    elif (codon[0] == 'C' and codon[1] == 'U') or codon == "UUG" or codon == "UUA":
        return "Leucine (Leu)"

    elif codon == "UGG":
        return "Tryptophan (Tpr)"

    elif codon == "UGA" or codon == "UAG" or codon == "UAA":
        return "STOP"

    elif codon == "UGC" or codon == "UGU":
        return "Cysteine (Cys)"

    elif codon == "UAU" or codon == "UAC":
        return "Tyrosine (Tyr)"

    elif (codon[0] == 'U' and codon[1] == 'C') or codon == "AGC" or codon == "AGU":
        return "Serine (Ser)"

    elif codon == "UUC" or codon == "UUU":
        return "Phenylalanine (Phe)"

    elif codon[0] == 'G' and codon[1] == 'G':
        return "Glycine (Gly)"

    elif codon == "GAG" or codon == "GAA":
        return "Glutamic Acid (Glu)"

    elif codon == "GAC" or codon == "GAU":
        return "Aspartic Acid (Asp)"

    elif codon[0] == 'G' and codon[1] == 'C':
        return "Alanine (Ala)"

    elif codon[0] == 'G' and codon[1] == 'U':
        return "Valine (Val)"

    elif codon == "AAG" or codon == "AAA":
        return "Lysine (Lys)"

    elif codon == "AAC" or codon == "AAU":
        return "Asparagine (Asn)"

    elif codon[0] == 'A' and codon[1] == 'C':
        return "Threonine (Thr)"


def hammingDistance(dna1, dna2):

    distance = 0

    dna1 = dna1.replace(" ", "")
    dna2 = dna2.replace(" ", "")

    for base in range(len(dna1)):
        if dna1[base] != dna2[base]:
            distance += 1

    return distance


def countingMotifs(dnaString, sub):

    motifs = []

    for base in range(len(dnaString) - len(sub) + 1):
        motif = ""

        for n in range(len(sub)):
            motif += dnaString[base + n]

        if motif == sub:
            motifs.append([base + 1, base + len(sub)])

    return motifs


def checkDna(dnaString):
    dnaString = dnaString.replace(" ", "")

    for base in dnaString:
        if base != 'A' and base != 'T' and base != 'C' and base != 'G':
            return False

    return True


def checkRna(rnaString):
    rnaString = rnaString.replace(" ", "")

    for base in rnaString:
        if base != 'A' and base != 'T' and base != 'C' and base != 'G':
            return False

    return True


def checkEitherDnaOrRna(string):
    string = string.replace(" ", "")

    for base in string:
        if base != 'A' and base != 'T' and base != 'C' and base != 'G' and base != 'U':
            return False

    return True


def checkDnaOrRna(string):
    if 'T' in string and 'U' in string:
        return False

    return True



"""def gc_Content(id, dnaString):
    i = 0

    for char in dnaString:
        if char == 'G' or char == 'C':
            i += 1

    return id + '\n' + str((i / len(dnaString)) * 100)
"""

