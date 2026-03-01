grade = input("Grade (A/B/C/D/E) : ").strip().upper()
heures = int(input("Nombre d'heures : "))

# (tarif, seuilPrime, primeParSeuil)
grille = {
    "A": (200, 20, 1000),
    "B": (150, 20, 800),
    "C": (120, 15, 500),
    "D": (100, 15, 350),
    "E": (80, 10, 100),
}

if grade not in grille or heures < 0:
    print("Entrée invalide.")
else:
    tarif, seuil, prime = grille[grade]
    salaire_base = tarif * heures
    nb_blocs = heures // seuil
    salaire = salaire_base + nb_blocs * prime
    print(f"Salaire = {salaire} dh")
