print("Input two strings to compare them")


def detect_pattern(s1, s2):
    c1 = None
    c2 = None

    if len(s1) == len(s2):
        for i in range(len(s1) - 1):
            for j in range(len(s1) - i - 1):
                if s1[i] == s1[j + i + 1]:
                    c1 = i
                    c2 = j + i + 1


        if c1 is None:
            return True

        elif s2[c1] == s2[c2]:
            return True

        else:
            return False

    else:
        return False


while True:
    str1 = input("String 1: ")
    str2 = input("String 2: ")
    print(str(detect_pattern(str1, str2)))
