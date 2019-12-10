# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def XO(letters):
    letters = letters.lower()
    countx = letters.count("x")
    counto = letters.count("o")
    if "x" in letters or "o" in letters:
        if countx == counto:
            print(True)
        else:
            print(False)
    else:
        print(False)

XO("ooxx")
XO("xooxx")
XO("ooxXm")
XO("zpzpzpp")
XO("zzoo")