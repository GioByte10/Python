
if __name__ == '__main__':                                       # Runs only if the file is run directly
    print("Hello, World!")

    print(type("Hi"))                                           # str
    print(type(10))                                             # int
    print(type(256.87))                                         # float
    print()

    test_variable = 90                                          # snake_case for variables
    print(str(test_variable) + " of type "                      # Concatenating using str()
          + str(type(test_variable)))

    test_variable = "test variable"                             # Python uses dynamic typing; variables can change type
    print(f'{test_variable} of type {type(test_variable)}')     # Concatenating using f-string

    test_variable = 57.984
    print("{} of type {}".format(test_variable,                 # Concatenating using format()
                                 type(test_variable)))
