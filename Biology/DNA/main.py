from DNA_Functions import *

print("author: Giovanni Bernal Ramirez")
print("Report any bug/problem/question/suggestion/improvement/etc to: gvanni.bernal10@gmail.com\n")
print("")

print("Genetic Material Analyzer\n")
print("-1 to exit when on the main menu, and to go back to the main menu when on an option\n")

option = 0


# def findSections(aminoAcids, indexes):


def checkString(string):                                    # general string checks
    if string:
        string = string.replace(" ", "").replace("-", "")

        if not any(char.isdigit() for char in string):
            if string.isalpha():
                return True

            else:
                print("\nerror: the string must contain letters\n")

        else:
            print("\nerror: the string cannot contain a number\n")

    else:
        print("\nerror: no string was entered\n")

    return False


def checkRna_m_Triplet(rna):                                # Checks mRNA can form at least 1 triplet
    if len(rna) > 2:
        return True

    print("No amino acids can be obtained as there are less than 3 bases\n")
    return False


def checkSameLength(str1, str2):
    if len(cleanString(str1)) == len(cleanString(str2)):
        return True

    else:
        print("error: the strings do not have the same length\n")

    return False


def analyzeDNA(dna):
    if checkDna(dna):
        dna = rewriteStr(dna)
        print("          3'5' DNA: " + dna)
        print(addBonds(dna))
        complement = dna_complement(dna)
        print("        Complement: " + complement)
        print("Reverse-complement: " + dna_reverseComplement(complement) + '\n')
        print(countNucleotides(dna) + "          The GC content is " + gc_Content(dna) + "%\n")

        rna = dnaToRna(dna)
        print("5'3' mRNA: " + rna + '\n')

        if checkRna_m_Triplet(rna):

            modifiedRNA = correctTriplets(rna)
            aminoAcids = getAminoAcids(modifiedRNA.split())

            print("Amino Acids: ")

            for aminoAcid in aminoAcids:
                print(aminoAcid)

        print("-----------------------------------------------------------------------------------------\n")


while True:

    dna = ""
    aminoAcid = ""
    rna = ""
    aminoAcids = ""

    print("Select an option")
    print("1.- Analyze a DNA String")
    print("2.- Analyze a mRNA String")
    print("3.- Identify Point Mutations")
    print("4.- Identify Frameshift Mutations")
    print("5.- Count Motifs")
    print("6.- Random DNA String generator")
    print("7.- Find Start/Stop")
    print("-1 to exit when on the main menu")
    option = input()

    if option.isnumeric() or option == "-1":
        option = int(option)

    print()

    if option == 1:
        while True:
            dna = input("          3'5' DNA: ").upper()

            if dna != "-1":
                if checkString(dna):
                    analyzeDNA(dna)

            else:
                print()
                break

    elif option == 2:
        while True:
            rna = input("5'3' mRNA: ").upper()

            if rna != "-1":
                if checkString(rna):
                    if checkRna(rna):
                        rna = rewriteStr(rna)
                        rna = separateStr(rna)
                        print("           " + rna + '\n')

                        if checkRna_m_Triplet(rna):
                            rna = correctTriplets(rna)
                            aminoAcids = getAminoAcids(rna.split())

                            print("Amino Acids: ")

                            for aminoAcid in aminoAcids:
                                print(aminoAcid)

                        print("-----------------------------------------------------------------------------------------\n")

            else:
                break

    elif option == 3:
        while True:
            str1 = input("First String:  ").upper()

            if str1 != "-1":
                if checkString(str1):
                    if checkIsGeneticMaterial(str1, "DNA/RNA"):
                        # str1 = rewriteStr(str1)
                        str2 = input("Second String: ").upper()

                        if checkString(str2):
                            if checkIsGeneticMaterial(str2, "DNA/RNA"):
                                # str2 = rewriteStr(str2)

                                if checkSameGeneticMaterial(str1, str2):
                                    if checkSameLength(str1, str2):
                                        print("There are " + str(hammingDistance(str1, str2)) + " mutations")
                                        print()

            else:
                print()
                break

    elif option == 5:
        while True:
            string = input("DNA/RNA String: ").upper()

            if string != "-1":
                if checkString(string):
                    if checkIsGeneticMaterial(string, "DNA/RNA"):
                        if checkDnaOrRna(string, "DNA/RNA"):
                            motif = input("Motif: ").upper()

                            if checkIsGeneticMaterial(motif, "motif"):
                                if checkDnaOrRna(motif, "motif"):
                                    if checkSameGeneticMaterial(string, motif):
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
                                            print("error: the motif must be shorter than the DNA/RNA String\n")
            else:
                print()
                break

    elif option == 6:
        while True:
            l = input("String length: ")

            if l.isnumeric() or l == "-1":
                l = int(l)

                if l == -1:
                    print()
                    break

                if l > 0:
                    randomDNA = generateRandomDNA(l)
                    analyzeDNA(randomDNA)

                else:
                    print("error: please enter a number greater than 0\n")
            else:
                print("error: please enter a valid integer\n")

    elif option == -1:
        break

    else:
        print("Not a valid option. Please enter a valid number\n")
