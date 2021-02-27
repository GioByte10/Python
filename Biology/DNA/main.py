from DNA_Functions import*

print("author: Giovanni Bernal Ramirez")
print("Report any bug/problem/suggestion/improvement to: gvanni.bernal10@gmail.com\n")
print("")

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
            dna = input("          3'5' DNA: ")

            if dna != "-1":
                if checkDna(dna):
                    if len(dna.replace(" ", "")) % 3 == 0:

                        print("Reverse-complement: " + reverseComplement(dna) + '\n')
                        print(countNucleotides(dna) + "          The GC content is " + gc_Content(dna) + "%\n")

                        rna = dnaToRna(dna)
                        print("5'3' RNA: " + rna + '\n')

                        aminoAcids = getAminoAcids(rna.split())

                        print("Amino Acids: ")

                        for aminoAcid in aminoAcids:

                            print(aminoAcid)

                        print()

                    else:
                        print("error: the DNA String contains " + str(len(dna.replace(" ", ""))) + " bases, which is not a multiple of 3\n")
                else:
                    print("error: there are characters other than the bases in a DNA String\n")
            else:
                print()
                break

    elif option == 2:
        while True:
            dna1 = input("First String: ")

            if dna1 != "-1":
                if checkDna(dna1):

                    dna2 = input("Second String: ")

                    if checkDna(dna2):
                        if len(dna1.replace(" ", "")) == len(dna2.replace(" ", "")):
                            print("There are " + str(hammingDistance(dna1, dna2)) + " mutations")
                            print()

                        else:
                            print("error: the DNA Strings do not have the same length\n")
                    else:
                        print("error: the second DNA String contains characters other than the bases in a DNA String\n")
                else:
                    print("error: the first DNA String contains characters other than the bases in a DNA String\n")
            else:
                print()
                break

    elif option == 3:
        while True:
            string = input("DNA/RNA String: ")

            if string != "-1":
                if checkEitherDnaOrRna(string):
                    if checkDnaOrRna(string):
                        motif = input("Motif: ")

                        if checkEitherDnaOrRna(motif):
                            if checkDnaOrRna(motif):
                                if len(string) > len(motif):
                                    motifsPos = countingMotifs(string, motif)

                                    if len(motifsPos) != 0:
                                        print("The are " + str(len(motifsPos)) + " " + motif + " motifs located at " + str(motifsPos))

                                    else:
                                        print("There are no " + motif + " motifs\n")

                                    print()

                                else:
                                    print("error: the motif must be shorter then the DNA String\n")
                            else:
                                print("error: the motif String can not contain T and U\n")
                        else:
                            print("error: the motif contains characters other than the bases in a DNA or RNA String\n")
                    else:
                        print("error: the DNA/RNA String can not contain T and U\n")
                else:
                    print("error: the String contains characters other than the bases in a DNA or RNA String\n")
            else:
                print()
                break

    elif option == -1:
        break

    else:
        print("Not a valid option. Please enter a valid number\n")

