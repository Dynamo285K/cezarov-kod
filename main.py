def cez(vstup:str, posun:int):
    kod = ''
    for i in vstup:
        a = (ord(i)-97+posun)%26+97
        x = chr(a)
        kod += x
    return kod
print(cez('stefan', 12))
print(cez('korabletioblohou', 5))
