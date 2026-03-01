a = float(input("Nombre 1 : "))
b = float(input("Nombre 2 : "))
op = input("Opération (+, -, *, /) : ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Erreur : division par zéro")
    else:
        print(a / b)
else:
    print("Opération inconnue")
