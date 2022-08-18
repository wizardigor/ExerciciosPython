#1.	Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("primeiro numero: "))
n2 = int(input("segundo numero: "))

if (n1 > n2):
    print("O prieiro numero é maior.")
elif (n1 == n2):
    print("Os numeros são iguais.")
else:
    print("O segundo numero é maior.")
