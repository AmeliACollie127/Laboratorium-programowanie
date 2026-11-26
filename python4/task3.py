n = int(input())
liczby = []

for i in range(n):
    liczby.append(int(input()))

suma = 0
for el in liczby:
    suma += el

srednia = suma / n

print(f"Suma elementow listy: {suma}")
print(f"Srednia elementow listy: {srednia}")
