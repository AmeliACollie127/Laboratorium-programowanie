n = int(input())

if n>= 0:
    for i in range(n):
        if i == 0:
            wartosc = 0
        else:
            wartosc = 2 ** i
        print(f"Python {wartosc}")
