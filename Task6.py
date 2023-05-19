b = int(input('Введите номер билета: '))
sum = 0
while (b > 0):
    if (b>1000):
        sum = sum+b % 10
        b = b//10
    else:
        sum = sum-b % 10
        b = b//10
if (sum==0):
    print('Билет счастливый')
else:
    print('Билет несчастный')