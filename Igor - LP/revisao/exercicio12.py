valores = []
encontrou = False

for n in range(10):
    valores.append(input("insira um valor: "))

buscar = input("bucar: ")

for n in range(0,10,1):
    if buscar == valores[n]:
        encontrou = True
        print("o valor de busca estar na posição: ", n)

if encontrou != True:
    print("valor-1")