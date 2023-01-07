def zad1(): # Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # Выведите все элементы, которые меньше 5.
    
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    c = []
    for i in range(len(a)):
        if a[i]<5:
            c.append(a[i])
    print(c)


def zad2(): # Даны списки. Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for i in range(len(a)):
        for k in range(len(b)):
            if a[i]==b[k]:
                c.append(a[i])
    print(c)
    result = list(filter(lambda elem: elem in b, a))
    print(result)

def zad5(): # Найдите три ключа с самыми высокими значениями в словаре
    my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
    sorted_key = sorted(my_dict, key = my_dict.get) # список с ключами по возрастанию их значений 
    sorted_key.reverse() # разворачиваем список чтобы знач были от большего к меньшему 
    print(sorted_key[:3])  # выводим списко используя сечение  

def zad6():# Нужно вывести первые n строк треугольника Паскаля.
    n = int(input('Введите количесвто строк треугольника: '))
    row = [1]
    for i in range(n):
        print(row)
        row = [sum(x) for x in zip([0]+row,row+[0])] # сумма х из объединения 

def zad9(): # Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды
    second = int(input('Введите количество секунд: '))
    day = second//(24*60*60)
    second = second - day * 24*60*60
    hour = second//(60*60)
    second = second - hour * 60*60
    minute = second//60
    second = second - minute * 60
    print(f'{day}:{hour}:{minute}:{second}')


def zad10(): #Вы принимаете от пользователя последовательность чисел, разделённых запятой.
    # Составьте список и кортеж с этими числами
    numbers = input('Введите: ')
    list1 = numbers.split(',') # создание списка используя split
    list1_2 = list(map(int,list1)) # в списке 1_2 конвертим из стринг в инт 
    list2 = tuple(list1_2) # создание кортежа используя tuple
    print(list1_2)
    print(list2)
    
def zad11(): # Выведите первый и последний элемент списка.
    list1 = [0,1,2,3,4]

    print(f'Первый: {list1[0]}; последний: {list1[len(list1)-1]}')
    print(f'Первый: {list1[0]}; последний: {list1[-1]}')

def zad13(): # При заданном целом числе n посчитайте n + nn + nnn
    n = int(input('Введите n: '))
    res = 0
    for i in range(1, 4):
        res = res + n**i
    print(res)

def zad14(): # Напишите программу, которая выводит чётные числа из 
    # заданного списка и останавливается, если встречает число 237
    list = [1, 2, 3, 4, 5, 6, 237, 11, 15, 14]
    for i in list:
        if i % 2 == 0:
            print(i)
        elif i == 237:
            break
    
