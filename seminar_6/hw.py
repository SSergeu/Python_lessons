def zad_1(): # Дано натуральное число N. Найдите значение выражения:
    # N + NN + NNN
    N = 132 # или int(input('Введите N: '))
    result = list([int(i*str(N)) for i in range(1,4)]) # list comprehension
    print(sum(result))  # функция sum для списка 



def zad_2(): # Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
    # Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов,
    # совпадающая с введённым числом.
    import random
    array = [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] # = list([random.randint(0,10) for i in range(15)])
    N = 119 #int(input('Введите N: '))
    li = list([int(str(N)[i]) for i in range(3)])
    ind = True
    for i in range(len(array)-2):
        if array[i]==li[0] and array[i+1]==li[1] and array[i+2]==li[2]:
            print('да')
            ind = False
            break
    if ind:
        print('нет')    

def zad_3(): #Найдите все простые несократимые дроби, лежащие между 0 и 1, 
    # знаменатель которых не превышает 11
    for b in range(2,12):
        del_b = set([i for i in range(2,b+1) if b % i == 0])
        for a in range(1,b):
            del_a = set([i for i in range(1,a+1) if a % i == 0])
            if (del_b.intersection(del_a)) == set():
                print(f'{a}/{b}')
