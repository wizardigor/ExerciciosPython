
inicio = int(input("inicio: "))
fim = int(input("final: "))
r = 0

for num in range(inicio,fim+1):
    if num % 2 == 0:
        r += num

print(r)

