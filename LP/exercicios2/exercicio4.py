#4.	Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
#       A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#       A mensagem "Reprovado", se a média for menor do que sete;
#       A mensagem "Aprovado com Distinção", se a média for igual a dez. 

nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
media = (nota1+nota2)/2

if (media == 10):
    print("Aprovado com Distinção.")
elif (media>=7):
    print("Aprovado.")
else:
    print("Reprovado.")