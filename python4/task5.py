n = int(input())

liczby = []
for i in range(n):
    liczby.append(int(input()))

max = liczby[0]
for el in liczby:
    if el > max:
        max = el
print(f"Najwieksza: {max}")