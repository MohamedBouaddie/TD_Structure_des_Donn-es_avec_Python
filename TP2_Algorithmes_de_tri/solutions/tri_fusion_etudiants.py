def fusionner_etudiants(gauche, droite):
    res = []
    i = j = 0
    while i < len(gauche) and j < len(droite):
        # tri par note croissante
        if gauche[i][1] <= droite[j][1]:
            res.append(gauche[i])
            i += 1
        else:
            res.append(droite[j])
            j += 1
    res.extend(gauche[i:])
    res.extend(droite[j:])
    return res

def tri_fusion_etudiants(etudiants):
    if len(etudiants) <= 1:
        return etudiants
    mid = len(etudiants) // 2
    gauche = tri_fusion_etudiants(etudiants[:mid])
    droite = tri_fusion_etudiants(etudiants[mid:])
    return fusionner_etudiants(gauche, droite)

if __name__ == "__main__":
    etudiants = [("Ahmed", 15), ("Maryem", 12), ("Anas", 18), ("Safae", 14), ("Ali", 16), ("Fatima", 13)]
    print("Original :", etudiants)
    print("Trié     :", tri_fusion_etudiants(etudiants))
