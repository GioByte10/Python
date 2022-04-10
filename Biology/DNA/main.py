from math import ceil

from DNA_Functions import *

print("author: Giovanni Bernal Ramirez")
print("Report any bug/problem/question/suggestion/improvement/etc to: gvanni.bernal10@gmail.com\n")
print("")

print("Genetic Material Analyzer\n")
print("-1 to exit when on the main menu, and to go back to the main menu when on an option\n")

option = 0


# def findSections(aminoAcids, indexes):


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


while True:

    print("Select an option")
    print("1.- Analyze a DNA String")                       # Ready
    print("2.- Analyze a mRNA String")                      # almost Ready
    print("3.- Identify Point Mutations")
    print("4.- Identify Frameshift Mutations")
    print("5.- Count Motifs")
    print("6.- Random DNA/RNA String generator")            # Ready
    print("7.- Find Start/Stop (DNA/RNA?)")
    print("-1 to exit when on the main menu")
    option = input()

    if option.isnumeric() or option == "-1":
        option = int(option)

    print()

    if option == 1:
        while True:
            rna = analyzeDna()

            if rna:
                analyzeRna(rna)

            elif rna == '':
                break

    elif option == 2:
        while True:
            dna = analyzeRna()

            if dna:
                analyzeDna(dna)

            elif dna == '':
                break

    elif option == 3:
        while identifyPointMutations() is None:
            pass

    elif option == 5:
        while countMotifs() is None:
            pass

    elif option == 6:
        while generateRandomGeneticMaterial(input("String length: ")) is None:
            pass

    elif option == -1:
        break

    else:
        print("Not a valid option. Please enter a valid number\n")
