import random
from math import log10, ceil


def rewriteStr(string):
    """
    rewrites a string to a correct format if not already

    spacing is either '-' or ' '
    """
    same = False
    new = ''

    char = '-' if '-' in string else ' '

    cleaned = cleanString(string)

    for i, base in enumerate(cleaned):
        new += base

        if not (i + 1) % 3:
            new += char + (int(log10((i + 1) / 3)) - 2) * char

    if new[-1] == '-' or new[-1] == ' ':
        new = new[:-1]

    if new == string:
        same = True

    return same, new


def countNucleotides(dnaString):
    """
    counts dna nucleotides

    returns the total number of bases of each base
    """
    g = 0
    t = 0
    a = 0
    c = 0

    for base in dnaString:
        if base == 'A':
            a += 1

        elif base == 'C':
            c += 1

        elif base == 'G':
            g += 1

        elif base == 'T':
            t += 1

    return f"There are {a} A, {t} T, {c} C, and {g} G; a total of {a + t + c + g} bases"


def dnaComplement(dna):
    """
    returns the dna complement
    """
    complement = ''

    for base in dna:
        if base == 'A':
            complement += 'T'

        elif base == 'C':
            complement += 'G'

        elif base == 'G':
            complement += 'C'

        elif base == 'T':
            complement += 'A'

        else:
            complement += base

    return complement


def dnaReverseComplement(complement_dna):
    """
    returns the dna reverse complement by reversing the complement
    """
    reverseComplement = complement_dna[::-1]
    return rewriteStr(reverseComplement)


def rnaComplement(dna):
    """
    returns the rna complement
    """
    complement = ""

    for base in dna:
        if base == 'A':
            complement += 'T'

        elif base == 'C':
            complement += 'G'

        elif base == 'G':
            complement += 'C'

        elif base == 'T':
            complement += 'A'

        else:
            complement += base

    return complement


def addBonds(dna):
    """
    Adds bonds (|) between the dna and its complement

    returns a string with the bonds
    """
    bonds = ''

    for char in dna:
        bonds += '|' if not (char == ' ' or char == '-') else ' '

    return "                    " + bonds


def gcContent(dnaString):
    """
    calculates the percentage of g & c bases in a dna string

    returns the gc content
    """
    i = 0

    dnaString = cleanString(dnaString)

    for char in dnaString:
        i += 1 if char == 'G' or char == 'C' else 0

    return (i / len(dnaString)) * 100


def dnaToRna(dnaString):
    """
    inverts the DNA bases

    returns the RNA of a DNA string
    """
    rnaString = ''

    for base in dnaString:
        if base == 'A':
            rnaString += 'U'

        elif base == 'T':
            rnaString += 'A'

        elif base == 'C':
            rnaString += 'G'

        elif base == 'G':
            rnaString += 'C'

        else:
            rnaString += base

    return separateStr(rnaString)


def rnaToDna(rnaString):
    """
    inverts the RNA bases

    returns the DNA of a RNA string
    """
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
    """
    returns a string with a space added every three characters

    ATC GTA CTA
    """
    string = cleanString(string)
    new = ""

    for i, a in enumerate(string):
        new += a

        if not (i + 1) % 3:
            new += ' '

    if new[-1] == ' ':
        new = new[:-1]

    return new


def getAminoAcids(codons):
    """
    yields an amino acid from a given list of codons
    """
    for codon in codons:
        aminoAcid = codonToAminoAcid(codon)
        yield aminoAcid + (" " * (27 - len(aminoAcid))) + codon


def codonToAminoAcid(codon):
    """
    returns an amino acid from a given codon
    """
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
    """
    Adds '^' indicating where the mutation is located

    returns the hamming distance
    """
    arrw = "               "

    distance = 0

    for base1, base2 in zip(str1, str2):
        arrw += '^' if base1 != base2 else ' '

    print(arrw)

    str1 = cleanString(str1)
    str2 = cleanString(str2)

    for base1, base2 in zip(str1, str2):
        if base1 != base2:
            distance += 1

    return distance


def countingMotifs(dnaString, motif):
    """
    returns the index of the motifs in the DNA string
    """

    motifIndexes = []

    while True:
        index = dnaString.find(motif)

        if index != -1:
            motifIndexes.append([index + 1, index + len(motif)])

        else:
            return motifIndexes

        sl = index + len(motif) - len(dnaString)
        dnaString = dnaString[sl:] if sl != 0 else ''


