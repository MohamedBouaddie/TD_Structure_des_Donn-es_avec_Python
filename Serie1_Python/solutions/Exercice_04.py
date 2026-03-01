sec = int(input("Nombre de secondes : "))

h = sec // 3600
sec = sec % 3600
m = sec // 60
s = sec % 60

print(f"{h}h {m}min {s}sec")
