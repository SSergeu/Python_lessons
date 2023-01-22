def zad1(): # Напишите программу, которая составит список простых множителей числа N
    N =int(input('Введите число N: '))  # Вводим число с клавиатуры
    i = 2                               # задаём делитель 
    while N > 1:                        # цикл с условием 'пока число N больше 1'
        if N % i == 0:                  # проверяем, делится ли нацело число на делитель 
            N/=i                        # и если делится то делим (можно использовать вещ. деление, всё равно уже знаем, что делится нацело)
            print(i, end=' ')           # выводим делитель, столько раз, сколько наше число делится на него
        else:
            i+=1                        # а если нет, то увеличиваем делитель на 1

def zad2():
    import re
    data = open('assortment.txt', 'r',encoding='UTF-8')
    list_assort = re.split(', |\n', data.readline())
    if list_assort[len(list_assort)-1]=='':
        list_assort.pop()

    list_in_stok = re.split(', |\n',data.readline())
    if list_in_stok[len(list_in_stok)-1]=='':
        list_in_stok.pop()

    data.close()

    result_list = []
    count = 0
    for i in list_assort:
        for k in list_in_stok:
            if i == k:
                count+=1
                break
        if count == 0:
            result_list.append(i)
        count = 0

    print(f'Отсутствуют: {result_list}')

def zad3():
    from math import pi
    accuracy = int(input('Введите точность: '))
    print(round(pi, accuracy))
   
    
