import random


n = int(input("insira um numero entre 1 e 10: "))
r = 0
while r <= n:
    r += random.randint(1,10)

print (r)

