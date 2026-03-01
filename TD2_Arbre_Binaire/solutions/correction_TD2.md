# TD2 : Arbre binaire — Correction (représentation + parcours)

Référence : **TD 2 arbre.pdf** fileciteturn10file4

---

## I) Définitions (résumé)

- **Nœud (sommet)** : élément contenant une valeur.
- **Arête** : lien entre deux nœuds (parent → enfant).
- **Racine** : nœud tout en haut, sans parent.
- **Feuille** : nœud sans enfants.
- **Sous-arbre** : partie de l’arbre (ex : sous-arbre gauche).
- **Hauteur** : nombre de niveaux (longueur max racine→feuille, en nœuds).

---

## II) Représentation en liste [r, G, D]

### Exercice 1
Arbre (racine 14) :

```python
A1 = [14,
      [7,
       [3, [], []],
       [10, [8, [], []], []]
      ],
      [20,
       [17, [16, [], []], [18, [], []]],
       [25, [], []]
      ]
]
```

---

## III) Manipulation

On utilise les fonctions :
- `ValRacine(A)`, `FilsGauche(A)`, `FilsDroit(A)`, `EstVide(A)`, `EstFeuille(A)`

(voir `outils_arbre.py`).

---

## Exercice 2

### 1) Représentation en liste
```python
A = [50,
     [25,
      [12, [7, [], []], [18, [], [19, [], []]]],
      [37, [30, [], []], [44, [41, [], []], [46, [], []]]]
     ],
     [80,
      [65, [58, [], [59, [], []]], [70, [68, [66, [], []], []], []]],
      [92, [86, [], []], [97, [], [99, [], []]]]
     ]
]
```

### 2) Résultats des appels
- `FilsGauche(A)` = sous-arbre dont la racine est **25**
- `FilsDroit(A)` = sous-arbre dont la racine est **80**
- `ValRacine(A)` = **50**
- `FilsDroit(FilsDroit(A))` = sous-arbre dont la racine est **92**
- `EstFeuille(FilsDroit(A))` = **False** (80 a des enfants)

---

## IV) Parcours d’un arbre

Rappel :
- **Préfixe** : r → SAG → SAD
- **Infixe** : SAG → r → SAD
- **Postfixe** : SAG → SAD → r

---

## Exercice 3

### 1) Représentation en liste
```python
A3 = [50,
      [25,
       [10, [5, [], []], [15, [], []]],
       [35, [30, [28, [], []], []], [40, [], []]]
      ],
      [75,
       [60, [55, [], []], [65, [], [70, [], []]]],
       [90, [85, [], []], [95, [], [100, [], []]]]
      ]
]
```

### 2) Nombre total de nœuds et de feuilles
- nœuds = **18**
- feuilles = **8**

### 3) Hauteur
- hauteur = **5** niveaux

### 4) Parcours
- **Préfixe** : 50, 25, 10, 5, 15, 35, 30, 28, 40, 75, 60, 55, 65, 70, 90, 85, 95, 100
- **Infixe**  : 5, 10, 15, 25, 28, 30, 35, 40, 50, 55, 60, 65, 70, 75, 85, 90, 95, 100
- **Postfixe**: 5, 15, 10, 28, 30, 40, 35, 25, 55, 70, 65, 60, 85, 100, 95, 90, 75, 50
