n = int(input())
liczby = []

for i in range(n):
    liczby.append(int(input()))

szukana = int(input())
znaleziono = False

for indeks in range(len(liczby)):
    if liczby[indeks] == szukana:
        print(f"indeks: {indeks}")
        zaleziono = True
        
if not znaleziono:
    print("Nie znaleziono")
