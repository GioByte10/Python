from DNA_Functions import *

print("author: Giovanni Bernal Ramirez")
print("Report any bug/problem/question/suggestion/improvement/etc to: gvanni.bernal10@gmail.com\n")
print("")

option = 0
print("DNA Calculations\n")
print("-1 to exit when on the main menu, and to go back to the main menu when on an option\n")


# def findSections(aminoAcids, indexes):


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

        if len(rna) > 2:

            modifiedRNA = correctTriplets(rna)
            aminoAcids = getAminoAcids(modifiedRNA.split())

            print("Amino Acids: ")

            for aminoAcid in aminoAcids:
                print(aminoAcid)

        else:
            print("No amino acids can be obtained as there are less than 3 bases\n")

        print("-----------------------------------------------------------------------------------------\n")


while True:

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
            print()

            if dna != "-1":
                if len(dna) > 0:
                    analyzeDNA(dna)

                else:
                    print("error: no string was entered\n")
            else:
                print()
                break

    elif option == 2:
        while True:
            rna = input("5'3' mRNA: ").upper()

            if rna != "-1":
                if len(rna) > 0:
                    if checkRna(rna):
                        rna = rewriteStr(rna)
                        rna = separateStr(rna)
                        print("           " + rna + '\n')

                        if len(rna) > 2:
                            rna = correctTriplets(rna)
                            aminoAcids = getAminoAcids(rna.split())

                            print("Amino Acids: ")

                            for aminoAcid in aminoAcids:
                                print(aminoAcid)

                        else:
                            print("No amino acids can be obtained as there are less than 3 bases\n")

                        print("-----------------------------------------------------------------------------------------\n")
                else:
                    print("error: no string was entered\n")
            else:
                break

    elif option == 3:
        while True:
            dna1 = input("First String: ").upper()

            if dna1 != "-1":
                if checkDna(dna1):
                    dna2 = input("Second String: ").upper()

                    if checkDna(dna2):
                        if len(cleanString(dna1)) == len(cleanString(dna2)):
                            print("There are " + str(hammingDistance(dna1, dna2)) + " mutations")
                            print()

                        else:
                            print("error: the strings do not have the same length\n")
            else:
                print()
                break

    elif option == 5:
        while True:
            string = input("DNA/RNA String: ").upper()

            if string != "-1":
                if checkIsGeneticMaterial(string, "DNA/RNA"):
                    if checkDnaOrRna(string, "DNA/RNA"):
                        motif = input("Motif: ").upper()

                        if checkIsGeneticMaterial(motif, "motif"):
                            if checkDnaOrRna(motif, "motif"):
                                if checkSameGeneticMaterial(string, motif):
                                    if len(string) >= len(motif):
                                        motifsPos = countingMotifs(string, motif)

                                        if len(motifsPos) != 0:
                                            print(
                                                "The are " + str(len(motifsPos)) + " " + motif + " motifs located at ",
                                                end='')

                                            for motifPos in motifsPos:
                                                print(motifPos, end='')

                                        else:
                                            print("There are no " + motif + " motifs")

                                        print(
                                            "-----------------------------------------------------------------------------------------\n")

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
