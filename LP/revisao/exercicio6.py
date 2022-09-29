x1 = int(input("x1: "))
x2 = int(input("x2: "))
x3 = int(input("x3: "))

if x1 == x2 and x2 == x3:
    print("TODOS SÃO IGUAIS.")
elif x1 <= x2 and x2 < x3:
    if x1 == x2:
        print("x1 e x2 SÃO IGUAIS")
    else:
        print("X1 É O MENOR")
elif x2 < x1 and x2 <= x3:
    if x2 == x3:
        print("x2 e x3 SÃO IGUAIS")
    else:
        print("X2 É O MENOR")
elif x3 < x2 and x3 <= x1:
    if x1 == x3:
        print("x1 e x3 SÃO IGUAIS")
    else:
        print("X3 É O MENOR")