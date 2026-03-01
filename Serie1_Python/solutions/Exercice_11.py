poids = float(input("Poids (kg) : "))
taille = float(input("Taille (m) : "))

imc = poids / (taille ** 2)
print(f"IMC = {imc:.2f}")

if imc > 40:
    print("Obésité morbide ou massive")
elif imc >= 35:
    print("Obésité sévère")
elif imc >= 30:
    print("Obésité modérée")
elif imc >= 25:
    print("Surpoids")
elif imc >= 18.5:
    print("Corpulence normale")
elif imc >= 16.5:
    print("Maigreur")
else:
    print("Famine")
