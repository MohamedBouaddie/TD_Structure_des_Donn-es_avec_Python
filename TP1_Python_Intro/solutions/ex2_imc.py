poids = float(input("Poids (kg) : "))
taille = float(input("Taille (m) : "))

imc = poids / (taille ** 2)
print(f"IMC = {imc:.2f}")
