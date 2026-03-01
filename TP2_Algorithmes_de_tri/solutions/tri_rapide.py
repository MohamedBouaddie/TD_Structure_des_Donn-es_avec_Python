def partition_premier_pivot(a, debut, fin):
    pivot = a[debut]
    i = debut + 1
    j = fin

    while True:
        while i <= j and a[i] <= pivot:
            i += 1
        while i <= j and a[j] >= pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
        else:
            break

    a[debut], a[j] = a[j], a[debut]
    return j

def quicksort_premier_pivot(a, debut, fin):
    if debut < fin:
        p = partition_premier_pivot(a, debut, fin)
        quicksort_premier_pivot(a, debut, p - 1)
        quicksort_premier_pivot(a, p + 1, fin)

def quicksort_pivot_milieu(a, debut, fin):
    if debut >= fin:
        return
    mid = (debut + fin) // 2
    a[debut], a[mid] = a[mid], a[debut]  # mettre pivot au début
    p = partition_premier_pivot(a, debut, fin)
    quicksort_pivot_milieu(a, debut, p - 1)
    quicksort_pivot_milieu(a, p + 1, fin)

if __name__ == "__main__":
    l1 = [10, 80, 30, 90, 40]
    quicksort_premier_pivot(l1, 0, len(l1) - 1)
    print("Pivot premier :", l1)

    l2 = [7, 2, 1, 6, 8, 5]
    quicksort_pivot_milieu(l2, 0, len(l2) - 1)
    print("Pivot milieu  :", l2)
