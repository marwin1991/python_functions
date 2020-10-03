# tupla -> (30.1111,90.22222)


# *args, **kwargs
# https://book.pythontips.com/en/latest/args_and_kwargs.html
def animals(*animals_names, **cities):
    for elem in animals_names:
        print(elem)

    print(animals_names)
    print(cities)

animals("cat", "dog", "mouse", city1="Cracow", city2="Warsow", city3="Wroclaw")