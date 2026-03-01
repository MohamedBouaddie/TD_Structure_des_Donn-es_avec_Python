import time
import itertools
import random

def get_first_element(arr):
    return arr[0]

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_max(arr):
    max_val = arr[0]
    for v in arr:
        if v > max_val:
            max_val = v
    return max_val

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def bubble_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def generate_permutations(arr):
    return list(itertools.permutations(arr))

def bench(title, func, *args):
    t0 = time.time()
    func(*args)
    t1 = time.time()
    return title, (t1 - t0)

def main():
    for n in [10, 20]:
        arr = list(range(n))
        arr_sorted = arr[:]  # pour binaire
        target = n-1

        tests = [
            bench(f"O(1) accès premier (n={n})", get_first_element, arr),
            bench(f"O(log n) recherche binaire (n={n})", binary_search, arr_sorted, target),
            bench(f"O(n) max (n={n})", find_max, arr),
            bench(f"O(n log n) quicksort (n={n})", quick_sort, random.sample(range(n*10), n)),
            bench(f"O(n^2) bubble sort (n={n})", bubble_sort, random.sample(range(n*10), n)),
        ]

        print("\n=== Mesures n =", n, "===")
        for title, dt in tests:
            print(f"{title:<40} : {dt:.6f}s")

    # Fibonacci : garder n petit sinon trop lent
    for n in [5, 10, 20]:
        title, dt = bench(f"Fibonacci naïf (n={n})", fibonacci, n)
        print(f"{title:<40} : {dt:.6f}s")

    # Permutations : garder n petit (n!)
    for n in [4, 5]:
        arr = list(range(n))
        title, dt = bench(f"Permutations (n={n})", generate_permutations, arr)
        print(f"{title:<40} : {dt:.6f}s")

if __name__ == "__main__":
    main()
