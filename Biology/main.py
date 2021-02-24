from Genetics import*

print("author: Giovanni Bernal Ramirez")

option = 0
print("DNA Calculations\n")

while True:

    print("Select an option")
    print("1.- Analyze a DNA String")
    print("2.- Count Point Mutations")
    print("3.- Count Motifs")
    print("-1 to exit")
    option = input()

    if option.isnumeric() or option == "-1":
        option = int(option)

    print()

    if option == 1:
        while True:
            dna = input("               DNA: ")

            if dna != "-1":
                if checkDna(dna):
                    if len(dna.replace(" ", "")) % 3 == 0:

                        print("Reverse-complement: " + reverseComplement(dna) + '\n')
                        print(countNucleotides(dna) + "          The GC content is " + gc_Content(dna) + "%\n")

                        rna = dnaToRna(dna)
                        print("RNA: " + rna + '\n')

                        aminoAcids = getAminoAcids(rna.split())

                        print("Amino Acids: ")

                        for aminoAcid in aminoAcids:
                            print(aminoAcid)

                        print()

                    else:
                        print("error: the DNA String contains " + str(len(dna.replace(" ", ""))) + " bases, which is not a multiple of 3\n")
                else:
                    print("error: there are characters other than the bases in the DNA String\n")
            else:
                print()
                break

    elif option == 2:
        while True:
            dna1 = input("First String: ")

            if dna1 != "-1":
                if checkDna(dna1):
                    if len(dna1.replace(" ", "")) % 3 == 0:
                        dna2 = input("Second String: ")

                        if checkDna(dna2):
                            if len(dna2.replace(" ", "")) % 3 == 0:
                                if len(dna1.replace(" ", "")) == len(dna2.replace(" ", "")):
                                    print("There are " + str(hammingDistance(dna1, dna2)) + " mutations")
                                    print()

                                else:
                                    print("error: the DNA Strings do not have the same length\n")
                            else:
                                print("error: the second DNA String contains " + str(len(dna2.replace(" ", ""))) + " bases, which is not a multiple of 3\n")
                        else:
                            print("error: the second DNA String contains characters other than the bases in the DNA String\n")
                    else:
                        print("error: the first DNA String contains " + str(len(dna1.replace(" ", ""))) + " bases, which is not a multiple of 3\n")
                else:
                    print("error: the first DNA String contains characters other than the bases in the DNA String\n")
            else:
                print()
                break

    elif option == 3:
        while True:
            dna = input("DNA/RNA String: ")

            if dna != "-1":
                if checkDna(dna):
                    motif = input("Motif: ")

                    if len(dna) > len(motif):
                        motifsPos = countingMotifs(dna, motif)

                        if len(motifsPos) != 0:
                            print("The are " + str(len(motifsPos)) + " " + motif + " motifs located at " + str(motifsPos))

                        else:
                            print("There are no " + motif + " motifs")

                        print()

                    else:
                        print("error: the motif must be shorter then the DNA String\n")
                else:
                    print("error: the DNA String contains characters other than the bases in the DNA String\n")
            else:
                print()
                break

    elif option == -1:
        break

    else:
        print("Not a valid option. Please enter a valid number\n")

