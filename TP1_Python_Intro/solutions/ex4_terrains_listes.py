# terrain = (largeur, longueur)

l_terrains = []

# 1) Créer 3 terrains via saisie
for i in range(1, 4):
    larg = float(input(f"Largeur terrain{i} : "))
    long = float(input(f"Longueur terrain{i} : "))
    l_terrains.append((larg, long))

# 2) Afficher éléments
print("\nListe des terrains :", l_terrains)

# 3/4) Calculer l’aire de chaque terrain
print("\nAires :")
for idx, (larg, long) in enumerate(l_terrains, start=1):
    aire = larg * long
    print(f"terrain{idx} -> aire = {aire}")

# 5) Ajouter terrain4 à l’indice 2 et calculer son aire
larg4 = float(input("\nLargeur terrain4 : "))
long4 = float(input("Longueur terrain4 : "))
terrain4 = (larg4, long4)

l_terrains.insert(2, terrain4)
print("\nAprès insertion terrain4 à l'indice 2 :", l_terrains)
print("Aire terrain4 =", terrain4[0] * terrain4[1])

# 6) Supprimer terrain4
l_terrains.remove(terrain4)
print("\nAprès suppression terrain4 :", l_terrains)

# 7) Taille de la liste et affichage via len()
print("\nTaille =", len(l_terrains))
for t in l_terrains:
    print(t)
