n = int(input())

poprawne = 0
for i in range (1, n + 1):
    print(f"podaj kwadrat liczby {i}")
    kwadrat = i * i

    proby = 0 
    odganiete = False

    while proby < 3 and not odganiete:
        odpowiedz = int(input())
        proby += 1

        if odpowiedz == kwadrat:
            print("Poprawna odpowiedz")
            poprawne += 1
            odganiete = True
        else:
            print("Bledna odpowiedz")
print(f"Poprawne rozwiazanie: {poprawne}")
