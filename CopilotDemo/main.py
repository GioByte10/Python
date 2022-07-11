# Converts decimal to binary and back
def dec_to_bin(dec):
    bin = ""
    while dec > 0:
        bin = str(dec % 2) + bin
        dec = dec // 2
    return bin

print(dec_to_bin(10))