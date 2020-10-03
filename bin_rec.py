

def dec_to_bin(number):
    print("Aktualna liczba " + str(number))
    if number > 1:
        dec_to_bin(number//2)
    print("BINARNIE: " + str(number%2))


dec_to_bin(79)