# Outils généraux (liste [r, G, D])
def ValRacine(A):
    return A[0] if A != [] else None

def FilsGauche(A):
    return A[1] if A != [] else []

def FilsDroit(A):
    return A[2] if A != [] else []

def EstVide(A):
    return A == []

def EstFeuille(A):
    return A != [] and A[1] == [] and A[2] == []

def n_nodes(A):
    if A == []:
        return 0
    return 1 + n_nodes(A[1]) + n_nodes(A[2])

def n_leaves(A):
    if A == []:
        return 0
    if EstFeuille(A):
        return 1
    return n_leaves(A[1]) + n_leaves(A[2])

def hauteur(A):
    if A == []:
        return 0
    return 1 + max(hauteur(A[1]), hauteur(A[2]))

def prefixe(A):
    if A == []:
        return []
    return [A[0]] + prefixe(A[1]) + prefixe(A[2])

def infixe(A):
    if A == []:
        return []
    return infixe(A[1]) + [A[0]] + infixe(A[2])

def postfixe(A):
    if A == []:
        return []
    return postfixe(A[1]) + postfixe(A[2]) + [A[0]]
