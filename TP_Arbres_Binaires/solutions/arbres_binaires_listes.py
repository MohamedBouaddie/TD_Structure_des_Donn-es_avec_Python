# Représentation : arbre = [valeur, gauche, droite] ; arbre vide = []

def NbreNoeuds(arbre):
    if arbre == []:
        return 0
    return 1 + NbreNoeuds(arbre[1]) + NbreNoeuds(arbre[2])

def hauteur(arbre):
    if arbre == []:
        return 0
    return 1 + max(hauteur(arbre[1]), hauteur(arbre[2]))

def MaxArb(arbre):
    if arbre == []:
        return None
    m = arbre[0]
    mg = MaxArb(arbre[1])
    md = MaxArb(arbre[2])
    if mg is not None and mg > m:
        m = mg
    if md is not None and md > m:
        m = md
    return m

if __name__ == "__main__":
    A = [10, [5, [], []], [20, [15, [], []], []]]
    print("NbreNoeuds:", NbreNoeuds(A))
    print("Hauteur  :", hauteur(A))
    print("Max      :", MaxArb(A))
