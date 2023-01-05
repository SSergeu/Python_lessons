def factorial (number): # факториал числа 
    k = 1
    for i in range(number):
        k*=i+1
    return k


def zad1(): # Напишите программу, которая принимает на вход число N
    # и выдает список факториалов для чисел от 1 до N

    N = int(input('Введите N: '))
    for x in range(1, N):
        print (f'{factorial(x)},',end=' ')
    print(factorial(N))

def zad2(): #  Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z
    print ('x | y | z | f')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                
                print (f'{x} | {y} | {z} | {int(not x and not y or z)}')

def zad3(): # посчитайте сколько раз каждый символ первой строки встречается во второй
    symbols = 'one'
    text = 'onetwonine'

    for x in symbols:
        k = 0
        for y in text:
            if (x == y):
                k+=1         
        print(f'{x} - {k}')

def zad4(): #  Задайте список из N элементов, заполненных числами из промежутка [-N, N]
    # Сдвиньте все элементы списка на 2 позиции вправо
    N = int(input('Введите N: '))
    list = []
    k = N-1
    for x in range (2):
         list.append(k)
         k+=1
    k = -N
    for x in range((N*2)-1):
        list.append(k)
        k+=1
    print(list)
