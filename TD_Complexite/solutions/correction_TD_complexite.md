# TD : Initiation à la complexité algorithmique en temps — Correction

Référence : **TD Initiation à la complexité algorithmique en temps 1.pdf** fileciteturn10file5

---

## Exercice 1 : accès au premier élément
Code : `return arr[0]`

1) Complexité : **O(1)** (temps constant)  
2) Elle ne dépend pas de n car on accède directement à l’index 0 (pas de boucle).

---

## Exercice 2 : recherche binaire
1) À chaque itération, on élimine la moitié du tableau ⇒ taille / 2.  
2) Complexité : **O(log n)**.

---

## Exercice 3 : trouver le max avec une boucle
1) La boucle s’exécute **n** fois.  
2) Complexité : **O(n)**.

---

## Exercice 4 : quick sort (pivot milieu, list comprehensions)
1) Plus efficace que tri à bulles car il ne fait pas systématiquement n² comparaisons.
2) Complexité moyenne : **O(n log n)** (partitionnement ~ log n niveaux, et on traite ~ n éléments par niveau).

---

## Exercice 5 : bubble sort (2 boucles imbriquées)
1) Deux boucles : pour faire plusieurs passages + comparer/échanger voisins.
2) Complexité : **O(n²)**.

---

## Exercice 6 : Fibonacci récursif naïf
1) Appels récursifs explosent (répétitions). Pour n=5, on observe beaucoup d’appels redondants.
2) Temps explose car on recalcule plusieurs fois les mêmes valeurs ⇒ **O(φ^n)** (≈ O(2^n)).

---

## Exercice 7 : permutations
1) Pour 4 éléments : **4! = 24** permutations.
2) Complexité : **O(n!)**.

---

## Travail demandé (mesures)
Voir le script `benchmark_complexite.py` : il exécute les fonctions avec n=10 et n=20, mesure le temps et compare qualitativement avec la théorie.
