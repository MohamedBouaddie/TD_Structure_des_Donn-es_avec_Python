TVA = 0.2
total_ttc = 0.0

for i in range(1, 3):  # 2 articles
    nom = input(f"Nom article {i} : ")
    qte = int(input(f"Quantité {i} : "))
    pu = float(input(f"Prix unitaire {i} : "))

    ht = qte * pu
    ttc = ht + ht * TVA
    total_ttc += ttc

    print(f"Total pour l'article {nom} = {ht:.2f} dh (HT) | {ttc:.2f} dh (TTC)")

print(f"Total facture = {total_ttc:.2f} dh (TTC)")
