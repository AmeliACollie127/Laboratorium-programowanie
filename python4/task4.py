n = int(input())

liczby = []
for i in range(n):
    liczby.append(int(input()))

liczby2 = []
for el in liczby:
    if el > 0:
        liczby2.append(el)

print(f"Dodatnie: {liczby2}")
print(f"Liczba dodatnich: {len(liczby2)}")