import random


def rewriteStr(string):
    new = ""
    char = ''

    if '-' in string:
        char = '-'

    elif ' ':
        char = ' '

    string = cleanString(string)

    for i, base in enumerate(string):
        new += base

        if not (i + 1) % 3:
            new += char

    if new[-1] == '-' or new[-1] == ' ':
        new = new[:-1]

    return new


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

    return f"There are {a} A, {t} T, {c} C, {g} G; a total of {a + t + c + g} bases"


def dna_complement(dna):
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

        else:
            complement += char

    return complement


def dna_reverseComplement(complement_dna):
    reverseComplement = complement_dna[::-1]
    return rewriteStr(reverseComplement)


def rna_complement(dna):
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


def addBonds(dna):
    bonds = ""

    for char in dna:
        if char != ' ' and char != '-':
            bonds += '|'
        else:
            bonds += ' '

    return "                    " + bonds


def gc_Content(dnaString):
    i = 0

    dnaString = cleanString(dnaString)

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

    return separateStr(rnaString)


def rnaToDna(rnaString):
    dnaString = ""

    for base in rnaString:
        if base == 'U':
            dnaString += 'A'

        elif base == 'A':
            dnaString += 'T'

        elif base == 'G':
            dnaString += 'C'

        elif base == 'C':
            dnaString += 'G'

    return separateStr(dnaString)


def separateStr(string):
    string = cleanString(string)
    new = ""

    for i, a in enumerate(string):
        new += a

        if not (i + 1) % 3:
            new += ' '

    return new


def getAminoAcids(codons):
    for codon in codons:
        aminoAcid = codonToAminoAcid(codon)
        yield aminoAcid + (" " * (27 - len(aminoAcid))) + codon


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

    elif codon == "UAG":
        return "STOP - Amber"

    elif codon == "UAA":
        return "STOP - Ochre"

    elif codon == "UGA":
        return "STOP - Opal"

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


def hammingDistance(str1, str2):
    arrw = "               "

    distance = 0

    for base1, base2 in zip(str1, str2):
        if base1 != base2:
            arrw += '^'

        else:
            arrw += ' '

    print(arrw)

    str1 = cleanString(str1)
    str2 = cleanString(str2)

    for base1, base2 in zip(str1, str2):
        if base1 != base2:
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
    dnaString = cleanString(dnaString)

    for base in dnaString:
        if base != 'A' and base != 'T' and base != 'C' and base != 'G':
            print("error: there are characters other than the bases in a DNA String\n")
            return False

    return True


def checkRna(rnaString):
    rnaString = cleanString(rnaString)

    for base in rnaString:
        if base != 'A' and base != 'U' and base != 'C' and base != 'G':
            print("error: there are characters other than the bases in a RNA String\n")
            return False

    return True


def correctTriplets(string):
    if not len(cleanString(string)) % 3:
        return string

    print("The last amino acid cannot be obtained, as the mRNA string contains " + str(
        len(cleanString(string))) + " bases, which is not a multiple of 3\n")

    subS = (len(cleanString(string)) // 3) * 3 + len(cleanString(string)) // 3 - 1
    return string[:subS]


def checkIsGeneticMaterial(string, part):
    string = cleanString(string)

    for base in string:
        if base != 'A' and base != 'T' and base != 'C' and base != 'G' and base != 'U':
            print("error: the " + part + " String contains characters other than the bases in a DNA or RNA String\n")
            return False

    return True


def checkDnaOrRna(string, part):
    if 'T' in string and 'U' in string:
        print("error: the " + part + " String can not contain T and U\n")
        return False

    return True


def checkSameGeneticMaterial(string1, string2):
    if ('T' in string1 and 'U' in string2) or ('U' in string1 and 'T' in string2):
        print("Both strings must be of the same type (DNA or RNA)\n")
        return False

    return True


def cleanString(string):
    return string.replace(" ", "").replace("-", "")


def generateRandomDNA(length):
    string = ""

    for c in range(length):
        i = random.randint(0, 3)

        if c != 0 and c % 3 == 0:
            string += ' '

        if i == 0:
            c = 'A'

        elif i == 1:
            c = 'C'

        elif i == 2:
            c = 'G'

        elif i == 3:
            c = 'T'

        string += c

    return string
