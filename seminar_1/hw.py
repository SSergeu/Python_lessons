def zad1():#Вапишите программу, которая принимает на вход цифру, 
    #обозначающую день недели, и выводит название этого дня недели

    number = int(input('Введите число: '))
    day_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    if 0 < number < 8:
        print(day_week[number-1])
    else:
        print('Нет такого дня')

def zad2():#Напишите программу, которая принимает на вход
    #координаты двух точек и находит расстояние между ними в 2D пространстве

    Ax=int(input('Ax = '))
    Ay=int(input('Ay = '))
    Bx=int(input('Bx = '))
    By=int(input('By = '))
    result = round(((Ax-Bx)**2+(Ay-By)**2)**0.5,2)
    print(result)

def zad3(): #Напишите программу, которая по заданному номеру четверти, 
    #показывает диапазон возможных координат точек в этой четверти (x и y)

    quarter=int(input('Введите номер четверти: '))
    while quarter < 0 or  quarter > 4:
         quarter=int(input('Введите значение от 1 до 4: '))
    if quarter == 1:
        print ('x > 0, y > 0')
    elif quarter == 2:
        print ('x < 0, y > 0')
    elif quarter == 3:
        print ('x < 0, y < 0')
    elif quarter == 4:
        print ('x > 0, y < 0')

def zad4(): #Напишите программу, которая на вход принимает число (N),
    #а на выходе показывает все чётные числа от 1 до N

    N=int(input('Введите N: '))
    i=2
    while i < N-1:
        print (f'{i},', end=' ')
        i+=2
    print(i)
