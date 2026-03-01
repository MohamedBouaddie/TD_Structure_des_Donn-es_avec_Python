from tp1_m_calcul_air import aire_terrain

# 1) dictionnaires longueurs et largeurs
dict_long = {}
dict_larg = {}

for name in ["terrain1", "terrain2", "terrain3"]:
    l = float(input(f"Longueur {name} : "))
    w = float(input(f"Largeur  {name} : "))
    dict_long[name] = l
    dict_larg[name] = w

# 4) Fonctions demandées
def get_largeurs(d):
    return list(d.values())

def get_longueurs(d):
    return list(d.values())

def aire(name):
    return aire_terrain(dict_larg[name], dict_long[name])

# 2) Calcul des aires
print("\nAires terrain1..3 :")
for name in ["terrain1","terrain2","terrain3"]:
    print(name, "->", aire(name))

# 3) Ajouter terrain4
dict_long["terrain4"] = float(input("\nLongueur terrain4 : "))
dict_larg["terrain4"] = float(input("Largeur terrain4  : "))

print("\nAires terrain1..4 :")
for name in dict_long.keys():
    print(name, "->", aire(name))

print("\nLargeurs :", get_largeurs(dict_larg))
print("Longueurs :", get_longueurs(dict_long))
