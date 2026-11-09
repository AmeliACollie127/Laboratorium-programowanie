liczba1 = float (input())
operator = input()
liczba2 = float (input())
if operator == "+":
    print (liczba1 + liczba2)
if operator == "-":
    print (liczba1 - liczba2)
if operator == "*":
    print (liczba1 * liczba2)
if operator == "/":
    if liczba2 !=0:
        print (liczba1 / liczba2)
    if liczba2 == 0:
        print ("nie można dzielić przez 0")