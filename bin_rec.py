def dec_to_bin(number):
    print("Aktualna liczba " + str(number))
    if number > 1:
        dec_to_bin(number//2)
    print("BINARNIE: " + str(number%2))


def dec_to_bin_with_return(number):
    child_reposne = ""
    if number > 1:
        child_reposne = dec_to_bin_with_return(number//2)
    return child_reposne + str(number%2)

print(dec_to_bin(79))


### Piotr --> rtoiP
def reverse_string(to_revers):
    """TODO"""
    pass