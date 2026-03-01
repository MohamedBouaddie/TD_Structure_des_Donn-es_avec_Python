def tri_bulles(liste):
    a = liste[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def tri_bulles_optimise(liste):
    a = liste[:]
    n = len(a)
    for i in range(n):
        echange = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                echange = True
        if not echange:
            break
    return a

if __name__ == "__main__":
    print(tri_bulles([5, 1, 4, 2, 8]))
    print(tri_bulles_optimise([5, 1, 4, 2, 8]))
