liczba_punktow = int(input())

if liczba_punktow >= 10:
    print("zaliczone")
else:
    brakujace = 10 - liczba_punktow
    print("niezaliczone")
    print (f"brakuje punktow: {brakujace}")