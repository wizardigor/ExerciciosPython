#11.	Faça um Programa que peça 2 números inteiros e um número real. 
# Calcule e mostre o produto do dobro do primeiro com metade do segundo. 
# A soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo. 

def numeros(n1, n2, n3):
    c1= (n1*2)*(n2/2)
    c2= (n1*3)+n3
    c3= pow(n3,3)
   
    print('produto: ')
    print(c1)
    print('soma: ')
    print(c2)
    print('protencia: ')
    print(c3)

numeros(14, 4, 9)
