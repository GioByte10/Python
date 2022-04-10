import random
from math import log10


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
