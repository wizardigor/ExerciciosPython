#12.	Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule 
# seu peso ideal, usando a seguinte fórmula: (72.7*altura) – 58 Tendo como dado de entrada a 
# altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as 
# seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7 


def alturaHomem(h):
    print((72.7*h)-58)

def alturaMulher(h):
    print((62.1*h) - 44.7)


alturaHomem(1.75)

alturaMulher(1.65)