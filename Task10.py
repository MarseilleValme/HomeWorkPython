# 5 -> 1 0 1 1 0
# 2
from random import randint
n=10
orel=0
reshka=0
for i in range(n):
    coin = randint(0, 1)
    print(coin)
    if coin==0:
        reshka+=1
    else:
        orel+=1
if orel<reshka:
    print(f'Нужно перевернуть {orel} орлов')
else:
    print(f'Нужно перевернуть {reshka} решек')