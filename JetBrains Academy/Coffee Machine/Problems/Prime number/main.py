num = int(input())

# If given number is greater than 1
if num > 1:

    # Iterate from 2 to n / 2
    for i in range(2, num):

        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print("This number is not prime")
            break

    else:
        print("This number is prime")

else:
    print("This number is not prime")