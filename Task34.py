# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться
# в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух
# вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам
poem = 'пара-ра-рам-пи рам-пам-папам-пу па-ра-па-да-да'
print(poem)
phrase = poem.split()

for i in range(len(phrase)):
    phrase[i] = sum(1 for x in filter(lambda x: x in 'аяуюоеёэиы', phrase[i]))#Перезаписываем в список подстрок кол-во гласных букв в 
                                                                              #этих подстроках

if len(set(phrase)) == 1:   #Если кол-во гласных оказалось одинаковым во всех подстроках, set, убрав повторы, сведёт всё к одному элементу
    print('Парам пам-пам')
else:
    print('Пам парам')  #Если множество получилось из больше одного элемента - значит кол-во гласных в подстроках было разное
