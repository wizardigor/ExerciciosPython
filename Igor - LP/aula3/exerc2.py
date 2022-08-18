#IMC = massa_kg/(altura_m) elevado ao quadrado
#Git Hub

peso= float(input("insera seu peso: "))

altura= float(input("insera sua altura: "))

imc = peso/pow(altura,2)

if (imc<18.5):
   print("seu imc é: ",imc, "ABAIXO DO PESO.")
elif (imc>18.5 and imc<=25):
    print("seu imc é: ",imc, "SAUDAVEL.")
elif (imc>25 and imc<=30):
    print("seu imc é: ",imc, "PESO EM EXCESSO.")
elif (imc>30 and imc<=35):
    print("seu imc é: ",imc, "OBESIDADE GRAU I.")
elif (imc>35 and imc<=40):
    print("seu imc é: ",imc, "OBESIDADE GRAU II (SEVERA).")
else:
    print("seu imc é: ",imc, "OBESIDADE GRAU III (MORBIDA).")