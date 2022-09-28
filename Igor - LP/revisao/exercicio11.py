numeros = []
cont = 0 
for n in range(0,10,1):
    numeros.append(int(input("insira um nuermo: ")))
    maximo = max(numeros)
    if maximo > 1:
        print("maximo: ", maximo)
        for n2 in range(maximo-1):
            base = numeros[n] 
            verificado = numeros[n2]
            if base == verificado:
                cont += 1

diferentes = 10 - cont

print("total de diferentes: ", diferentes)