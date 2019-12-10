def namelist(names):
    listLength = len(names)
    phrase = []
    if listLength > 2:
        for name in names:
            phrase.append(name['name'])
        phrase.insert(-1, "&")
        final = ", ".join(phrase)
        print(final)


namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])