def checkDna(dnaString):
    dnaString = cleanString(dnaString)

    for base in dnaString:
        if base not in "ATCG":
            print("error 0x04: there are characters other than the bases in a DNA String\n")
            return False

    return True


def checkRna(rnaString):
    rnaString = cleanString(rnaString)

    for base in rnaString:
        if base not in "AUCG":
            print("error 0x05: there are characters other than the bases in a RNA string\n")
            return False

    return True


def correctTriplets(string):
    """
    Checks if the RNA string can be separated in triplets

    returns a slice of the string if not
    """
    error = ''

    if not len(cleanString(string)) % 3:
        return string, error

    error = "The last amino acid cannot be obtained, as the mRNA string contains " + str(
        len(cleanString(string))) + " bases, which is not a multiple of 3\n"

    subS = (len(cleanString(string)) // 3) * 3 + len(cleanString(string)) // 3 - 1
    return string[:subS], error


def checkIsGeneticMaterial(string, part):
    """
    Checks if the string contains bases other than those of DNA or RNA
    """
    string = cleanString(string)

    for base in string:
        if base not in "ATUCG":
            print("error 0x06: the " + part + " string contains characters other than the bases in a DNA or RNA string\n")
            return False

    return True


def checkDnaOrRna(string, part):
    """
    Checks that the string is either DNA or RNA (not both)
    """
    if 'T' in string and 'U' in string:
        print("error 0x07: the " + part + " string can not contain T and U\n")
        return False

    return True


def checkSameGeneticMaterial(string1, string2):
    """
    Checks if both strings are of the same genetic material
    """
    if ('T' in string1 and 'U' in string2) or ('U' in string1 and 'T' in string2):
        print("Both strings must be of the same genetic material (DNA or RNA)\n")
        return False

    return True


def cleanString(string):
    """
    removes all spaces and '-' of a string
    """
    return string.replace(" ", "").replace("-", "")


def randomGeneticMaterial(length, geneticMaterial):
    """
    Generates a random string of bases of the given genetic material (DNA or RNA)
    """
    s = ''
    if geneticMaterial == "DNA":
        s = "".join(random.choice("ATCG") for _ in range(length))

    elif geneticMaterial == "RNA":
        s = "".join(random.choice("AUCG") for _ in range(length))

    return rewriteStr(s)[1]


def checkString(string):
    """
    Checks a string for: not empty, no digits, letters only

    returns true if the string passes all tests
    """
    if string:
        string = cleanString(string)

        if not any(char.isdigit() for char in string):
            if string.isalpha():
                return True

            else:
                print("error 0x00: the string must contain letters\n")

        else:
            print("error 0x01: the string cannot contain a number\n")

    else:
        print("error 0x02: no string was entered\n")

    return False


def checkRna_m_Triplet(rna):
    """
    Checks mRNA can form at least 1 triplet

    returns true if so
    """
    if len(rna) > 2:
        return True

    print("No amino acids can be obtained as there are less than 3 bases\n")
    return False


def checkSameLength(str1, str2):
    """
    checks that both strings have the same length

    returns true if so
    """
    if len(cleanString(str1)) == len(cleanString(str2)):
        return True

    else:
        print("error 0x03: the strings do not have the same length\n")

    return False


def analyzeDna(st='_', en=True):  # Option 1
    if st == '_':
        dna = input("          3'5' DNA: ")

    else:
        dna = st
        print("          3'5' DNA: " + dna)

    lower = False

    if any(char.islower() for char in dna):
        lower = True
        dna = dna.upper()

    if dna != "-1":
        if checkString(dna) and checkDna(dna):
            same, dna = rewriteStr(dna)

            if not same or lower:
                print("          3'5' DNA: " + dna)

            print(addBonds(dna))
            complement = dnaComplement(dna)
            print("        Complement: " + complement)
            print("Reverse-complement: " + dnaReverseComplement(complement)[1])

            string1 = ''
            indexString = ''

            nDna = ceil(len(cleanString(dna)) / 3)

            for tripletIndex in range(nDna):
                n1 = 3 - len(str(tripletIndex + 1))
                n2 = len(str(tripletIndex + 1)) - 3

                string1 += "^   " + n2 * ' '
                indexString += str(tripletIndex + 1) + n1 * ' ' + ' '

            print("                    " + string1)
            print("                    " + indexString + '\n')

            print(countNucleotides(dna) + "          The GC content is " + str(gcContent(dna)) + "%\n")

            if en:
                print("-----------------------------------------------------------------------------------------\n")

            rna = dnaToRna(dna)
            return rna
    else:
        print()
        return ''


def analyzeRna(st='_', en=True):  # Option 2
    if st == '_':
        rna = input("         5'3' mRNA: ")

    else:
        rna = st
        print("         5'3' mRNA: " + rna)

    lower = False

    if any(char.islower() for char in rna):
        lower = True
        rna = rna.upper()

    if rna != "-1":
        if checkString(rna) and checkRna(rna):
            same, rna = rewriteStr(rna)

            if not same or lower:
                print("         5'3' mRNA: " + rna)

            if checkRna_m_Triplet(rna):
                rna, error = correctTriplets(separateStr(rna))
                codons = separateStr(rna).split()
                aminoAcids = getAminoAcids(codons)

                string1 = ''
                indexString = ''

                nCodons = len(codons)

                for aminoAcidIndex in range(nCodons):
                    n1 = 3 - len(str(aminoAcidIndex + 1))
                    n2 = len(str(aminoAcidIndex + 1)) - 3

                    string1 += "^   " + n2 * ' '
                    indexString += str(aminoAcidIndex + 1) + n1 * ' ' + ' '

                print("                    " + string1)
                print("                    " + indexString + '\n')

                if error:
                    print(error)

                print("Amino Acids: ")

                for i, aminoAcid in enumerate(aminoAcids):
                    print(aminoAcid + '   ' + str(i + 1))

                print()

            if en:
                print("-----------------------------------------------------------------------------------------\n")

            dna = rnaToDna(rna)
            return dna
    else:
        print()
        return ''


def identifyPointMutations():  # Option 3
    str1 = input("First String:  ").upper()

    if str1 != "-1":
        if checkString(str1):
            if checkIsGeneticMaterial(str1, "DNA/RNA") and checkDnaOrRna(str1, "DNA/RNA"):
                # str1 = rewriteStr(str1)
                str2 = input("Second String: ").upper()

                if checkString(str2):
                    if checkIsGeneticMaterial(str2, "DNA/RNA") and checkDnaOrRna(str2, "DNA/RNA"):
                        # str2 = rewriteStr(str2)

                        if checkSameGeneticMaterial(str1, str2):
                            if checkSameLength(str1, str2):
                                print("There are " + str(hammingDistance(str1, str2)) + " mutations")
                                print()

    else:
        print()
        return False


def countMotifs():  # Option 5
    string = input("DNA/RNA String: ").upper()

    if string != "-1":
        if checkString(string) and checkIsGeneticMaterial(string, "DNA/RNA") and checkDnaOrRna(string, "DNA/RNA"):
            motif = input("Motif: ").upper()

            if checkString(motif) and checkIsGeneticMaterial(motif, "motif") and checkDnaOrRna(motif, "motif") and checkSameGeneticMaterial(string, motif):
                if len(string) >= len(motif):
                    motifsPos = countingMotifs(string, motif)

                    if len(motifsPos) != 0:
                        print("The are " + str(len(motifsPos)) + " " + motif + " motifs located at ", end='')

                        for motifPos in motifsPos:
                            print(motifPos, end='')

                        print()

                    else:
                        print("There are no " + motif + " motifs")

                    print("-----------------------------------------------------------------------------------------\n")
                else:
                    print("error 0x08: the motif must be shorter than the DNA/RNA String\n")
    else:
        print()
        return False


def generateRandomGeneticMaterial(l):                # Option 6
    if l.isnumeric() or l == "-1":
        l = int(l)

        if l == -1:
            print()
            return False

        if l > 0:
            print()
            randomDNA = randomGeneticMaterial(l, "DNA")
            rna = analyzeDna(randomDNA, False)
            analyzeRna(rna)

        else:
            print("error 0x09: please enter a number greater than 0\n")
    else:
        print("error 0x0A: please enter a valid integer\n")