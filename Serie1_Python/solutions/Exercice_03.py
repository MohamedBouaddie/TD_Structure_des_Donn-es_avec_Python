distance_km = float(input("Distance (km) : "))
temps_min = float(input("Temps (minutes) : "))

distance_m = distance_km * 1000
temps_s = temps_min * 60

vitesse = distance_m / temps_s
print(f"Vitesse = {vitesse:.2f} m/s")
