n = int(input())
licznik = 0
while licznik < n:
    if licznik == 0:
        wartosc = 0
    else:
        wartosc = 2 ** licznik
    print(f"Python {wartosc}")
    licznik += 1