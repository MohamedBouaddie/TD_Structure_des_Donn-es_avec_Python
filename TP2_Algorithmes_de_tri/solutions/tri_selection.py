def tri_selection(liste):
    a = liste[:]  # copie
    n = len(a)
    for i in range(n - 1):
        imin = i
        for j in range(i + 1, n):
            if a[j] < a[imin]:
                imin = j
        a[i], a[imin] = a[imin], a[i]
    return a

def tri_selection_decroissant(liste):
    a = liste[:]
    n = len(a)
    for i in range(n - 1):
        imax = i
        for j in range(i + 1, n):
            if a[j] > a[imax]:
                imax = j
        a[i], a[imax] = a[imax], a[i]
    return a

if __name__ == "__main__":
    print(tri_selection([64, 25, 12, 22, 11]))
    print(tri_selection_decroissant([5, 2, 8, 1, 9]))
