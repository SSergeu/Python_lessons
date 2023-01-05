def zad1():#Принимает 2 числа и выводит, являются ли любое из них квадратом второго

    number_1 = int(input('Введите 1е число: '))
    number_2 = int(input('Введите 2е число: '))
    if number_1 * number_1 == number_2 or number_2 * number_2 == number_1:
        print('да')
    else:
        print('нет')

def zad2():#Последовательный ввод чисел до тех пор пока не будет 0
    #Посчитать, сколько чисел кратных 3 было введено

    number = int(input('Введите число: '))
    i = 0
    while number != 0:
        if number%3 ==0 :
            i +=1
        number = int(input())
    print(f'Количетсво чисел кратных 3: {i}')

def zad3():#Программа на вход принимает число и выводит числа от -N до N

    N = abs(int(input('Введите N: ')))
    N1 = N*(-1)
    while N1 != N+1:
        print(N1, end=' ')
        N1+=1

def zad4():#Программа принимает дробь и выводит 1-ую цифру дробной части 
    # // - целочисленное деление
    # % - остаток от деления

    number = float(input('Введите дробь: '))
    print(int(number * 10 // 1 % 10))

def zad5():#Максимальное и минимальное значение из списка
    numbers = [-1, 2, 5, -11, 14, 12]
    maxNumbers = numbers[0]
    minNumbers = numbers[0]
    for el in numbers:
        if el > maxNumbers:
            maxNumbers = el
        elif el < minNumbers:
            minNumbers = el
    print (f'Максимальное: {maxNumbers}')
    print (f'Минимальное: {minNumbers}')

