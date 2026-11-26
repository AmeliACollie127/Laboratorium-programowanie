n = int(input())

wyniki = []

for i in range(n):
    wynik = int(input())
    while wynik < 0 or wynik > 100:
        print("Niepoprawny wynik")
        wynik = int(input())
    wyniki.append(wynik)

suma = 0
zaliczenia = 0

for wynik in wyniki:
    suma += wynik
    if wynik >= 50:
        zaliczenia += 1

srednia = suma / n

print(f"wyniki: {wyniki}")
print(f"srednia: {srednia}")
print(f"liczba zaliczen: {zaliczenia}")
