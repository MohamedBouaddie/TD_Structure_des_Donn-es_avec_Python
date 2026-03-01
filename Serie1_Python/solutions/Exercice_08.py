notes = []
coeffs = []
for i in range(1, 5):
    n = float(input(f"Note {i} : "))
    c = float(input(f"Coefficient {i} : "))
    notes.append(n)
    coeffs.append(c)

s = 0
sc = 0
for n, c in zip(notes, coeffs):
    s += n * c
    sc += c

moy = s / sc
print(f"Moyenne = {moy:.2f}")

if moy >= 10:
    print("Semestre validé")
elif moy >= 7:
    print("Rattrapage")
else:
    print("Non validé")
