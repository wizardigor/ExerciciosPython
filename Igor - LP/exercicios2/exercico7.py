#7.	Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("produto 1: "))
p2 = float(input("produto 2: "))
p3 = float(input("produto 3: "))

if (p1 == p2 and p2 == p3):
    print("Os produtos teem o mesmo preço.")
elif (p1 >= p2 and p2 >= p3):
    print("O mais barato: ",p3,".")
elif (p1 >= p3 and p3 >= p2):
    print("O mais barato: ",p2,".")
elif (p2 >= p1 and p1 >= p3):
    print("O mais barato: ",p3,".")
elif (p2 >= p3 and p3 >= p1):
    print("O mais barato: ",p1,".")
elif (p3 >= p1 and p1 >= p2):
    print("O mais barato: ",p2,".")
elif (p3 >= p2 and p2 >= p1):
    print("O mais barato: ",p1,".")