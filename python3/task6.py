suma = 0
liczbawartosci = 0

liczba = int(input())
while liczba != 0:
    suma += liczba
    liczbawartosci += 1
    liczba = int(input())
print (f"suma: {suma}")
print (f"liczba wartosci: {liczbawartosci}")