def tri_insertion_affichage(liste):
    a = liste[:]
    for i in range(1, len(a)):
        cle = a[i]
        j = i - 1
        while j >= 0 and a[j] > cle:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = cle
        print(f"Après insertion i={i} :", a)
    return a

def tri_insertion_sentinelle(liste):
    # sentinelle : placer le minimum en position 0
    a = liste[:]
    if not a:
        return a

    imin = min(range(len(a)), key=lambda k: a[k])
    a[0], a[imin] = a[imin], a[0]

    for i in range(2, len(a)):
        cle = a[i]
        j = i - 1
        while a[j] > cle:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = cle
    return a

if __name__ == "__main__":
    tri_insertion_affichage([31, 41, 59, 26, 41])
    print(tri_insertion_sentinelle([31, 41, 59, 26, 41]))
