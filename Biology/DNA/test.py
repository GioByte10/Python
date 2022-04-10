from All_functions import*


def analyzeDna_tests():
    tests = [
        "-1",
        "-",
        "          ",
        "dSDMID032OM",
        "",
        "d"
        "10",
        "null",
        "CATTACGTAGU",
        "CAT ATT  TTTTT TATAT TTTTA",
        "CAUT 1_ C",
        "CAT TAG GCA TAG GAC GGC",
        "CAT---TAG-GAT----CAG   TA",
        "CAT-GGA-GAG-GATA",
        "C",
        "CA",
        "uasus",
        "agctag",
        "agc cga",
        "acg---agc",
        "acgag    agc"
    ]

    for test in tests:
        analyzeDna(test)


def analyzeRna_tests():
    tests = [
        "-1",
        "-",
        "          ",
        "dSDMID032OM",
        "",
        "d",
        "10",
        "null",
        "CATTACGTAGU",
        "CAU UAUAU CCAU",
        "CAU 1_ C",
        "CAU UAG GCA UAG GAC GGC",
        "CAU---AG-GAU----CAG   UA",
        "CAU-GGA-GAG-GAUA",
        "C",
        "CA",
        "aucguacua--  acuaccguc",
        "uag cuuuu augh",
        "uag gaggga    gaag"
    ]

    for test in tests:
        analyzeRna(test)


def generateRandomGeneticMaterial_tests():
    tests = [
        "0",
        "null",
        "none",
        "vmuisvmsi",
        "___",
        "",
        "   ",
        "----",
        "o,dwod,w",
        "-1",
        "1",
        "2",
        "3",
        "5",
        "10",
        "100",
        "500",
        "1000",
        "5000"
    ]

    for test in tests:
        generateRandomGeneticMaterial(test)


# analyzeDna_tests()
# analyzeRna_tests()
# generateRandomGeneticMaterial_tests()

