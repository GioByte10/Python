from Genetics import*

dna = input("               DNA: ")
print("Reverse-complement: " + reverseComplement(dna) + '\n')

print(countNucleotides(dna) + "          The GC content is " + gc_Content(dna) + "%\n")


rna = dnaToRna(dna)
print("RNA: " + rna + '\n')

aminoAcids = getAminoAcids(rna.split())

print("Amino Acids: ")

for aminoAcid in aminoAcids:
    print(aminoAcid)





