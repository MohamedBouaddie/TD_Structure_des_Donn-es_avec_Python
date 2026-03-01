a = float(input("Nombre 1 : "))
b = float(input("Nombre 2 : "))

# sans calculer a*b :
if a == 0 or b == 0:
    print("Le produit est nul")
elif (a > 0 and b > 0) or (a < 0 and b < 0):
    print("Le produit est positif")
else:
    print("Le produit est négatif")
