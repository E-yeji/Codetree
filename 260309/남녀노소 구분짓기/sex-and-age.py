wm = int(input())
age = int(input())

if wm == 0:
    if age >= 19:
        print("MAN")
    else:
        print("BOY")
elif wm == 1:
    if age >= 19:
        print("WOMAN")
    else:
        print("GIRL")