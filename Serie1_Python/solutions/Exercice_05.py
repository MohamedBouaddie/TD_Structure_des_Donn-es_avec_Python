n = int(input("Saisir un entier : "))

if n % 2 == 0:
    print("Ce nombre est pair")
elif n % 3 == 0:
    print("Ce nombre est impair, mais est multiple de 3")
else:
    print("Ce nombre n’est ni pair ni multiple de 3")
