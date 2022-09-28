numeros = []

numeros.append(int(input("numero1: ")))
numeros.append(int(input("numero2: ")))
numeros.append(int(input("numero3: ")))
numeros.append(int(input("numero4: ")))
numeros.append(int(input("numero5: ")))

soma = sum(numeros)
media = soma/5

print("a soma dos numeros é: ", soma)
print("amedia dos numeros é: ", media)